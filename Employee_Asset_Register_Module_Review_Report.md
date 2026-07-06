# Employee Asset Register Module Review Report

**Module Reviewed:** `md_employee_asset_register.zip`  
**Target Version:** Odoo 18.0  
**Review Date:** 03 July 2026  
**Review Type:** Static code review against TRD + syntax checks

## Review Summary

The module partially satisfies the TRD. Core models, fields, menus, views,
sequence data, category data, and basic workflow methods are present. However,
the delivery is not ready for acceptance because several required deliverables
are missing, the shared zip contains generated/local artifacts, and some logic
does not fully match the TRD.

Full install/functional testing in an Odoo database was not executed in this
workspace because no Odoo 18 server/configuration is available here. Static
Python compilation and XML parsing were executed successfully.

## Test Results

| Test | Result | Notes |
| --- | --- | --- |
| Python syntax compile | Pass | All `.py` files compile successfully. |
| XML well-formed parsing | Pass | All XML files parse successfully. |
| Manifest presence | Pass | Manifest exists and has required base metadata. |
| Required README | Fail | `README.md` is missing. |
| Required i18n files | Fail | `i18n/de_CH.po`, `i18n/fr_CH.po`, and `i18n/it_IT.po` are missing. |
| Required static description files | Fail | `static/description/icon.png` and `static/description/index.html` are missing. |
| Zip hygiene | Fail | Zip contains `__MACOSX` and `__pycache__` artifacts. |
| Odoo install test | Not Run | Requires Odoo 18 runtime/database. |

## Must Fix Before Acceptance

### 1. Missing Required Deliverables

**Severity:** High  
**TRD Requirement:** Module must include `README.md`, required `i18n` files, and
static app description files.

**Current Issue:**

- `README.md` is not present.
- `i18n/` directory exists but contains no `.po` files.
- `static/description/` directory exists but contains no `icon.png` or
  `index.html`.
- Manifest image entry is commented out in `__manifest__.py`.

**Evidence:**

- `__manifest__.py`, line 28:

```python
# "images": ["static/description/icon.png"],
```

**Expected Fix:**

- Add `README.md`.
- Add:
  - `i18n/de_CH.po`
  - `i18n/fr_CH.po`
  - `i18n/it_IT.po`
- Add:
  - `static/description/icon.png`
  - `static/description/index.html`
- Uncomment/add manifest images:

```python
"images": ["static/description/icon.png"],
```

### 2. Shared Zip Contains Generated and Local System Files

**Severity:** High  
**TRD Requirement:** Do not share/commit generated cache files or local artifacts.

**Current Issue:**

The zip contains:

- `__MACOSX/`
- `md_employee_asset_register/__pycache__/`
- `md_employee_asset_register/models/__pycache__/`
- Multiple `.pyc` files

**Expected Fix:**

Regenerate the module zip after removing:

```text
__MACOSX/
__pycache__/
*.pyc
```

### 3. Validation Messages Are Not Translation Ready

**Severity:** High  
**TRD Requirement:** All user-facing validation messages must use `_()`.

**Current Issue:**

`models/md_employee_asset.py` imports only:

```python
from odoo import api, fields, models
```

Validation errors use plain strings, not `_()`.

**Evidence:**

- `models/md_employee_asset.py`, lines 177-194.

**Expected Fix:**

Import `_` and wrap messages:

```python
from odoo import _, api, fields, models
```

```python
raise ValidationError(
    _("Assigned Employee is required when Status is Assigned.")
)
```

Apply the same for all validation messages and SQL constraint messages where
applicable.

### 4. Asset Code Field Is Not Marked Required

**Severity:** Medium  
**TRD Requirement:** Asset Code is mandatory and unique, auto-generated if not
entered.

**Current Issue:**

`md_asset_code` is unique and auto-generated in `create()`, but the field itself
is not marked `required=True`.

**Evidence:**

- `models/md_employee_asset.py`, lines 20-24.

**Expected Fix:**

Set:

```python
md_asset_code = fields.Char(
    string="Asset Code",
    required=True,
    copy=False,
    tracking=True,
)
```

Keep the `create()` sequence logic so manual entry remains optional in the UI
only if the developer intentionally handles draft values before save. If Odoo
blocks empty required fields before `create()`, use a default value of `/`.

### 5. Mark Assigned Button Does Not Explicitly Validate Employee First

**Severity:** Medium  
**TRD Requirement:** `action_mark_assigned()` must validate that employee is
selected, then set status and assigned date.

**Current Issue:**

The method sets `state = "assigned"` first and relies on model constraints to
raise an error afterward if no employee is selected.

**Evidence:**

- `models/md_employee_asset.py`, lines 131-135.

**Expected Fix:**

Validate first:

```python
def action_mark_assigned(self):
    for record in self:
        if not record.md_employee_id:
            raise ValidationError(
                _("Assigned Employee is required when Status is Assigned.")
            )
        record.state = "assigned"
        if not record.md_assigned_date:
            record.md_assigned_date = fields.Date.context_today(record)
```

