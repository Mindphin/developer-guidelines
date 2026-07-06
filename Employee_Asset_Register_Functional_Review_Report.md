# Employee Asset Register Functional Review Report

**Module Reviewed:** `md_employee_asset_register.zip`  
**Target Version:** Odoo 18.0  
**Review Date:** 03 July 2026  
**Review Scope:** Functional correctness against TRD only. Non-functional
delivery standards are intentionally excluded from this report.
**Test Database:** `md_asset_register_test_20260703`

## Summary

The module installs successfully in Odoo 18 and is functionally close to the
TRD. The main asset register, category model, employee integration, sequence,
default categories, menus, views, workflow buttons, and validations are mostly
implemented.

I found a few functional issues/risks that should be fixed or confirmed before
acceptance:

1. `Asset Code` is not technically required on the model.
2. `Mark Assigned` does not validate the employee before changing state.
3. Asset action includes `search` in `view_mode`, which is not a normal Odoo
   action view mode and may cause action/view loading issues.
4. Default search grouping by Status is not applied.
5. Chatter does not create tracking messages for tracked field changes.
6. Asset count exists in Python but is not exposed in the employee UI.

Python syntax checks, XML parsing, Odoo module installation, and ORM functional
tests were executed.

## Checks Performed

| Check | Result |
| --- | --- |
| Python syntax compile | Pass |
| XML well-formed parsing | Pass |
| Manifest dependency/data order review | Pass |
| Odoo 18 module install on clean DB | Pass |
| ORM functional test suite | Fail: 5 failed out of 30 checks |
| Browser/UI functional test | Not Run |

## Odoo ORM Test Result Summary

| Result | Test |
| --- | --- |
| Pass | Module installed. |
| Fail | Asset Code field is not marked required. |
| Pass | Default Mouse category is available. |
| Pass | Asset Code auto-generates as `AST-00001`. |
| Pass | Default status is In Stock. |
| Pass | Default condition is New. |
| Pass | Duplicate Asset Code is blocked. |
| Pass | Assigned state requires employee. |
| Pass | Assigned state requires assigned date. |
| Pass | Return Date before Assigned Date is blocked. |
| Fail | Mark Assigned does not set status and assigned date. |
| Pass | Mark Assigned without employee is blocked. |
| Pass | Mark Returned sets status and return date. |
| Pass | Mark Damaged sets status and condition. |
| Pass | Mark Lost sets status. |
| Pass | Scrap sets status and keeps record active. |
| Pass | Employee One2many includes linked assets. |
| Pass | Employee asset count counts assigned assets. |
| Pass | Employee Assigned Assets tab view exists. |
| Pass | Asset action exists. |
| Fail | Asset action contains invalid/unwanted `search` view mode. |
| Fail | Asset action does not apply default Status grouping. |
| Pass | Search filters exist: Assigned, In Stock, Returned, Damaged, Lost, Scrapped, Archived. |
| Fail | Chatter does not record tracked field changes. |

## Functional Findings

### 1. Asset Code Is Not Marked Required

**Severity:** Medium  
**Requirement:** Asset Code is mandatory, unique, and auto-generated if not
entered.

**Current Code:**

`models/md_employee_asset.py`, lines 20-24:

```python
md_asset_code = fields.Char(
    string="Asset Code",
    copy=False,
    tracking=True,
)
```

The field has a unique SQL constraint and sequence generation in `create()`, so
records created through normal ORM create should receive a code. However, the
field is not marked `required=True`, so the model definition does not fully
enforce the requirement that Asset Code is mandatory.

**Recommended Fix:**

Use a placeholder default so the form can save and `create()` can replace it:

```python
md_asset_code = fields.Char(
    string="Asset Code",
    required=True,
    copy=False,
    default="/",
    tracking=True,
)
```

Keep the existing create logic that replaces empty or `/` with the sequence.

### 2. Mark Assigned Does Not Validate Employee Before State Change

**Severity:** Medium  
**Requirement:** Button `Mark Assigned` must validate that employee is selected,
then set status and assigned date.

**Current Code:**

`models/md_employee_asset.py`, lines 131-135:

```python
def action_mark_assigned(self):
    for record in self:
        record.state = "assigned"
        if not record.md_assigned_date:
            record.md_assigned_date = fields.Date.context_today(self)
```

The general constraint will raise a validation error after the state is changed
if no employee is selected. Functionally this may still block the invalid write,
but the button logic does not follow the required flow and can produce a less
controlled user experience.

During live ORM testing, this method also failed for a valid asset with an
employee selected. Because it writes `state = "assigned"` before assigning
`md_assigned_date`, the constraint runs immediately and raises:

```text
ValidationError: Assigned Date is required when Status is Assigned.
```

**Recommended Fix:**

```python
def action_mark_assigned(self):
    for record in self:
        if not record.md_employee_id:
            raise ValidationError(
                "Assigned Employee is required when Status is Assigned."
            )
        record.state = "assigned"
        if not record.md_assigned_date:
            record.md_assigned_date = fields.Date.context_today(record)
```

### 3. Asset Action Uses Invalid/Unnecessary `search` View Mode

**Severity:** Medium  
**Requirement:** Asset list, form, kanban, and search views must be available.

**Current Code:**

`views/menus.xml`, line 7:

```xml
<field name="view_mode">list,form,kanban,search</field>
```

