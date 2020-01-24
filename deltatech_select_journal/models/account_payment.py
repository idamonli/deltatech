# -*- coding: utf-8 -*-
# ©  2015-2020 Terrabit
# See README.rst file on addons root folder for license details

from odoo import api, models, _
from odoo.exceptions import UserError, ValidationError


class account_payment(models.Model):
    _inherit = "account.payment"

    @api.multi
    def post(self):
        """ Mostenire functie post pentru selectarea seriei.
        seria standard ar trebui dezactivata
        """
        
        for rec in self:
            if rec.partner_type == 'customer':
                if not rec.name and rec.payment_type != 'transfer':
                    if self.journal_id:
                        rec.name = self.journal_id.sequence_id.with_context(ir_sequence_date=rec.payment_date).next_by_id()
        return super(account_payment, self).post()