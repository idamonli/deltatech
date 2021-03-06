# -*- coding: utf-8 -*-
# ©  2008-2019 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details

{
    "name": "MRP Planning",
    'version': '12.0.1.0.0',
    "author": "Terrabit, Dorin Hongu",
    "website": "https://www.terrabit.ro",
    "description": """
    
Functionalitati:
 - Calculeaza datele planificate pentru comanda de productie si pentru comenzile de lucru
 - Similar cu mrp_workorder


    """,

    "category": "Manufacturing",
    "depends": ["mrp"],

    "data": [
        "views/mrp_production_view.xml"
    ],
    "images": ['static/description/main_screenshot.png'],

    "installable": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
