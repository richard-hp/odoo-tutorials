# Odoo Cheat Sheet

The purpose of the cheatsheet is to give simple, minimal examples to demonstrate how to perform individual tasks within Odoo.

An explanation will also be given to relate it to other, more traditional MVC web frameworks such as node, django, ruby on rails, laravel etc.

## Odoo Architecture

It's important before you start doing Odoo development, to understand what Odoo actually is.

It is essentially a highly extensible MVC web framework.  It is very abstract and data driven, with most of the basic functionality would expect of a web framework already implemented for you.

So in order to achieve your goals, you will more often than not, be looking to *extend and customise existing Odoo functionality* rather than implementing it yourself.

This saves a lot of time so you are not constantly re-implementing the same things over and over.

The trade-off is, of course, you have to live within the confines of the Odoo way of doing things.  So without a clear understanding on that, you will find it difficult to acheive what you want to achieve.

## Odoo Base

What you get bundled with Odoo, already implemented and awaiting customisation is the following:

1. Database migrations
2. ORM
3. Relations between models (one-2-one, one-2-many, many-2-one etc.)
4. Basic CRUD forms, routes and database operations
5. A full Javascript SPA frontend
6. A full Python based backend
7. Powerful Templating engine
8. Bootstrap CSS framework
9. JS component / widget UI library
10. Plus a whole bunch of other stuff as well

This is all there before you even write your first line of code.

So when you want to start achieving certain tasks, you have to understand which parts of the existing functionality you will want to extend to make Odoo do what you want it to do.

### How do I guides

This section will provide sample modules for each question, showing the minimal example required to implement the required functionality.

This will start from simple tasks to progressively more complex ones.

Links will also be provided back to the official docs for more context and theory to explain, these are mainly just code samples you can use to see exactly how to achieve what you want, step by step.

1. [How do I perform basic CRUD actions?](./basic_crud)
2. [How do I build relations between mdoels](./model_relations)

