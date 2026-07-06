# Odoo Development Checklist

<a href="https://github.com/Mindphin/developer-guidelines/archive/refs/heads/mindphin.zip" download>Download the starter repository ZIP</a>

## Purpose

This document defines the mandatory development and review standards for custom
Odoo 19 module development, including Mindphin-specific module conventions. It is
intended for internal documentation, developer onboarding, task completion
checks, and code review enforcement.

## Scope

These standards apply to all custom Odoo 19 modules developed or maintained by
the team. Reviewers should use this checklist before approving code for merge,
deployment, or client delivery.

## Mandatory Standards

- Every module must include a complete and accurate `__manifest__.py` file.
- Every custom model must have proper security access rights.
- Every custom model must have at least one required field.
- User-facing labels, menu names, button labels, and messages must be clear and
  consistently formatted.
- Python code must follow PEP 8 conventions.
- XML views must be clean, readable, and suitable for business users.
- Debug code, unused imports, commented-out code, and temporary test logic must
  be removed before review.
- Module upgrade and functional testing must be completed before approval.

## Mindphin Module Standards

Mindphin modules must follow the naming, branding, and translation standards in
this section in addition to the general Odoo standards in this document.

### Manifest Branding

Every Mindphin module manifest must use `mindphin` as the author and the Mindphin
website as the website value.

Required values:

- `author`: `mindphin`
- `website`: `www.mindphin.com`

Module display names must use clear Title Case:

```python
"name": "Module Name"
```

### Technical Module Naming

Technical module names must start with `md_`.
The module folder name must match the technical module name exactly.
Recommended format:

```text
md_module_name
```

Correct examples:

- `md_customer_management`
- `md_sale_extension`
- `md_inventory_report`

Incorrect examples:

- `customer_management`
- `mindphin_customer_management`
- `md customer management`

### Technical Field Naming

Custom technical field names must start with `md_`.
Recommended format:

```text
md_field_name
```

Correct examples:

```python
md_customer_code = fields.Char(string="Customer Code")
md_credit_limit = fields.Float(string="Credit Limit")
md_approval_user_id = fields.Many2one(
    "res.users",
    string="Approval User",
)
```

Do not rename standard Odoo fields or common framework fields with the `md_`
prefix. Standard fields must remain unchanged.

Standard field examples that must not be renamed:

- `name`
- `active`
- `sequence`
- `company_id`
- `user_id`
- `state`
- `create_uid`
- `create_date`
- `write_uid`
- `write_date`

Correct example:

```python
sequence = fields.Integer(default=10)
name = fields.Char(string="Name", required=True)
active = fields.Boolean(default=True)
md_customer_code = fields.Char(string="Customer Code")
```

Incorrect example:

```python
md_sequence = fields.Integer(default=10)
md_name = fields.Char(string="Name", required=True)
md_active = fields.Boolean(default=True)
```

### UI Label Naming

All visible UI labels must use the approved Mindphin label prefix where required
and proper Title Case. Do not expose technical names such as `md_field_name` in
the UI. This applies to field labels, action names, menu names, button labels,
page names, and other UI-visible strings.

Correct examples:

- `Label Name`
- `Customer Code`
- `Approval User`
- `Customer Profiles`
- `Confirm Request`

Incorrect examples:

- `label name`
- `customer code`
- `CUSTOMER CODE`
- `md_customer_code`
- `md Customer Code`

Standard Odoo labels such as `Name`, `Active`, and `Sequence` must remain
human-readable and must not be renamed to technical-looking labels.

### Repository and Folder Layout

Every Mindphin module must follow the standard Odoo module layout.

Required files and folders:

- `__init__.py`
- `__manifest__.py`
- `models/`, when Python models are present
- `views/`, when XML views are present
- `security/`, when models, groups, or rules are present
- `static/description/`, including app description assets

Repository hygiene rules:

- Do not commit `.zip` archives.
- Do not commit `.env` files, credentials, API keys, or secrets.
- Do not commit `__pycache__/` folders.
- Use either `wizard/` or `wizards/` within a module; do not mix both.
- Only include module-related changes in the commit.

