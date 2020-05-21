# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2019 Wineissocial (http://www.wineissocial.com)

from openerp import api, models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.multi
    def toggle_wis_app(self):
        """ Inverse the value of the field ``active`` on the records in ``self``. """
        for record in self:
            record.wis_app = not record.wis_app

    wis_app = fields.Boolean(string="App WIS",
                             delaut=False)
