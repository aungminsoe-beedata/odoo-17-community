# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Installment Notifications",

    'summary': """
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "BEE",
    'website': "http://www.beedatamyanmar.com",

    'category': 'Installments Notifications',
    'depends': ['account'],
    'data': [
        # 'security/groups.xml',
        'security/ir.model.access.csv',
        'views/payments.xml',
        'data/crons.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