### Model, View, and XML ID Naming

Mindphin model technical names, view technical names, and XML IDs must contain
`md`.

Correct examples:

```python
_name = "md.customer.profile"
```

```xml
<record id="md_customer_profile_action" model="ir.actions.act_window">
    <field name="name">Customer Profiles</field>
    <field name="res_model">md.customer.profile</field>
    <field name="view_mode">list,form</field>
</record>

<record id="md_customer_profile_view_form" model="ir.ui.view">
    <field name="name">md.customer.profile.view.form</field>
    <field name="model">md.customer.profile</field>
    <field name="arch" type="xml">
        <form>
            <sheet>
                <group>
                    <field name="name"/>
                    <field name="md_customer_code"/>
                </group>
            </sheet>
        </form>
    </field>
</record>
```

### Mindphin i18n Directory

Every Mindphin module must include an `i18n` directory with sample translation
files for the required languages.

Required files:

- `i18n/de_CH.po` for German Switzerland
- `i18n/fr_CH.po` for French Switzerland
- `i18n/it_IT.po` for Italian

Sample `.po` file structure:

```po
# Translation of Odoo Server.
# This file contains the translation of the following modules:
# * md_customer_management
#
msgid ""
msgstr ""
"Project-Id-Version: Odoo Server 19.0\n"
"Language: de_CH\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: \n"

#. module: md_customer_management
#: model:ir.model.fields,field_description:md_customer_management.field_md_customer_profile__md_customer_code
msgid "Customer Code"
msgstr ""
```

Translation export instructions:

1. Open Odoo in developer mode.
2. Go to `Settings > Translations > Import / Export > Export Translation`.
3. Select the Mindphin app or module in the `Apps To Export` field.
4. Select the required language, such as `German (CH) / de_CH`, `French (CH) / fr_CH`,
   or `Italian / it_IT`.
5. Select `PO File` as the file format.
6. Export the file and place it inside the module's `i18n` directory.
7. Confirm that the exported file is included in the module before review.

## Manifest File Standards

Every module must maintain a valid `__manifest__.py` file with relevant metadata.
For Mindphin modules, `OPL-1` is the standard license unless a different license
is explicitly approved.

Required checks:

- `name`
- `version`
- `author`
- `website`
- `category`
- `summary`
- `description`
- `license`
- `depends`
- `data`
- `demo`, if applicable
- `installable`
- `application`
- `auto_install`
- `assets`, if applicable
- `images`, if app branding is required

Manifest file rules:

- File starts with `# -*- coding: utf-8 -*-`.
- Version follows `19.0.x.y` or `19.0.x.y.z`.
- `summary` and `description` clearly describe the module functionality and are
  relative to the actual module scope.
- `depends` includes only modules the code actually uses.
- Asset paths use full module paths, such as `md_module/static/src/...`.
- Asset bundles are selected correctly, such as `web.assets_frontend` or
  `web.assets_backend`.
- `installable`, `application`, and `auto_install` are set explicitly.
- No leftover commented-out manifest entries.

Recommended data load order:

1. `security/`, including groups, `ir.model.access.csv`, and record rules
2. `data/`
3. `views/`
4. `reports/`
5. `wizard/` or `wizards/`
6. `views/menus.xml` last, when menus exist

Example:

```python
# -*- coding: utf-8 -*-

{
    "name": "Customer Management",
    "version": "19.0.1.0",
    "author": "mindphin",
    "website": "www.mindphin.com",
    "category": "Sales",
    "summary": "Manage customer information efficiently.",
    "description": "Provides customer profile management features.",
    "license": "OPL-1",
    "depends": ["base", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/md_customer_profile_views.xml",
        "views/menus.xml",
    ],
    "demo": [],
    "images": ["static/description/icon.png"],
    "installable": True,
    "application": False,
    "auto_install": False,
}
```

## Coding Standards

Python code must follow PEP 8 and Odoo development conventions.