### 6. Security Group Does Not Match TRD Label/Scope Exactly

**Severity:** Medium  
**TRD Requirement:** Create one group named `Employee Asset Manager` with XML ID
`md_group_employee_asset_manager`.

**Current Issue:**

The module creates two groups:

- `md_group_employee_asset_user` with label `User`
- `md_group_employee_asset_manager` with label `Manager`

**Evidence:**

- `security/md_employee_asset_register_groups.xml`, lines 10-19.

**Expected Fix:**

Use one group unless a second role is explicitly approved:

```xml
<record id="md_group_employee_asset_manager" model="res.groups">
    <field name="name">Employee Asset Manager</field>
    ...
</record>
```

Remove the extra user group if not required.

### 7. Asset Action Includes `search` in `view_mode`

**Severity:** Medium  
**TRD Requirement:** Asset list, form, kanban, and search views must be
available. Search views are linked automatically by model/action; `search` is
not normally included in `view_mode`.

**Current Issue:**

`view_mode` is:

```xml
list,form,kanban,search
```

**Evidence:**

- `views/menus.xml`, line 7.

**Expected Fix:**

Use:

```xml
<field name="view_mode">list,form,kanban</field>
```

Keep the search view record in `views/md_employee_asset_views.xml`.

## Should Fix

### 8. Manifest Contains Commented-Out Code

**Severity:** Low  
**Current Issue:** Manifest has a commented-out `images` entry.

**Evidence:**

- `__manifest__.py`, line 28.

**Expected Fix:** Remove commented-out manifest code and add the real `images`
entry once the icon exists.

### 9. SQL Constraint Formatting Is Hard to Read

**Severity:** Low  
**Current Issue:** `_sql_constraints` is written on one compressed line.

**Evidence:**

- `models/md_employee_asset.py`, lines 111-112.

**Expected Fix:**

Format as:

```python
_sql_constraints = [
    (
        "md_employee_asset_code_unique",
        "unique(md_asset_code)",
        _("Asset Code must be unique."),
    ),
]
```

### 10. Computed Asset Count May Be Inefficient on Large Employee Lists

**Severity:** Low  
**Current Issue:** `md_asset_count` filters `employee.md_asset_ids` in Python.
This is acceptable for small datasets but can be inefficient when opening many
employees.

**Evidence:**

- `models/hr_employee.py`, lines 16-24.

**Suggested Fix:**

Use `read_group()` if this count is shown in list views, smart buttons, or any
screen with many employees.

## Requirement Coverage

| Requirement Area | Status | Notes |
| --- | --- | --- |
| Module technical name | Pass | Folder and manifest use `md_employee_asset_register`. |
| Core asset model | Partial | Model exists; `md_asset_code` should be required. |
| Category model | Pass | Model and default categories exist. |
| Employee extension | Pass | One2many and assigned count exist. |
| Sequence | Pass | Sequence exists and is used in `create()`. |
| Status and condition workflow | Partial | Core methods exist; assigned action should validate first. |
| Constraints | Partial | Validation exists but messages are not translatable. |
| Views | Partial | Views exist; action `view_mode` should be corrected. |
| Menus | Pass | Menus are restricted to manager group. |
| Security | Partial | Access exists, but group design/name differs from TRD. |
| Chatter tracking | Pass | Required tracked fields are configured. |
| Translation readiness | Fail | Required `.po` files missing and validation strings not wrapped in `_()`. |
| Static app description | Fail | Required files missing. |
| README | Fail | Missing. |
| Repository/package hygiene | Fail | Generated/local artifacts included in zip. |

## Recommended Developer Test Plan

After fixing the issues above, test in Odoo 18:

1. Install the module on a clean database.
2. Upgrade the module without errors.
3. Confirm only Employee Asset Manager users can see the Asset Register menus.
4. Create an asset without entering Asset Code and confirm sequence generates
   `AST-00001`.
5. Try creating a duplicate Asset Code and confirm the unique constraint error.
6. Try marking an asset Assigned without an employee and confirm the validation
   message.
7. Assign an employee and confirm Assigned Date is auto-filled.
8. Mark Returned and confirm Return Date is auto-filled.
9. Enter Return Date earlier than Assigned Date and confirm validation error.
10. Mark Damaged and confirm Condition changes to Damaged.
11. Open an employee and confirm the Assigned Assets tab shows linked assets.
12. Confirm Asset Count includes only assigned assets.
13. Confirm chatter tracks changes to the required fields.
14. Confirm filters and group-by options work in the asset search view.
15. Export translations and update the required `.po` files if needed.

## Final Review Decision

**Status:** Not accepted yet.

The developer should fix the high and medium issues, regenerate a clean module
zip, and then run a clean Odoo 18 install/upgrade/functional test pass.
