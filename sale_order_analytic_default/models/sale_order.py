# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2020 Wineissocial (http://www.wineissocial.com)

from openerp import api, models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        """
        Update the following fields when the Partner is changed:
        """
        if self.partner_id:
            # See if the user_id team has the mark Override User Team
            self.analytic_account_id = self.partner_id.sale_account_analytic_id.id

        return
