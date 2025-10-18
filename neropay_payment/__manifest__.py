{
    'name': 'NeroPay Payment Gateway',
    'version': '17.0.1.0',
    'category': 'Accounting/Payment Acquirers',
    'summary': 'Accept online payments securely with NeroPay',
    'author': 'NeroPay, Stockport UK',
    'website': 'https://neropay.app',
    'license': 'LGPL-3',
    'support': 'support@neropay.app',
    'depends': ['payment'],
    'data': [
        'data/neropay_data.xml',
        'views/payment_neropay_templates.xml',
    ],
    'images': [
        'static/description/icon.png',
        'static/description/cover.png'
    ],
    'installable': True,
    'application': False,
    'maintainers': ['neropay'],
    'odoo_version': '16.0,17.0,18.0',
    'description': """
<h1>NeroPay Payment Gateway for Odoo 16, 17, and 18</h1>

<p>
NeroPay enables businesses to accept payments securely and easily in Odoo eCommerce, Website, and Invoicing.
Supports Live and Sandbox environments with instant IPN updates.
</p>

<ul>
  <li>Compatible with Odoo 16, 17, and 18</li>
  <li>Automatic validation via IPN</li>
  <li>Supports GBP, EUR, IDR currencies</li>
  <li>Easy setup with Public/Secret keys</li>
</ul>

<p>
<a href="mailto:support@neropay.app">support@neropay.app</a><br>
+44 333 049 4380<br>
Stockport, UK
</p>
"""
}

