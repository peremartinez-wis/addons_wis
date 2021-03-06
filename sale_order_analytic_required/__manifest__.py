# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2020 Wineissocial (http://www.wineissocial.com)

{
    'name': 'Sale Order Analytic Required',
    'summary': 'This module sets the analytic account field as mandatory in sale orders.',
    'version': '12.0.1.0',
    'category': 'Analytic',
    'license': 'AGPL-3',
    'author': "Pere Martínez",
    'website': '',
    'depends': [
        'sale',
        'analytic',
    ],
    'data': [
        'views/sale_order.xml',
    ],
    'installable': True,
}
