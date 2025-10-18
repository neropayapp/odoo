from odoo import models, fields
import requests, hashlib, hmac

class PaymentAcquirerNeropay(models.Model):
    _inherit = 'payment.acquirer'
    provider = fields.Selection(selection_add=[('neropay', 'Neropay')])
    neropay_public_key = fields.Char(string='Public API Key')
    neropay_secret_key = fields.Char(string='Secret API Key')
    neropay_mode = fields.Selection([('sandbox','Sandbox'),('live','Live')], default='sandbox')

    def neropay_get_api_url(self):
        return 'https://eu.neropay.app/payment/initiate' if self.neropay_mode=='live' else 'https://eu.neropay.app/sandbox/payment/initiate'

class PaymentTransactionNeropay(models.Model):
    _inherit = 'payment.transaction'
    def _create_neropay_payment(self):
        acquirer=self.acquirer_id;base=self.get_base_url()
        payload={
            'public_key':acquirer.neropay_public_key,
            'identifier':self.reference,
            'currency':self.currency_id.name,
            'amount':self.amount,
            'details':self.reference,
            'ipn_url':f'{base}/payment/neropay/ipn',
            'success_url':f'{base}/payment/neropay/success',
            'cancel_url':f'{base}/payment/neropay/cancel',
            'customer_name':self.partner_id.name,
            'customer_email':self.partner_id.email,
            'customer_phone':self.partner_id.phone or '',
            'customer_address':self.partner_id.contact_address or '',
            'customer_shipping_method':'Delivery'
        }
        r=requests.post(acquirer.neropay_get_api_url(),data=payload,timeout=30)
        j=r.json()
        if j.get('success')=='ok':return j['url']
        raise ValueError(j.get('message'))
    def _handle_neropay_notification(self,data):
        acquirer=self.acquirer_id
        s=data.get('status');i=data.get('identifier');sg=data.get('signature');pd=data.get('data',{})
        ck=f"{pd.get('amount')}{i}";sk=acquirer.neropay_secret_key
        ms=hmac.new(sk.encode(),ck.encode(),hashlib.sha256).hexdigest().upper()
        if s=='success' and sg==ms and i==self.reference:self._set_done()
        else:self._set_error('Invalid signature')
