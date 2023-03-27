# -*- coding: utf-8 -*-
# from odoo import http


# class model_relations(http.Controller):
#     @http.route('/1_model_relations/1_model_relations', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/1_model_relations/1_model_relations/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('1_model_relations.listing', {
#             'root': '/1_model_relations/1_model_relations',
#             'objects': http.request.env['1_model_relations.1_model_relations'].search([]),
#         })

#     @http.route('/1_model_relations/1_model_relations/objects/<model("1_model_relations.1_model_relations"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('1_model_relations.object', {
#             'object': obj
#         })
