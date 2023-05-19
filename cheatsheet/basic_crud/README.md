# Basic CRUD

Odoo has this already out of the box.  Very little code needs to be written in order to achieve this.

You can of course customise it a great deal, but you can very quickly scaffold up basic CRUD forms.

## How does a traditional MVC framework do this

If you are thinking like a traditional MVC framework, you might think of it like a REST API, with a set pattern of routes for each model / resource you are managing.  For example, let's say we have a plant database, where each plant can be in a category.  You might do something like the following:

1. Create some routes, like:

```
GET /categories
POST /category
GET /category/:id
PUT /category/:id
DELETE /category/:id
```

2. Wire these up to controller actions

So the first route, to ```GET /categories``` you might write some code to fetch all the records out of the database and pass them to the view template.  You might even implement pagination etc.

3. Build front-end templates to render the index page, the create form, update form etc.

4. Implement the logic for this.  Here you put code in your controllers to validate the form, interact with the ORM, route users to different pages after the POST method is called etc.

## How does Odoo do this

None of this is actually necessary in Odoo.

This functionality is already built-in, and implemented in very generic classes that we can inherit and extend to customise to our needs.

The basic steps are:

1. Extend the base model, and define the fields we want.
2. Grant access to the model in the security rules 
3. Extend the base 'action'
4. Extend the menu and point it to the action
5. Configure the manifest file

That's it really.  You can think of the action as a highly configurable view of the model, that provides all of those routes and forms and everything I described above.

It is, in effect, implementing all the features you would expect of a resourceful routing, REST type HTTP interface.

Odoo scaffolds all the routes, forms, buttons, database migrations and operations etc, everything is there already implemented by default.

If you don't like how the default way has been done, it's easy enough to extend the base classes and override the default behaviour with what you want.

## Step by step guide

What follows here is an explanation of what changes have been made to the default Odoo module to achieve these steps.

### 1 - Extend the base model

In the file

```bash
models/models.py
```

you will see I've created a new class called 'Category' that extends the base model.  It has only one field, called 'name'.

```py
class Category(models.Model):
  _name = 'basic_crud.category'
  _description = 'Each plant lives inside a category'

  name = fields.Char()
```


We don't need to do any database migrations or anything else.  We can now read and write these values to the database.

### 2 - Enable security

If you look in the 

```bash
security/ir.model.access.csv
```

file, you can see that a security rule has been added allowing all users unrestricted access to this data model.

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_basic_crud_category,basic_crud.category,model_basic_crud_category,base.group_user,1,1,1,1
```

You can of course fine-tune this, and create user groups that can only read this model, etc. etc.

But how do we view this on the frontend, where do I write all my html templates?

### 3 - Extend the base action

The action essentially provides all the view templates, CRUD actions etc that you would want.

So we can have an index view, where each record is listed in a table and paginated, we get forms for creating new records, updating or deleting existing ones and so forth.

If you look in the 

```bash
views/views.xml
```

file you will see we have extended 'ir.actions.act_window'.  

```xml
  <record model="ir.actions.act_window" id="basic_crud.category_action">
    <field name="name">Categories</field>
    <field name="res_model">basic_crud.category</field>
    <field name="view_mode">tree,form</field>
  </record>
```

This is the base, abstract component that does all those things for us.  All we have to do is extend it, then fill in some basic parameters such as, which model we want it to be associated with, what text should appear and so forth.

In the 'view_mode' section, we have 'tree' which is basically a table / list of records, and 'form' which provides all the create, view and update forms.


### 4 - Extend the menu

So checkout the 

```bash
views/menus.xml
```

file.  By not supplying a parent property, this makes it the application root menu.  It will also cause it to appear in the main Odoo menu as well.

```xml
<menuitem name="Categories" id="basic_crud.main_menu" action="basic_crud.category_action"/>
```

So when you select this option from the main Odoo menu, it will point the user straight to the action specified.

Note how this is all configured by just supplying data to the templates.  So we have to make sure all the IDs match up.  I recommend developing a naming convention so that you don't have conflicts.

### 5 - Update the manifest file

I've made sure that all the view files and the security files are being loaded, and also set the 'application' property to True.  This will allow you to install the module as a new app.

You should be able install this module and see for yourself that you can create new categories, and view them in a list.
