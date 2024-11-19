# -*- coding: utf-8 -*-
{
    'name': "CF Website Customization",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Bee Data Myanmar",
    'website': "https://beedatamyanmar.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        
                'base',
                'website',
                'website_sale',
                'stock',
                'sale_management',
                'sale',
                'web',
                
                ],
    'data': [
        
        'views/templates.xml',
        'views/delivery_order_select.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'cf_website_customization/static/src/js/delivery_order_select.js',
        ],
    },
}

