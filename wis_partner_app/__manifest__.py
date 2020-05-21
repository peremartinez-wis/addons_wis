# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2019 Wineissocial (http://www.wineissocial.com)

{
    "name": "WIS Partner App",
    'summary': "Adding a boolean smart-button to indicate if the partner has installed the app.",
    "version": "10.0.1.0.0",
    "author": "Wineissocial",
    "website": "https://www.wineissocial.com",
    "category": "Accounting",
    "license": "AGPL-3",
    "depends": [
        "account",
    ],
    "data": [
        "views/res_partner_view.xml",
    ],
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    'installable': True,
    'application': False,
}
