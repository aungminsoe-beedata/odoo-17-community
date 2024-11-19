# -*- coding: utf-8 -*-
{
    'name': "Bee Data approval_customization 17",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1.17',

    # any module necessary for this one to work correctly
     'depends': [
        
                'base',
                'base_setup',
                'mail',
                'purchase',
                'approvals',
                'stock',
                'approvals_purchase',
                
                ],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/views.xml',
        'views/templates.xml',
        'data/sequence_data.xml',
        'views/menu_items.xml',
        
        'views/class_name.xml',
        'views/class_create_form_view.xml',
        'views/rfq_request_approve_button.xml',
        'views/stock_packing_view_ssr.xml',
        
        'views/approval_to_rfq.xml',
        'wizards/refused_wizard_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            # 'approval_customization/static/src/css/custom_styles.css',
            # 'approval_customization/static/src/js/custom_styles.js',
            # 'approval_customization/static/src/css/state_received.css',
        ],
    },

}

