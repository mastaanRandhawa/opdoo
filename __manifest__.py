{
    'name': 'CrioCo Theme',
    'version': '17.0.1.0.0',
    'category': 'Website/Theme',
    'summary': 'Premium artisan chocolate brand website theme',
    'author': 'CrioCo',
    'depends': [
        'website_sale',
        'auth_signup',
        'mass_mailing',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/product_categories.xml',
        'data/product_attributes.xml',
        'data/website_menu.xml',
        'views/layouts.xml',
        'views/pages.xml',
        'views/shop_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # Prepended so Bootstrap SCSS variable overrides compile correctly
            ('prepend', 'crioco_theme/static/src/scss/variables.scss'),
            'crioco_theme/static/src/scss/layout.scss',
            'crioco_theme/static/src/scss/home.scss',
            'crioco_theme/static/src/scss/shop.scss',
            'crioco_theme/static/src/js/main.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
