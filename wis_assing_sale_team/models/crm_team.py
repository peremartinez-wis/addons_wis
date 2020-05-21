# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2020 Wineissocial (http://www.wineissocial.com)

from openerp import api, models, fields


class Team(models.Model):
    _inherit = "crm.team"

    override_user_team = fields.Boolean(string='Override User Team',
                               help="If checked, When you create a Sale Order, will override the computed user team "
                                    "with the team associated to the Salesperson field.")
