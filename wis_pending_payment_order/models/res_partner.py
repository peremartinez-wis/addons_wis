# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2020 Wineissocial (http://www.wineissocial.com)

from openerp import api, models, fields
from datetime import datetime


class ResPartner(models.Model):
    _inherit = "res.partner"

    total_pending_payment_order = fields.Monetary(compute='_compute_total_pending_payment_order',
                                                  string="Girado pendiente",
                                                  default=0.0)
    """total_pending_payment_order_related = fields.Monetary(string="Total girado pendiente",
                                                          related="total_pending_payment_order",
                                                          store=True)"""

    def _compute_total_pending_payment_order(self):

        user_currency_id = self.env.user.company_id.currency_id.id
        today = datetime.today().strftime('%Y-%m-%d')
        domain = [('partner_id', '=', self.id),
                  ('date', '>', today),
                  ]
        account_payment_line_objs = self.env['account.payment.line'].search(domain)

        total_pending = 0.0
        total_pending = sum(account_payment_line_objs.mapped('amount_company_currency'))
        self.total_pending_payment_order = total_pending

    def action_open_payment_lines(self):
        today = datetime.today().strftime('%Y-%m-%d')
        related_payment_lines = self.env['account.payment.line'].search(
            [('partner_id', '=', self.id), ('date', '>', today)])
        action = self.env.ref('contacts.action_contacts').read()[0]
        if len(related_payment_lines) > 1:
            # If we have more than one customer for this country we'll open the contacts tree view.
            action['domain'] = [('id', 'in', related_payment_lines.ids)]
        elif len(related_payment_lines) == 1:
            # If we would click on the smart button and create a contact from the tree it would automatically be filled
            # in with the current country thanks to its context.
            action['context'] = {'partner_id': self.id, }
            # If we have just one customer for this country we'll open the contacts form view directly.
            action['views'] = [(self.env.ref('account_payment_order.account_payment_line_form').id, 'form')]
            # Pass along the ID of the contact record for the action.
            action['res_id'] = related_payment_lines.ids[0]

        return action