Required checks:

- Every `.py` file starts with `# -*- coding: utf-8 -*-` and a blank line.
- Model file names must match the technical model name contained in the file.
  For example, an inherited model with `_inherit = "sale.order"` must be placed
  in `sale_order.py`.
- One Python model file should contain only one model.
- Use `snake_case` for variables, fields, and methods.
- Use `PascalCase` for Python class names.
- Use `MdSomething` class names for new Mindphin models.
- Keep import order as standard library, third-party, Odoo, then local/addon
  imports.
- Keep line length reasonable, preferably around 88 to 100 characters.
- Use meaningful names for variables, methods, classes, and fields.
- Remove unused imports.
- Avoid duplicate code.
- Avoid commented-out code and temporary debug statements.
- Add docstrings only where they clarify non-obvious behavior.
- Use `ensure_one()` where appropriate.
- Use `sudo()` only when justified and documented by the business or technical
  need.
- Keep business constants in a top-level `const.py` when constants are shared or
  reused.
- Do not hardcode secrets, API keys, credentials, or instance names.
- If a standard Odoo method is overridden, add a concise comment explaining the
  reason for the override and the purpose of the custom logic in the overridden
  method.

Good example:

```python
# -*- coding: utf-8 -*-

from odoo import fields, models


class MdCustomerProfile(models.Model):
    _name = "customer.profile"
    _description = "Customer Profile"

    name = fields.Char(string="Name", required=True)

    def action_confirm(self):
        self.state = "confirmed"
```

Poor example:

```python
class customer(models.Model):
    _name='customer.profile'

    def Confirm(self):
        pass
```

## Model Standards

Common recommended fields:

```python
from odoo import fields, models


class CustomerProfile(models.Model):
    _name = "customer.profile"
    _description = "Customer Profile"
    _order = "sequence, name"

    sequence = fields.Integer(default=10)
    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(default=True)
    company_id = fields.Many2one(
        "res.company",
        string="Company",
        default=lambda self: self.env.company,
    )
```

Use `company_id` where multi-company behavior is relevant. Do not add
multi-company fields where the business process is clearly global and does not
require company-level isolation.

## Required Field Standard

Every custom model must include at least one required field.

Recommended default:

```python
name = fields.Char(
    string="Name",
    required=True,
)
```

## Field Label and String Standards

All field labels, button labels, menu names, and visible strings must use proper
Title Case.

Correct examples:

- `Name`
- `First Name`
- `Description`
- `Customer Reference`
- `Email Address`
- `Mobile Number`

Incorrect examples:

- `name`
- `first name`
- `FIRST NAME`
- `customer reference`

For Mindphin-specific UI labels, apply the approved label prefix where required
and keep the visible text in Title Case.

## XML and View Standards

Form views must:

- Group related fields logically.
- Use separators where needed.
- Use notebook pages for large forms.
- Keep the layout clean and readable.
- Show important operational fields in predictable positions.

List views must:

- Show only important fields.
- Avoid unnecessary columns.
- Include sequence handles for sortable records.
- Use proper default sorting where needed.

Search views must:

- Include commonly searched fields.
- Include useful filters.
- Include relevant group-by options.

Inherited view standards:

- Inherited view technical names must contain `_inh` or `_inherit`.
- Inherited view XML IDs should clearly indicate that the view is inherited.

Example:

```xml
<record id="md_sale_order_view_form_inherit" model="ir.ui.view">
    <field name="name">md.sale.order.view.form.inherit</field>
    <field name="model">sale.order</field>
    <field name="inherit_id" ref="sale.view_order_form"/>
    <field name="arch" type="xml">
        <xpath expr="//sheet" position="inside">
            <group string="Additional Information"/>
        </xpath>
    </field>
</record>
```

Example menu, action, and views:

