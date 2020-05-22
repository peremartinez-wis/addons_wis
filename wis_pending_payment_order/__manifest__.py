# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2019 Wineissocial (http://www.wineissocial.com)

{
    "name": "WIS Giros Pendientes",
    'summary': "Smartbutton que calcula los giros pendientes en el form de cliente.",
    "version": "12.0.1.0.0",
    "author": "Wineissocial",
    "website": "https://www.wineissocial.com",
    "category": "Accounting",
    "license": "AGPL-3",
    "depends": [
        "account_payment_order",
    ],
    "data": [
        "views/res_partner_view.xml",
        "security/ir.model.access.csv",
    ],
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    'installable': True,
    'application': False,
}
