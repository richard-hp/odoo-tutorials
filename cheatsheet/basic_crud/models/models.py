# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Category(models.Model):
  _name = 'basic_crud.category'
  _description = 'Each plant lives inside a category'

  name = fields.Char()
