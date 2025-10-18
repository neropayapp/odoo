from odoo import http
from odoo.http import request

class NeropayController(http.Controller):
    @http.route(['/payment/neropay/redirect'],type='http',auth='public',csrf=False,website=True)
    def redirect(self,**post):
        tx=request.env['payment.transaction'].sudo().browse(int(post.get('transaction_id')))
        return request.redirect(tx._create_neropay_payment())

    @http.route(['/payment/neropay/ipn'],type='http',auth='public',csrf=False)
    def ipn(self,**post):
        tx=request.env['payment.transaction'].sudo().search([('reference','=',post.get('identifier'))],limit=1)
        if tx:tx._handle_neropay_notification(post)
        return 'OK'

    @http.route(['/payment/neropay/success'],type='http',auth='public',website=True)
    def success(self,**kw):return request.render('payment.payment_result',{'status':'success'})
    @http.route(['/payment/neropay/cancel'],type='http',auth='public',website=True)
    def cancel(self,**kw):return request.render('payment.payment_result',{'status':'cancel'})
