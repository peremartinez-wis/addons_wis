# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2019 Wineissocial (http://www.wineissocial.com)

{
    "name": "WIS Payment Order Discount",
    'summary': "Módulo para controlar los giros con descuento.",
    "version": "10.0.1.0.0",
    "author": "Wineissocial",
    "website": "https://www.wineissocial.com",
    "category": "Accounting",
    "license": "AGPL-3",
    "depends": [
        "account_credit_control",
        "account_banking_mandate",
    ],
    "data": [
        "views/wis_payment_order_discount_line_view.xml",
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
