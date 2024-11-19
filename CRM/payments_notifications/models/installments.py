from datetime import date

from odoo.exceptions import UserError, ValidationError

from odoo import models, fields, api, _




class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'
    _description = 'Register Payment'
    bill = fields.Many2one(
        'account.move',
    )

    notification_bill = fields.Many2one(
        'account.notification'
    )

    def _create_payment_vals_from_wizard(self):
        res = super(AccountPaymentRegister, self)._create_payment_vals_from_wizard()
        self.notification_bill.paid = True
        return res

    @api.onchange('notification_bill')
    def _get_amount(self):
        if self.notification_bill:
            bill = self.notification_bill.id
            cash = self.env['account.notification'].search([('id', '=', bill)])
            self.amount = cash.amount


class AccountInvoiceInherit(models.Model):
    _inherit = 'account.move'

    notification_bill = fields.One2many(
        'account.notification',
        'notification'

    )
    channel = fields.Many2one(
        'mail.channel',
        domain=[('channel_type', '=', 'channel')],
    )
    installments_total = fields.Float(
        compute='_compute_installments',
    )
    remaining = fields.Float(
        compute='_compute_remaining'
    )

    def _compute_installments(self):
        for rec in self:
            total = 0
            cashes = self.env['account.notification'].search([('notification', '=', rec.id)])
            for cash in cashes:
                total = total + cash.amount
            rec.installments_total = total

    def _compute_remaining(self):
        for rec in self:
            remain = rec.amount_total - rec.installments_total
            rec.remaining = remain

    @api.onchange('channel')
    def _channels(self):
        bill = self._origin.id
        dates = self.env['account.notification'].search([('notification', '=', bill)])
        for data in dates:
            data.channel = self.channel

    @api.constrains('notification_bill')
    def _max_notification_bill(self):
        for rec in self:
            total = 0
            cashes = self.env['account.notification'].search([('notification', '=', self.id)])
            for cash in cashes:
                total = total + cash.amount
            if total > rec.amount_total:
                raise ValidationError('Installments Total is more than the invoice Total.')


class Notification(models.Model):
    _name = "account.notification"
    _description = "Account Installments And Notifications"

    name = fields.Char(
        string='Name',
        compute='_compute_name',
    )
    notification = fields.Many2one(
        comodel_name='account.move',
        ondelete="cascade"
    )
    date = fields.Datetime(
        required=True
    )
    paid = fields.Boolean()
    amount = fields.Float()
    channel = fields.Many2one('mail.channel')

    def _compute_name(self):
        for rec in self:
            rec.name = str(rec.date.strftime('%d-%m-%Y'))

    def installment_notification(self):
        dates = self.env['account.notification'].search([('date', '<=', date.today()), ('paid', '!=', True)])
        for data in dates:
            if data.channel:
                body = 'Please be informed that the (invoice/bill) ' + data.notification.name + ' has a due payment on date ' + data.date.strftime(
                    '%d-%m-%Y') + ' With the amount ' + str(data.amount)
                data.channel.message_post(body=body)
            
