# Basic Form Layout

As we saw in the model_relations project, the default layouts can be quite messy.

It does not take a lot of effort to tidy them up.

## How does a traditional MVC framework do this

You would not have this problem in a traditional MVC framework, because you would have built all the HTML templates yourself.  Unles your framework of choice has template scaffolding, in which case you may have to edit some HTML files to get it looking how you want to.

## How does Odoo do this

Odoo provides something called 'views'.  These are basically layout templates that the action will call upon in order to configure how things will be rendered on the frontend.  With the action 'ir.actions.act_window', it has something called a 'view_mode'.  This provides some buttons in the task bar that allows the user to swtich between the different 'view_modes'.  You can provide a template per mode to customise how this is displayed, and also construct your own view_modes (more on that later).

Here's what we will be doing:

1. Create a new view to override the default view
2. Link it back to the action so Odoo will use it

Everything is just linked with IDs

## Step by step guide

What follows here is an explanation of what changes have been made to the default Odoo module to achieve these steps.

### 1 - Create a view

In the file

```bash
views/views.xml
```

you will see I've created a new view.

```xml
  <record model="ir.ui.view" id="basic_form_layout.category_action_form_view">
    <field name="name">Categories</field>
    <field name="model">basic_form_layout.category</field>
    <field name="arch" type="xml">
      <form>
        <sheet>
          <notebook>
            <page string="Category">
              <group>
                <field name="name" />
                <field name="parent_id" />
              </group>

              <group>
                <field name="sub_category_ids" />
              </group>
            </page>

            <page string="Plants">
              <field name="plant_ids" />
            </page>
          </notebook>
        </sheet>
      </form>
    </field>
  </record>
```

This view inherits 'ir.ui.view'.  Again, this is a pre-built component within Odoo base that has the ability to be rendered by the action.

In the 'arch' section (i.e. architecture), I've grouped some items together, and forced other items to be rendered on a separate tab.

### 2 - Link it back

By providing the model attribute, and the <form> tag, Odoo will now know that when the action wants to render a form for that model, to use the template we have provided.

Odoo is very data driven, and has a lot of defaults.  So by simply providing some additional data in the form of an XML template, it will alter the way Odoo behaves and cause it to utilise what we have provided.

Odoo has some default view_modes availble for each action, such as 'list', 'form', 'calendar', 'kanban' etc.  For each one, you can optionally override the default view for it.  If you don't the default will be used.  As long as you match the tag to the view_mode, so for kanban you supply a <kanban> tag in the view arch etc.

It is possible to build your own view_modes as well, but that is a slightly more advanced topic.
