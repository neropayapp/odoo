{
    'name': 'Neropay Payment Acquirer',
    'version': '1.0',
    'category': 'Accounting/Payment Acquirers',
    'summary': 'Accept online payments securely with Neropay',
    'author': 'Neropay Ltd, Stockport UK',
    'website': 'https://neropay.app',
    'license': 'LGPL-3',
    'support': 'support@neropay.app',
    'depends': ['payment'],
    'data': [
        'data/neropay_data.xml',
        'views/payment_neropay_templates.xml',
    ],
    'installable': True,
    'application': False,
}
