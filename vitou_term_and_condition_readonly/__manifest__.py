# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2024-TODAY,
#    Author: REAM Vitou (reamvitou@yahoo.com)
#    Tel: +855 17 82 66 82


################################################################################
{
    'name': 'Terms and Condition Edit Protection',
    'version': '18.0.1.1.3',
    'category': 'Sale',
    'summary': 'This module, set readonly for terms and condition in sale',
    'description': 'This module, set readonly for terms and condition in sale',
    'author': 'V Technologies',
    'company': 'V Technologies',
    'maintainer': 'V Technologies',
    'website': 'https://apps.odoo.com/apps/modules/browse?search=vitou',
    # 'price':'30.0',
    # 'currency':'USD',
    'depends': ['sale'],
    'data': [

             'views/term_condition_readonly.xml'

             ],
    'images': ['static/description/banner.png'],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': False,
}
