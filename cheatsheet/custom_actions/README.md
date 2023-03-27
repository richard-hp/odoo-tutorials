# Custom Actions

Odoo actions by default offer a very rigid format.

They essentially provide multiple 'view_modes', and some ways of customising the layout of each mode.

the <tree> mode will allow you to see lists and tables of records, <form> allows basic CRUD operations, <kanban>, <calendar> etc provide some more specialised view_modes you can use.

Then the ir.actions.act_window action essentially allows you to switch between these views, and also provides some of the machinery to allow you to edit records, view lists of them and so forth.

What if we don't want to be limited to this structure?  What if we want to build a completely custom HTML template and view that instead?

## How does a traditional MVC framework do this

For this you would probably just create a new route, something like:

```
GET /dashboard
```

Then have your controller pull in the required data, and pass that to a custom HTML template for rendering on the frontend.

## How does Odoo do this

Remember that Odoo is actually an SPA / API type architecture.

So in order to build custom actions we have to extend the functionality of the SPA.

This is easy enough to do, the basic steps are:

1. Extend the base OWL component
2. Provide this with a custom HTML template
3. Register the action
4. Link a <menuitem> to your custom action
5. Update the manifest file

### 1 - Extend Component

The Odoo frontend is an OWL SPA, with some additional libraries that assist with tasks specific to interacting with the Odoo backend.

If you look in the following file:

```bash
static/src/dashboard.js
```

You will see we have created a Component.  There are some important points to note:

1. This comment must be at the top of the file.

```js
/** @odoo-module **/
```

You can omit this, but you then have to manually load this code as an Odoo module, it's not worth the effort.

2. Create a basic component

```js
const { Component } = owl;

class Dashboard extends Component {
  // Make sure this aligns with the t-name in the dashboard.xml file
  static template = "custom_actions.dashboard_template";
}
```

This is all you need to actually render something onto the screen.  You can of course add much more to a component, such as state, methods, API calls etc.

We just have to ensure that the template is set to whatever the template id is.  Odoo takes care of the rest for us (linking this together, loading the template etc.)

### 2 - Provide the template

If you check out the

```bash
static/src/dashboard.xml
```

file, you'll see the HTML template.  Since Odoo uses bootstrap, we can easily scaffold up HTML pages using standard bootstrap css classes.

Again, we must ensure the ID links back to what the Component is expecting.

### 3 - Register the action

You'll see this in the following file:

```bash
views/view.xml
```

we create the action like so:

```xml
<record model="ir.actions.client" id="custom_actions.dashboard_action">
  <field name="name">Dashboard</field>
  <field name="tag">custom_actions.dashboard_action_component</field>
</record>
```

The 'tag' field is important, that will try to match on what is in the js file when we register the component:

```js
registry.category("actions").add("custom_actions.dashboard_action_component", Dashboard);
```

Then as usual, the static template property in the component must match the template ID in the XML file:

```js
  static template = "custom_actions.dashboard_template";
```

```xml
  <t t-name="custom_actions.dashboard_template" owl="1">
```

### 4 - Link a menuitem

We can create the menuitem:

```xml
<menuitem name="Dashboard" id="custom_actions.dashboard" action="custom_actions.dashboard_action" parent="custom_actions.menu_root" sequence="1" />
```

in the 

```bash
views/menus.xml
```

file.  So notice how the action is linked against the id of the ir.actions.client record.  So when you click on that menu item, it will load that action, and then the JS framework knows to render the component.  The component then pulls out the XML template, and renders the HTML for us.

### 5 - Update the manifest

So checkout the 

```bash
__manifest__.py
```

file and notice how we added this section:

```py
  'assets': {
      'web.assets_backend': [
          'custom_actions/static/src/**/*',
      ]
  }
```

This is so Odoo knows to load our JS component into the asset pipeline for us.

You can now put whatever you want into the HTML and it will get rendered onto the screen.