In Odoo actions, `search` is not normally included in `view_mode`. Search views
are defined separately and automatically used by the action/model. Including
`search` can cause action loading issues depending on Odoo version behavior.

**Recommended Fix:**

```xml
<field name="view_mode">list,form,kanban</field>
```

Keep the existing `md_employee_asset_view_search` record.

### 4. Default Group By Status Is Not Applied

**Severity:** Low  
**Requirement:** Asset search view should have default group by Status.

**Current Code:**

The search view defines a Status group-by filter:

`views/md_employee_asset_views.xml`, line 128:

```xml
<filter name="group_by_state" string="Status" context="{'group_by': 'state'}"/>
```

But the action does not set default context to apply it automatically.

**Recommended Fix:**

Add context on the asset action:

```xml
<field name="context">{'search_default_group_by_state': 1}</field>
```

Or use the exact default key matching the final filter name if changed.

### 5. Asset Count Is Implemented But Not Exposed

**Severity:** Low  
**Requirement:** Assigned asset count is available if implemented as a smart
button or computed field.

**Current Code:**

`models/hr_employee.py`, lines 15-27 implements `md_asset_count`, but
`views/hr_employee_views.xml` only adds the Assigned Assets One2many tab. The
count is not shown on the employee form.

This is not a hard failure because the TRD says "if implemented as a smart
button or computed field", and the computed field exists. However, from a user
perspective it is not available in the UI.

**Recommended Fix:**

Either:

- Add a smart button showing `md_asset_count`, or
- Add the count field in the employee form where appropriate.

### 6. Chatter Tracking Does Not Record Field Changes

**Severity:** Medium  
**Requirement:** Chatter should track business-critical field changes such as
Status, Assigned Employee, and Condition.

**Live Test Result:**

Creating an asset added the standard creation message, but changing a tracked
field did not add a new tracking message or tracking values.

Test evidence:

```text
before_count 1
after_count 1
tracking_values []
```

The model fields are configured with tracking metadata, but the expected chatter
tracking behavior did not occur during the Odoo ORM test.

**Recommended Fix:**

Investigate why `mail.thread` tracking is not posting tracking values on write
for `md.employee.asset`. After the fix, changing `state`, `md_condition`, or
`md_employee_id` should create a new chatter message with tracking values.

## Requirement Coverage

| Requirement | Status | Notes |
| --- | --- | --- |
| Create/manage asset records | Pass | Asset model and views exist. |
| Asset category configuration | Pass | Category model, views, and default data exist. |
| Assign assets to employees | Pass | `md_employee_id`, onchange, and employee tab exist. |
| Track asset status | Pass | `state` field, statusbar, filters, buttons exist. |
| Track asset condition | Pass | `md_condition` field and damaged logic exist. |
| Employee form Assigned Assets tab | Pass | Added through inherited employee view. |
| Dedicated menus/actions | Pass with risk | Menus exist; action `view_mode` should remove `search`. |
| List/form/search/kanban views | Pass | All are present. |
| Default filters/groupings | Partial | Filters/group-by exist; default group by Status not applied. |
| Chatter tracking | Fail | Field tracking metadata exists, but live write did not create tracking messages. |
| Security group/access rights | Pass | Menus/access restricted to manager group. |
| Asset code sequence | Pass | Sequence exists and create method uses it. |
| Asset code unique | Pass | SQL constraint exists. |
| Asset code mandatory | Partial | Auto-generation exists, but field is not `required=True`. |
| Assigned validation | Partial | Constraint exists; button should validate before state change. |
| Return date validation | Pass | Constraint exists. |
| Mark returned | Pass | Sets returned and return date. |
| Mark damaged | Pass | Sets damaged status and condition. |
| Mark lost | Pass | Sets lost status. |
| Scrap | Pass | Sets scrapped and does not archive. |
| Employee asset count | Partial | Computed, but not visible in UI. |

## Recommended Functional Test Cases In Odoo 18

Run these after applying the fixes:

1. Install the module on a clean Odoo 18 database.
2. Open Employees > Asset Register > Assets.
3. Create an asset without entering Asset Code and confirm `AST-00001` is
   generated.
4. Try duplicate Asset Code and confirm unique validation.
5. Click Mark Assigned without employee and confirm a validation error appears.
6. Select employee and confirm Assigned Date auto-fills and status becomes
   Assigned.
7. Click Mark Returned and confirm Return Date auto-fills.
8. Set Return Date earlier than Assigned Date and confirm validation error.
9. Click Mark Damaged and confirm Condition becomes Damaged.
10. Click Mark Lost and Scrap and confirm statuses update correctly.
11. Open the employee form and confirm the Assigned Assets tab shows linked
    assets.
12. Confirm search filters and group-by options work.
13. Confirm chatter creates tracking messages for status/condition/employee changes.
14. Confirm the asset action opens without errors after removing `search` from
    `view_mode`.

## Functional Acceptance Decision

**Status:** Not fully accepted yet.

The module is mostly aligned with the functional requirement, but the developer
should fix the medium findings before final acceptance:

- Make Asset Code truly mandatory while preserving sequence auto-generation.
- Validate employee explicitly in `action_mark_assigned()`.
- Remove `search` from the asset action `view_mode`.
- Fix chatter tracking so field changes create tracking messages.

The low findings can be fixed in the same pass or accepted if the team is
comfortable with the current behavior.
