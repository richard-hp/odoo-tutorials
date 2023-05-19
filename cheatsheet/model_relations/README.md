# Model Relations

Model relations will be things like, one-to-many, many-to-one etc.

Odoo can do most of this for you, including displaying linked records on the front end, managing database migrations etc.

## How does a traditional MVC framework do this

So let's say now we are allowing arbitrarily nested categories and sub-categories, and plants that can exist inside the categories.

This would allow heirarchies such as:

```
tree\fruit-tree\apple-tree
```

Normally to achieve this type of nesting, you'd need to do something along these lines:

1. Create some routes, like:

```
GET /category/:id/categories
GET /category/:id/plants
POST /category/:id/plant
etc.
```

So you can view all plants in a category, or add a plant to a category for example.

2. Wire these up to controller actions

As usual.  We'd also need to build filters that can pull out only plants in a specific category etc.

3. Build front-end templates

So we would require templates that can render the category, lists of plants within the category and so forth.

4. Implement the logic

So when someone adds a plant to a category, the controller would have to fetch the category, check it exists, add the plant record and so forth.


## How does Odoo do this

The basic steps are:

1. Create a new model, and define relations on them
2. Grant access to the new model in the security rules

Odoo will manage all the relations for you, provide forms for adding sub-categories, or adding plants to a category etc.

You will find the default views a bit messy, so it's worth while tidying them up a bit.

## Step by step guide

What follows here is an explanation of what changes have been made to the default Odoo module to achieve these steps.

### 1 - Create a new model

In the file

```bash
models/models.py
```

you will see I've created a new model for Plant.

```py
class Plant(models.Model):
  _name = 'model_relations.plant'
  _description = 'Each plant lives inside a category'

  name = fields.Char()
  category_id = fields.Many2one(comodel_name='model_relations.category', string='Category')

```

In terms of the relations, I've added both sides of the relation, so categories can have sub-categories, and plants can belong to a category.

### 2 - Grant Access

If you look in the 

```bash
security/ir.model.access.csv
```

file, you can see that a new security rule has been added.  You have to do this each time you add new models.

It's surprising how much functionality Odoo provides out of the box, just by adding a few lines of code we can create complex relations between data tables and easily view them on the frontend.
