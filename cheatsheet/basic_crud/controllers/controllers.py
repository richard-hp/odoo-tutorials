# -*- coding: utf-8 -*-
# from odoo import http


# class basic_crud(http.Controller):
#     @http.route('/1_basic_crud/1_basic_crud', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/1_basic_crud/1_basic_crud/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('1_basic_crud.listing', {
#             'root': '/1_basic_crud/1_basic_crud',
#             'objects': http.request.env['1_basic_crud.1_basic_crud'].search([]),
#         })

#     @http.route('/1_basic_crud/1_basic_crud/objects/<model("1_basic_crud.1_basic_crud"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('1_basic_crud.object', {
#             'object': obj
#         })
