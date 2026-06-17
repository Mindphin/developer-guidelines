# Soludoo Odoo Module Developer Checklist

## Purpose

This checklist is intended to be completed by the developer and committed with the module changes. It replaces the long survey flow with a repository-friendly review artifact.

Leave an item unchecked if it is pending or not applicable, and add a short note in the relevant remarks section.

## Module Information

- Module Name:
- Technical Module Name:
- Developer:
- Reviewer:
- Review Date:
- Target Odoo Version: 19

## Manifest and Module Naming

- [ ] Manifest version follows Odoo 19 format, such as 19.0.x.y or 19.0.x.y.z.
- [ ] Manifest fields, minimal dependencies, data load order, assets, images, and explicit flags have been reviewed.
- [ ] Manifest summary and description are present and describe the actual module functionality.
- [ ] No .zip archives, .env files, credentials, or __pycache__ folders are included.

Remarks:

```text

```

## Technical Names and UI Labels

- [ ] All custom technical field names use the sd_ prefix.
- [ ] Standard Odoo fields such as name, active, sequence, company_id, user_id, and state are kept unchanged.
- [ ] Soludoo-specific visible UI labels use the (sd) prefix and Title Case.
- [ ] Action names, menu names, button names, page names, and other visible labels are reviewed.
- [ ] Model technical names, view technical names, and XML IDs contain sd.
- [ ] XML IDs are module-prefixed and descriptive.

Remarks:

```text

```

## Python and Model Standards

- [ ] Python code follows PEP 8 and project coding standards.
- [ ] Python files include coding headers and correct import order.
- [ ] Model file names match the technical model name contained in the file, for example `_inherit = "sale.order"` is placed in `sale_order.py`.
- [ ] One Python model file contains only one model, only helper models or line models with minimum logic can be included in same file.
- [ ] New Soludoo model class names use the Sd prefix.
- [ ] Overridden standard Odoo methods include a comment explaining the reason for the override and the purpose of the custom logic.

Remarks:

```text

```

## XML Views and Widgets

- [ ] Long text fields such as notes, description, or remarks are placed under a separator with sufficient width.
- [ ] Assets are registered in the correct bundle and SCSS/CSS files are placed under static/src/.
- [ ] Inherited view technical names contain `_inh` or `_inherit`.

Remarks:

```text

```

## Security

- [ ] security/ir.model.access.csv has been added or updated for all custom models.
- [ ] Custom groups are defined in security/sd_<module>_groups.xml where roles are needed.
- [ ] Soludoo group labels use the (sd) prefix.
- [ ] Admin is auto-assigned to new security groups where required for administration or module management.
- [ ] Permissions are assigned according to user groups without unnecessary full access.
- [ ] Record rules have been added where business data needs restriction.
- [ ] Sensitive fields use groups= where required.
- [ ] Public controllers use auth='public' only when needed, with token/access checks and sitemap=False where required.

Remarks:

```text

```

## Translation and i18n

- [ ] User-facing dynamic messages are translation-ready using _().
- [ ] Translations were exported from Odoo using Settings > Translations > Import / Export > Export Translation.

Remarks:

```text

```

## Static Description, Documentation, Data, and Lifecycle

- [ ] README.md is added for non-trivial modules and documents purpose, exclusions, installation, configuration, and related sibling modules.
- [ ] CSV/data files are clearly named and data XML records use stable XML IDs.
- [ ] Sample/static files are kept under static/sample/ instead of the repository root.
- [ ] Hooks are declared only when needed, implemented in hooks.py, and safe on reinstall or upgrade.
- [ ] Cross-module duplication has been checked and sibling sd_ dependencies are limited to real dependencies.

Remarks:

```text

```

## Logging, Cleanup, and Testing

- [ ] Proper logging or validation has been added where required.
- [ ] Unused imports have been removed.
- [ ] Debug code, print statements, and commented-out temporary code have been removed.
- [ ] Multi-company and multi-language behavior has been tested where the module claims support.

Remarks:

```text

```

## Git and Repository Hygiene

- [ ] Only the module folder and related module files are included.
- [ ] The manifest version has been bumped for updates to existing modules.
- [ ] The commit message explains why the change is needed.
- [ ] The commit message follows [Purpose][Responsible Person] Message, for example [IMP][Vivek] Improve module checklist.

Remarks:

```text

```

## Final Review Decision

### Developer Confirmation    

- [ ] I confirm that the checklist has been completed for this module.
- [ ] I confirm that some checklist items are pending and remarks have been added.

### Reviewer Decision

- [ ] Approved
- [ ] Approved with minor comments
- [ ] Changes required

Remarks:

```text

```

## Final Sign-Off

- [ ] Developer confirms this checklist is completed and committed with the module.
- [ ] Reviewer confirms this checklist has been reviewed against the actual code changes.

Developer Name:

Reviewer Name:

Date:
