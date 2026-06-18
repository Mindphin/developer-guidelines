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
- [ ] Manifest summary and description are present and describe the actual module functionality.
- [ ] No .zip archives, .env files, credentials, or __pycache__ folders are included.

Remarks:

```text

```

## Technical Names and UI Labels

- [ ] All custom technical field names use the sd_ prefix.
e.g. sd_first_name
     sd_birthdate
- [ ] Standard Odoo fields such as name, active, sequence, company_id, user_id, and state are kept unchanged.
- [ ] Soludoo-specific visible UI labels use the (sd) prefix and Title Case.
      e.g. (sd) First Name
           (sd) Birthdate
- [ ] Action names, menu names, button names, page names, and other visible labels are reviewed.
      e.g. (sd) Payrexx
           (sd) Legal Pages
- [ ] Class Name, Model technical names, view technical and names contain sd.
     -       e.g.sd_partner_list_view_inherit --> xml id
                SdResPartner  --> class name
                sd.legal.pages  --> Model name
- [ ] make sure all XML IDs contain sd_.
- [ ] make sure there are not any sing warning message on terminal side.

Remarks:

```text

```

## Translation and i18n

- [ ] User-facing dynamic messages are translation-ready using _().
- [ ] Translations were exported from Odoo using Settings > Translations > Import / Export > Export Translation.

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

## Git and Repository

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
