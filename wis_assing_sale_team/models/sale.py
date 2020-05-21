# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2020 Wineissocial (http://www.wineissocial.com)

from openerp import api, models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"


    @api.onchange('user_id')
    def onchange_user_id(self):
        """
        Update the following fields when the Salesperson is changed:
        """
        if self.user_id:
            # See if the user_id team has the mark Override User Team
            sales_team_obj = self.env['crm.team'].search([
                ('override_user_team', '=', 1),
                ('member_ids', '=', self.user_id.id),
            ])

            if sales_team_obj:

                # ensuring one
                sales_team_obj.ensure_one()

                self.update({
                    'team_id': sales_team_obj.id,
                })
            else:
                self.update({
                    'team_id': self.env['crm.team']._get_default_team_id(),
                })
        return
