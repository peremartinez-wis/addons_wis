# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2020 Wineissocial (http://www.wineissocial.com)

{
    'name': 'Sale Order Analytic Default',
    'summary': 'This module sets the partner analytic account into the sale order',
    'version': '12.0.0.1',
    'category': 'Analytic',
    'license': 'AGPL-3',
    'author': "Pere Martínez",
    'website': '',
    'depends': [
        'res_partner_analytic',
        'sale',
        'analytic',
    ],
    'data': [
    ],
    'installable': True,
}
