# -*- coding: utf-8 -*-
# Copyright 2020 Pere Martínez <pere@wineissocial.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    sale_account_analytic_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Sale Analytic Account',
    )
    purchase_account_analytic_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Purchase Analytic Account',
    )
