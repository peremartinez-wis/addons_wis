# -*- coding: utf-8 -*-
# Copyright 2019 Pere Martínez <peremg@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Account Invoice Committed Date',
    'summary': 'This module adds Committed Date field to account_invoice model',
    'version': '12.0.0.1',
    'category': 'Account',
    'license': 'AGPL-3',
    'author': "Pere Martínez",
    'website': '',
    'depends': [
        'account',
    ],
    'data': [
        'views/account_invoice.xml',
    ],
    'installable': True,
}
