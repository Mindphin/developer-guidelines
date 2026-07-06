# Mindphin Developer Checklist

## Module Information

- [ ] Module display name:
- [ ] Technical module name starts with `md_`:
- [ ] Target Odoo version is 19.0:
- [ ] Developer name:
- [ ] Reviewer name:
- [ ] Requirement / task reference:

## Scope Confirmation

- [ ] Implementation matches the approved requirement.
- [ ] No unrelated features were added.
- [ ] No architecture decisions were introduced without approval.
- [ ] Dependencies are limited to modules actually used.
- [ ] Related Mindphin modules were checked to avoid duplicate functionality.

## Manifest

- [ ] `__manifest__.py` starts with `# -*- coding: utf-8 -*-`.
- [ ] `name` is clear Title Case.
- [ ] `version` follows `19.0.x.y` or `19.0.x.y.z`.
- [ ] `author` is `mindphin`.
- [ ] `website` is `www.mindphin.com`.
- [ ] `category`, `summary`, and `description` are accurate.
- [ ] `license` is `OPL-1`, unless another license was approved.
- [ ] `depends` includes only real dependencies.
- [ ] `data` load order is security, data, views, reports, wizard, menus last.
- [ ] `demo` is present, even when empty.
- [ ] `installable`, `application`, and `auto_install` are explicit.
- [ ] `images` references `static/description/icon.png` when app branding is used.
- [ ] No commented-out or temporary manifest entries remain.

## Module Structure

- [ ] Module folder name exactly matches the technical module name.
- [ ] Required files exist: `__init__.py`, `__manifest__.py`, `README.md`.
- [ ] `models/` exists when Python models are present.
- [ ] `views/` exists when XML views are present.
- [ ] `security/` exists when models, groups, or rules are present.
- [ ] `data/` exists when default data or sequences are present.
- [ ] `i18n/de_CH.po`, `i18n/fr_CH.po`, and `i18n/it_IT.po` exist.
- [ ] `static/description/icon.png` and `static/description/index.html` exist.
- [ ] Either `wizard/` or `wizards/` is used, not both.
- [ ] No `.zip`, `.env`, `__pycache__/`, `.DS_Store`, or generated files are included.

## Python and Models

- [ ] Every `.py` file starts with `# -*- coding: utf-8 -*-` and a blank line.
- [ ] One Python model file contains only one model.
- [ ] Model file names match the model or inherited Odoo model.
- [ ] New model class names use `MdSomething`.
- [ ] New model technical names contain `md`.
- [ ] Every custom model has at least one required field.
- [ ] Custom fields use the `md_` prefix.
- [ ] Standard fields such as `name`, `active`, `sequence`, `company_id`,
      `user_id`, and `state` are not renamed with `md_`.
- [ ] Field labels use clear Title Case.
- [ ] Import order is standard library, third-party, Odoo, local imports.
- [ ] Business constants are moved to `const.py` when shared or reused.
- [ ] Overridden standard methods include a concise reason comment.
- [ ] `sudo()` is avoided unless justified by the business need.
- [ ] User-facing dynamic messages use `_()`.
- [ ] Validation errors use `ValidationError` or `UserError` appropriately.
- [ ] No unused imports, debug code, print statements, or commented-out code remain.

## Security

- [ ] `security/ir.model.access.csv` exists for every custom model.
- [ ] Access CSV IDs follow `access_md_<model>_<role>`.
- [ ] Security groups are defined in `security/md_<module>_groups.xml` when needed.
- [ ] Group labels are clear Title Case.
- [ ] Admin auto-assignment is reviewed where module management requires it.
- [ ] Permissions are limited to the real business roles.
- [ ] Record rules are added when business data requires restriction.
- [ ] Sensitive fields use `groups=` when visibility must be restricted.

## XML and Views

- [ ] XML files are well formed and readable.
- [ ] XML IDs contain `md`.
- [ ] View technical names contain `md`.
- [ ] Inherited view XML IDs and names include `_inherit` or `_inh`.
- [ ] Form views group related fields logically.
- [ ] Long text fields are under separators and use enough width.
- [ ] `active` is placed near the top-right when visible.
- [ ] List views show only useful columns.
- [ ] Sortable models use `sequence` with `widget="handle"`.
- [ ] Search views include useful fields, filters, and group-by options.
- [ ] Menus and actions use clear Title Case labels.
- [ ] Menus load after their referenced actions and views.
- [ ] Widgets are used where relevant, such as email, phone, URL, image, or avatar.

## Data, Demo, and Sequences

- [ ] Default data XML/CSV files use clear names and stable XML IDs.
- [ ] `noupdate="1"` is used for seed data that should not overwrite user edits.
- [ ] Sequences are stored in `data/ir_sequence_data.xml` when auto-numbering is used.
- [ ] Demo data is included only when it is useful and explicitly approved.
- [ ] Sample/static files are placed under `static/sample/`, not the module root.

## Chatter, Logging, and Errors

- [ ] Chatter tracking is used only for fields with business audit value.
- [ ] Chatter behavior is tested after write operations.
- [ ] Logging uses `_logger`, not `print()`.
- [ ] Custom module warnings are reviewed and removed before delivery.
- [ ] Error messages are clear, actionable, and translatable.

## Frontend and Assets

- [ ] JavaScript files start with `/** @odoo-module **/` when JS is used.
- [ ] Odoo 19 frontend imports are used correctly.
- [ ] JavaScript user-facing strings use `_t()`.
- [ ] Assets are registered under the correct manifest bundle.
- [ ] SCSS/CSS files are placed under `static/src/scss/` or `static/src/css/`.
- [ ] Browser console has no import, registry, or runtime errors.

## Documentation and Translation

- [ ] `README.md` explains purpose, exclusions, installation, and configuration.
- [ ] Relation to sibling Mindphin modules is documented where relevant.
- [ ] Translation files exist for `de_CH`, `fr_CH`, and `it_IT`.
- [ ] Translation files are exported or updated after final UI strings are complete.
- [ ] Dynamic Python and JavaScript messages are translation-ready.

## Testing

- [ ] Module installs successfully on a clean database.
- [ ] Module upgrades successfully.
- [ ] Module uninstalls successfully, or an uninstall exception is documented.
- [ ] Security access is tested with each relevant role.
- [ ] Core business workflows are tested end to end.
- [ ] Chatter tracking is tested where enabled.
- [ ] Multi-company behavior is tested where relevant.
- [ ] Browser console is checked when frontend code is present.
- [ ] No custom module warnings appear in logs.

## Git and Submission

- [ ] Git diff is scoped to the module and directly related files.
- [ ] Manifest version is bumped when updating an existing module.
- [ ] Commit message follows `[Purpose][Responsible Person] Message`.
- [ ] Branch name follows the approved style, such as `feature/module_name`.
- [ ] This checklist is completed before review submission.
- [ ] Reviewer feedback is resolved or explicitly deferred.

## Reviewer Approval

- [ ] Manifest reviewed.
- [ ] Security reviewed.
- [ ] Models and business logic reviewed.
- [ ] Views and UX reviewed.
- [ ] Translation readiness reviewed.
- [ ] Install/upgrade/uninstall evidence reviewed.
- [ ] Functional testing evidence reviewed.
- [ ] Code review approved.
