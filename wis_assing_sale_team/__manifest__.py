# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2020 Wineissocial (http://www.wineissocial.com)

{
    "name": "WIS Sale Order Sales Team",
    'summary': "Assign Sales Team depending on the Salesperson.",
    "version": "12.0.1.0.0",
    "author": "Wineissocial",
    "website": "https://www.wineissocial.com",
    "category": "Stock",
    "license": "AGPL-3",
    "depends": [
        "sale",
        "crm",
        "sales_team",
    ],
    "data": [
        "views/crm_team_view.xml",
    ],
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    'installable': True,
    'application': False,
}
