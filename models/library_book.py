from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char('Title', required=True)
    author = fields.Char('Author', required=True)
    isbn = fields.Char('ISBN', required=True, unique=True)
    category_id = fields.Many2one('library.book.category', string='Category')
    state = fields.Selection([
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('lost', 'Lost')
    ], default='available', string='Status')
    description = fields.Text('Description')
    current_borrower_id = fields.Many2one('library.member', string='Current Borrower')
    lending_ids = fields.One2many('library.lending', 'book_id', string='Lending History')

    @api.constrains('isbn')
    def _check_isbn(self):
        for book in self:
            if self.search_count([('isbn', '=', book.isbn), ('id', '!=', book.id)]) > 0:
                raise ValidationError('ISBN must be unique!')
