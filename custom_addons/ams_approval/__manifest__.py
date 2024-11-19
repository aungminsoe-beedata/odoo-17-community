# -*- coding: utf-8 -*-
{
    'name': "ams_approval",

    'summary': "Supply request create RFQ state in puchase order",

    'description': """
Long description of module's purpose
    """,

    'author': "Bee Data Myanmar",
    'website': "https://beedatamyanmar.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base',
                'base_setup',
                'purchase',
                'stock',],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        
        'views/purchase_receive_waiting.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
}

