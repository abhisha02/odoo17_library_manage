{
    'name': 'Library Management',
    'version': '1.0',
    'category': 'Services',
    'summary': 'Manage library books and lending',
    'sequence': 10,
    'description': """
Library Management System
========================
Manage books, members, and lending operations in a library.
    """,
    'author': 'Abhisha',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'auto_install': False,
}