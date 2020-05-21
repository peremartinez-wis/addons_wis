# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2019 Wineissocial (http://www.wineissocial.com)

from openerp import api, models, fields

class WisPaymentOrderDiscountLine(models.Model):
    _name = "wis.payment.order.discount.line"

    partner_id = fields.Many2one(comodel_name="res.partner",
                                 string="Cliente")
    origin_id = fields.Many2one(comodel_name="account.invoice",
                                string="Documento de origen",
                                help="Normalmente, la factura a la que hace referencia esta línea.")
    mandate_id = fields.Many2one(comodel_name="account.banking.mandate",
                                 string="Mandato de adeudo directo",
                                 help="Mandato relacionado.")
    due_date = fields.Date(string='Fecha de vencimiento',
                           help="Fecha de vencimiento")
    payment_date = fields.Date(string="Fecha de pago",
                       help="Fecha de pago.")
    amount = fields.Float(string="Importe",
                             help="Importe.")
    comments = fields.Text(string="Comentarios",
                           help="Comentarios.")
