{
    'name': "HMS",
    'author': "Mohamed Abd-ElGani",
    'category': 'Management',
    'version': '17.0.0.1.0',
    'depends': ['base',
                'sale',
                'crm',
                ],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/base_menus.xml',
        'views/patient.xml',
        'views/department.xml',
        'views/doctor.xml',
        'wizard/add_log_wizard.xml',
        'views/sale_order.xml',
        'views/res_partner.xml',
    ],

}
