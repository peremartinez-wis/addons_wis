# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2020 Wineissocial (http://www.wineissocial.com)

from openerp import api, models, fields
from datetime import datetime

class ResPartner(models.Model):
    _inherit = "res.partner"

    total_pending_payment_order_discount = fields.Monetary(compute='_compute_total_pending_payment_order_discount',
                                                  string="Girado con descuento",
                                                  default=0.0)
    """total_pending_payment_order_related = fields.Monetary(string="Total girado pendiente",
                                                          related="total_pending_payment_order",
                                                          store=True)"""

    def _compute_total_pending_payment_order_discount(self):

        user_currency_id = self.env.user.company_id.currency_id.id
        today = datetime.today().strftime('%Y-%m-%d')
        domain = [('partner_id', '=', self.id),
                  ('due_date', '>', today),
                  ]
        account_payment_line_objs = self.env['wis.payment.order.discount.line'].search(domain)

        total_discount = 0.0
        total_discount = sum(account_payment_line_objs.mapped('amount'))
        self.total_pending_payment_order_discount = total_discount

