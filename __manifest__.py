{
    'name': 'Git Demo UCS',
    'version': '19.0.1.0.0',
    'category': 'Tools',
    'summary': 'Simple demo module for Git and Odoo practice',
    'description': '''
Git Demo UCS
============
A simple Odoo demo module for learning module structure and Git workflow.
''',
    'depends': ['base'],
    'data': [
        'views/git_demo_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