```xml
<odoo>
    <record id="customer_profile_action" model="ir.actions.act_window">
        <field name="name">Customer Profiles</field>
        <field name="res_model">customer.profile</field>
        <field name="view_mode">list,form</field>
    </record>

    <record id="customer_profile_view_list" model="ir.ui.view">
        <field name="name">customer.profile.view.list</field>
        <field name="model">customer.profile</field>
        <field name="arch" type="xml">
            <list>
                <field name="sequence" widget="handle"/>
                <field name="name"/>
                <field name="email" widget="email"/>
                <field name="phone" widget="phone"/>
                <field name="active"/>
            </list>
        </field>
    </record>

    <record id="customer_profile_view_form" model="ir.ui.view">
        <field name="name">customer.profile.view.form</field>
        <field name="model">customer.profile</field>
        <field name="arch" type="xml">
            <form>
                <sheet>
                    <group>
                        <group>
                            <field name="name"/>
                            <field name="email" widget="email"/>
                            <field name="phone" widget="phone"/>
                            <field name="website" widget="url"/>
                        </group>
                        <group>
                            <field name="active" widget="boolean_toggle"/>
                            <field name="company_id"/>
                        </group>
                    </group>
                    <separator string="Notes"/>
                    <field name="note" colspan="2"/>
                </sheet>
            </form>
        </field>
    </record>

    <menuitem
        id="customer_profile_menu_root"
        name="Customer Management"
        sequence="10"
    />
    <menuitem
        id="customer_profile_menu"
        name="Customer Profiles"
        parent="customer_profile_menu_root"
        action="customer_profile_action"
        sequence="10"
    />
</odoo>
```

## Notes and Description Field Layout

Long text fields such as `note`, `description`, and `internal_remarks` must:

- Be placed under a separator.
- Use sufficient width.
- Use `colspan="2"` where applicable.

Example:

```xml
<separator string="Notes"/>
<field name="note" colspan="2"/>
```

## Active Field Placement

The `active` field should be displayed at the top-right side of the form view
when it is visible to users.

Recommended widget:

```xml
<field name="active" widget="boolean_toggle"/>
```

## Widget Usage

Use relevant widgets consistently for better user experience and data quality.

Examples:

```xml
<field name="image_1920" widget="image"/>
<field name="email" widget="email"/>
<field name="phone" widget="phone"/>
<field name="mobile" widget="phone"/>
<field name="website" widget="url"/>
<field name="user_id" widget="many2one_avatar_user"/>
```

Widget rules:

- Image fields must use image widgets.
- Email fields must use email widgets.
- Phone and mobile fields must use phone widgets.
- Website fields must use URL widgets.
- User-related Many2one fields should use avatar widgets where applicable.

## Sequence Field Handling

For sortable records:

- Add a `sequence` field in the model.
- Show it in list views using `widget="handle"`.
- Hide it in form views unless there is a clear business reason to display it.

Python example:

```python
sequence = fields.Integer(default=10)
```

XML list example:

```xml
<field name="sequence" widget="handle"/>
```

## Security Standards

Every model must have proper access rights.

Required checks:

- Add `security/ir.model.access.csv`.
- Access CSV IDs follow the pattern `access_md_<model>_<role>`.
- Custom groups are defined in `security/md_<module>_groups.xml` where roles are
  needed.
- Group labels use the approved Mindphin label prefix where required and remain
  in Title Case.
- Admin is auto-assigned to new security groups where the group is required for
  administration or module management.
- Define permissions based on user groups.
- Avoid giving full access unnecessarily.
- Add record rules where business data requires restriction.
- Confirm that access rules match the actual business process.
- Sensitive fields use `groups=` to restrict visibility where required.
- Public controllers use `auth='public'` only when necessary and must include
  token/access checks.
- Internal or payment-related routes use `sitemap=False` where appropriate.

