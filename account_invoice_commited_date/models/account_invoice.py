# -*- coding: utf-8 -*-
# Copyright 2020 Pere Martínez <pere@wineissocial.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    date_committed = fields.Date(
        string='Committed Date'
    )

