# library_management/models/book.py
# -*- coding: utf-8 -*-

from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    # Campo para el título del libro
    name = fields.Char(string='Title', required=True)
    
    # Campo para el autor del libro
    author = fields.Char(string='Author', required=True)
    
    # Campo para la fecha de publicación del libro
    published_date = fields.Date(string='Published Date')
    
    # Campo para la descripción del libro
    description = fields.Text(string='Description')
