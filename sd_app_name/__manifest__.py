# -*- coding: utf-8 -*-
###############################################################################
#
# soludoo Mader
# Copyright (C) soludoo Mader(<https://www.soludoo.ch>).
#
###############################################################################

{
    'name': '(sd) App Name',
    'version': '19.0.1.0.0',
    'category': '',  # Provide category.
    'sequence': 1,
    'summary': 'Add a short module summary here',
    'description': 'Add the module description here',
    'website': 'https://www.soludoo.ch',
    'author': 'Soludoo',
    'license': 'OPL-1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/sd_default_data.xml',
    ],
    'installable': True,
    'application': False,
}