Example `ir.model.access.csv`:

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_customer_profile_user,customer.profile.user,model_customer_profile,base.group_user,1,1,1,0
access_customer_profile_manager,customer.profile.manager,model_customer_profile,base.group_system,1,1,1,1
```

## JavaScript and Frontend Standards

For Odoo 19 frontend code:

- JavaScript files start with `/** @odoo-module **/`.
- Frontend public behavior uses the Odoo Interaction API and registry where
  applicable.
- Use Odoo 19 imports such as `_t` from `@web/core/l10n/translation`, `rpc` from
  `@web/core/network/rpc`, and browser utilities from `@web/core/browser/browser`.
- Translate user-facing JavaScript strings with `_t()`.
- Register assets under the correct manifest bundle.
- Place SCSS under `static/src/scss/` or CSS under `static/src/css/`.
- Confirm the browser console has no import, registry, or runtime errors.

## Static Description and App Branding

Mindphin modules published or visible in the Apps list should include:

- `static/description/icon.png`
- `static/description/index.html`
- Mindphin branding in the app title or slogan where required
- Optional Mindphin brand asset where used by sibling modules
- Manifest `images` entry referencing the app icon

The `index.html` should follow the style used by existing Mindphin modules,
including clear slogans, feature lists, and app description content.

## Documentation Standards

Non-trivial modules must include `README.md`.

README requirements:

- Title format: `# <Module Name>`
- Explain what the module does.
- Explain what the module does not do where scope could be confused.
- Include installation and configuration steps.
- Document relation to sibling Mindphin modules where relevant.

## Data and Demo Standards

- CSV and data files must be named clearly, such as `md.partner.zip.city.csv`.
- Data XML records must use stable XML IDs.
- Add sequences in `data/ir_sequence_data.xml` when auto-numbering is used.
- Keep sample/static files under `static/sample/`, not in the repository root.

## Hooks and Lifecycle Standards

- Use `post_init_hook` and `uninstall_hook` only when needed.
- Declare hooks in the manifest and implement them in `hooks.py`.
- Hook logic must be idempotent and safe on reinstall or upgrade.

## Cross-Module Consistency

- Do not duplicate functionality already provided by another `md_` module without
  a clear scope split.
- Depend on other `md_` modules only where there is a real dependency.
- Payment and integration modules must document which sibling module to use, such
  as redirect, iframe, or POS variants.

## Tracking and Chatter

Use chatter tracking for business-critical fields where auditability matters.

Example:

```python
state = fields.Selection(
    selection=[
        ("draft", "Draft"),
        ("confirmed", "Confirmed"),
    ],
    string="Status",
    default="draft",
    tracking=True,
)
```

Only add tracking where it has clear business value.

## Translation Readiness

All user-facing dynamic messages must be translatable.

Example:

```python
from odoo import _, fields, models
from odoo.exceptions import ValidationError


class CustomerProfile(models.Model):
    _name = "customer.profile"
    _description = "Customer Profile"

    email = fields.Char(string="Email Address")

    def action_validate_email(self):
        for record in self:
            if not record.email:
                raise ValidationError(_("Customer Email is required."))
```

Avoid hardcoded non-translatable validation messages, warnings, and dynamic
labels.

## Logging and Error Handling

Use proper validation and logging. Do not use `print()` for server-side logging.
Warnings caused by the custom module must be removed before merge for new
modules.

Logging example:

```python
import logging

from odoo import models


_logger = logging.getLogger(__name__)


class CustomerProfile(models.Model):
    _name = "customer.profile"
    _description = "Customer Profile"

    def action_create_customer(self):
        _logger.info("Customer profile creation started.")
```

Validation example:

```python
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class CustomerProfile(models.Model):
    _name = "customer.profile"
    _description = "Customer Profile"

    email = fields.Char(string="Email Address")

    @api.constrains("email")
    def _check_email(self):
        for record in self:
            if not record.email:
                raise ValidationError(_("Email is required."))
```

## Git Standards

Commit messages should follow a consistent format:

```text
[Purpose][Responsible Person] Message
```

Example:

```text
[IMP][Vivek] Improve Mindphin module checklist survey
```

Repository changes must stay scoped to the module being added or updated.

Recommended prefixes:

- `[ADD]` for new modules or features.
- `[FIX]` for bug fixes.
- `[IMP]` for improvements.
- `[REF]` for refactoring.
- `[REM]` for removals.

