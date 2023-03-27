# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Category(models.Model):
  _name = 'custom_actions.category'
  _description = 'Each plant lives inside a category'

  name = fields.Char()
  sub_category_ids = fields.One2many(comodel_name='custom_actions.category', string='Sub Categories', inverse_name='parent_id')
  parent_id = fields.Many2one(comodel_name='custom_actions.category', string='Parent Category')
  plant_ids = fields.One2many(comodel_name='custom_actions.plant', string='Plants', inverse_name='category_id')

class Plant(models.Model):
  _name = 'custom_actions.plant'
  _description = 'Each plant lives inside a category'

  name = fields.Char()
  category_id = fields.Many2one(comodel_name='custom_actions.category', string='Category')
