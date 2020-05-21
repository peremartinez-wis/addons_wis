# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2019 Wineissocial (http://www.wineissocial.com)

from openerp import api, models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    wis_segment = fields.Selection([('A', 'A'),
                                    ('B', 'B'),
                                    ('C', 'C'),
                                    ('D', 'D'),
                                    ('E', 'E'),
                                    ('Z', 'Z'),
                                     ],
                                   string="Segmento",
                                   help="Segmentación WIS del cliente.")
    wis_customer_petition = fields.Text(string='Petición Cliente',
                               help="Introducir aquí la petición del cliente.")
    wis_answer = fields.Text(string='Rspuesta WIS',
                               help="Respuesta que da WIS a la petición del cliente.")
    wis_agreement = fields.Text(string='Acuerdo',
                               help="Acuewrdo al que se ha llegado con el cliente.")
    wis_cup_after_covid = fields.Boolean(string="¿Acepta hacer carta a copas post COVID?",help="Marcar esta opción si el cliente acepta hacer carta a copas después del COVID.")
    wis_next_visit = fields.Date(string="¿Cuándo le vamos a ver?",help="Fecha de la próxima visita.")
    wis_comments = fields.Text(string="Comentarios",help="Escribe aquí tus comentarios adicionales.")

