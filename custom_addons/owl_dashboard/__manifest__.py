# -*- coding: utf-8 -*-
{
    'name': "owl_dashboard",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
 This module have finished Mon 18 11 2024
    """,

    'author': "Aung Min Soe ",
    'website': "https://www.sunacademy.developer.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web','sale','board'],

    # always loaded
    'data': [
       'views/sales_dashboard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'assets':{
      'webs.assets_backend':[
            'owl_dashboard/static/src/components/**/*.js',
            'owl_dashboard/static/src/components/**/*.xml',  
      ],  
    },
}

