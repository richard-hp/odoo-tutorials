# -*- coding: utf-8 -*-
# from odoo import http


# class custom_actions(http.Controller):
#     @http.route('/1_custom_actions/1_custom_actions', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/1_custom_actions/1_custom_actions/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('1_custom_actions.listing', {
#             'root': '/1_custom_actions/1_custom_actions',
#             'objects': http.request.env['1_custom_actions.1_custom_actions'].search([]),
#         })

#     @http.route('/1_custom_actions/1_custom_actions/objects/<model("1_custom_actions.1_custom_actions"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('1_custom_actions.object', {
#             'object': obj
#         })
