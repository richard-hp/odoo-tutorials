# -*- coding: utf-8 -*-
# from odoo import http


# class basic_form_layout(http.Controller):
#     @http.route('/1_basic_form_layout/1_basic_form_layout', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/1_basic_form_layout/1_basic_form_layout/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('1_basic_form_layout.listing', {
#             'root': '/1_basic_form_layout/1_basic_form_layout',
#             'objects': http.request.env['1_basic_form_layout.1_basic_form_layout'].search([]),
#         })

#     @http.route('/1_basic_form_layout/1_basic_form_layout/objects/<model("1_basic_form_layout.1_basic_form_layout"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('1_basic_form_layout.object', {
#             'object': obj
#         })
