# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class MdAppRecord(models.Model):
    _name = "md.app.record"
    _description = "App Record"
    _order = "sequence, name"

    sequence = fields.Integer(
        default=10,
    )
    name = fields.Char(
        string="Name",
        required=True,
    )
    active = fields.Boolean(
        default=True,
    )
    company_id = fields.Many2one(
        "res.company",
        string="Company",
        default=lambda self: self.env.company,
    )
    md_code = fields.Char(
        string="Code",
    )
    md_note = fields.Text(
        string="Notes",
    )

    @api.constrains("md_code")
    def _check_md_code(self):
        for record in self:
            if record.md_code and " " in record.md_code:
                raise ValidationError(_("Code must not contain spaces."))
