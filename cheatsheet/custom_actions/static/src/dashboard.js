/** @odoo-module **/
import { registry } from "@web/core/registry";

const { Component } = owl;

class Dashboard extends Component {
  // Make sure this aligns with the t-name in the dashboard.xml file
  static template = "custom_actions.dashboard_template";

  setup() {
    console.log(`Dashboard loaded`)
  }
}

registry.category("actions").add("custom_actions.dashboard_action_component", Dashboard);
