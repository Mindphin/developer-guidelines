# -*- coding: utf-8 -*-

{
    "name": "App Name",
    "version": "19.0.1.0.0",
    "author": "mindphin",
    "website": "www.mindphin.com",
    "category": "Tools",
    "summary": "Describe the module purpose in one clear sentence.",
    "description": """
App Name

Describe what this module does, the business process it supports, and any
important scope exclusions.
""",
    "license": "OPL-1",
    "depends": ["base"],
    "data": [
        "security/md_app_name_groups.xml",
        "security/ir.model.access.csv",
        "data/md_app_name_data.xml",
        "views/md_app_record_views.xml",
        "views/menus.xml",
    ],
    "demo": [],
    "images": ["static/description/icon.png"],
    "installable": True,
    "application": False,
    "auto_install": False,
}
