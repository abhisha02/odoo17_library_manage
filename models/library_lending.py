from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryLending(models.Model):
    _name = 'library.lending'
    _description = 'Library Lending'
    _order = 'date desc'

    book_id = fields.Many2one('library.book', string='Book', required=True)
    member_id = fields.Many2one('library.member', string='Member', required=True)
    date = fields.Date(string='Borrowing Date', default=fields.Date.today)
    return_date = fields.Date('Return Date')
    expected_return_date = fields.Date('Expected Return Date', required=True)

    state = fields.Selection([
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue')
    ], default='borrowed', string='State')

    @api.model
    def create(self, vals):
        lending = super().create(vals)
        lending.book_id.write({
            'state': 'borrowed',
            'current_borrower_id': lending.member_id.id
        })
        return lending

    def return_book(self):
        self.ensure_one()
        self.write({
            'state': 'returned',
            'return_date': fields.Date.today()
        })
        self.book_id.write({
            'state': 'available',
            'current_borrower_id': False
        })
