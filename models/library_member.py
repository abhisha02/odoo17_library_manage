from odoo import models, fields, api

class LibraryMember(models.Model):
    _name = 'library.member'
    _description = 'Library Member'

    name = fields.Char('Name', required=True)
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    member_code = fields.Char('Member Code', required=True)
    active = fields.Boolean(default=True)
    lending_ids = fields.One2many('library.lending', 'member_id', string='Borrowing History')
    borrowed_books_count = fields.Integer(compute='_compute_borrowed_books', string='Currently Borrowed Books')

    @api.depends('lending_ids.state')
    def _compute_borrowed_books(self):
        for member in self:
            member.borrowed_books_count = len(member.lending_ids.filtered(lambda l: l.state == 'borrowed'))
