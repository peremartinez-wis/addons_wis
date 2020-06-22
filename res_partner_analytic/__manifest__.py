# -*- coding: utf-8 -*-
# Copyright 2019 Pere Martínez <peremg@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Res Partner Analytic',
    'summary': 'This module adds analytic account to res_partner model',
    'version': '12.0.0.1',
    'category': 'Analytic',
    'license': 'AGPL-3',
    'author': "Pere Martínez",
    'website': '',
    'depends': [
        'sale',
        'analytic',
    ],
    'data': [
        'views/res_partner_view.xml',
    ],
    'installable': True,
}
