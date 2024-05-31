# library_management/models/book.py
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author', required=True)
    published_date = fields.Date(string='Published Date')
    description = fields.Text(string='Description')

    @api.model
    def create_book(self, name, author, published_date, description):

        # Crear un nuevo libro
        book = self.create({
            'name': name,
            'author': author,
            'published_date': published_date,
            'description': description,
        })
        return book
    
    @api.model
    def update_book(self, book_id, name, author, published_date, description):
        
        # Actualizar un libro
        book = self.browse(book_id)
        book.name = name
        book.author = author
        book.published_date = published_date
        book.description = description
        return book
    
    @api.model
    def delete_book(self, book_id):

        # Eliminar un libro
        book = self.browse(book_id)
        book.unlink()
        return True