Commit examples:

- `[ADD][Vivek] Add customer profile module`
- `[FIX][Vivek] Fix customer email validation`
- `[IMP][Vivek] Improve sales order performance`
- `[REF][Vivek] Clean up customer profile code`

Branch examples:

- `feature/customer_profile`
- `fix/email_validation`
- `improvement/sales_order`

Repository hygiene checks:

- Only the module folder and directly related module files are changed.
- No unrelated edits are included.
- No duplicate `.zip` files, backup copies, generated files, `.env` files, or
  local artifacts are committed.
- Manifest version is bumped when updating an existing module.
- Commit message explains why the change is needed, not only which files changed.
- Commit message follows `[Purpose][Responsible Person] Message`.

## Code Review Checklist

Reviewers must verify:

- Manifest is complete and accurate.
- Manifest summary and description are present and describe the module
  functionality.
- Manifest targets Odoo 19 and uses `OPL-1`.
- Module folder and technical module name match.
- Standard Odoo module layout is present.
- Security access is configured.
- Access IDs, groups, and sensitive field restrictions are reviewed.
- Admin auto-assignment to new groups is reviewed where applicable.
- Python code follows PEP 8.
- Python headers, import order, model file naming, one-model-per-file rule, `Md`
  class names, override comments, secrets, and `sudo()` usage are reviewed.
- Required fields are present.
- Field strings use proper Title Case.
- Mindphin UI labels use the approved label prefix where required and Title Case.
- XML views are clean and readable.
- XML IDs, inherited view names, view inheritance, and no-core-override rules are
  checked.
- Widgets are applied correctly.
- Sequence behavior is handled where needed.
- Multi-company behavior is considered and tested where relevant.
- JavaScript and browser console are checked where applicable.
- Static description and README are checked where applicable.
- Data files, hooks, and cross-module consistency are checked where applicable.
- Translatable messages use `_()`.
- Required `i18n/de_CH.po`, `i18n/fr_CH.po`, and `i18n/it_IT.po` files are
  present.
- Logging is appropriate.
- Custom module warnings are removed from logs.
- Debug and commented-out code is removed.
- Module installs, upgrades, and uninstalls successfully, or an uninstall
  exception is documented.
- Functional testing is completed.
- Git diff is scoped and versioning is correct.
- Commit message format is correct.

## Final Review Checklist

- [ ] Manifest verified
- [ ] Manifest summary and description verified
- [ ] Odoo 19 version and `OPL-1` license verified
- [ ] Module folder and technical module name verified
- [ ] Standard module layout verified
- [ ] Security configured
- [ ] Security groups, access IDs, record rules, and sensitive fields reviewed
- [ ] Admin auto-assignment to new groups reviewed
- [ ] Views reviewed
- [ ] XML IDs and view inheritance reviewed
- [ ] Widgets applied
- [ ] Sequence handled
- [ ] Required fields added
- [ ] Multi-company tested where applicable
- [ ] Translation ready with `de_CH`, `fr_CH`, and `it_IT`
- [ ] PEP 8 compliant
- [ ] Python headers, import order, model file naming, one-model-per-file rule,
      override comments, `Md` class names, and `sudo()` usage reviewed
- [ ] Inherited view technical names include `_inh` or `_inherit`
- [ ] JavaScript/frontend checked where applicable
- [ ] Static description and README checked where applicable
- [ ] Data files, hooks, and cross-module consistency checked
- [ ] No warnings in logs
- [ ] No custom module warnings in logs
- [ ] Clean install successful
- [ ] Upgrade successful
- [ ] Uninstall successful or exception documented
- [ ] Functional testing completed
- [ ] Git diff scoped and version bumped where required
- [ ] Commit message follows `[Purpose][Responsible Person] Message`
- [ ] Code review approved

## Workflow Enforcement

This checklist should be included in:

- Internal developer onboarding.
- Code review process.
- Git merge request or pull request template.
- Task completion checklist.
- Team leader review process.
