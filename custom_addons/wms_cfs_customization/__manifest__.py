# -*- coding: utf-8 -*-
{
    'name': "Wms_cfs_ustomization",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
A Warehouse Management System (WMS) simplifies warehouse management by optimizing operations through data and automation. It offers real-time insights into inventory, shares data with ERP modules, and monitors productivity to identify improvement areas. Additionally, it provides step-by-step guidance for daily processes like receiving, picking, and packing orders.
    """,

    'author': "BEE DATA",
    'website': "https://www.beedatamyanmar.com",

 
    'category': 'Reduce stockouts, speed up operations, optimize routes and get real time visibility',
    'version': '0.1',
    'depends': ['base','sale_management','mail','stock','purchase','stock','account','web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/ir_sequence_data.xml',
        'views/menuitems.xml',
        
        'views/warehouse_form_view.xml',
        'views/warehouse_tree_view.xml',
        'views/warehouse_charge_form_view.xml',
        'views/warehouse_charge_tree_view.xml',
        
        # !charge notes warehouse
        'views/charge_note_form_view.xml',
        'views/charge_note_tree_view.xml',
        'views/wizard.xml',
        

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [           
            'wms_cfs_customization/static/src/**/*.scss',
        ]
    }
}

