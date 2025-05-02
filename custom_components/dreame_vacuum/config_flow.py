"""
Config flow for Dreame Vacuum integration
"""
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult
from .const import DOMAIN, CONF_IP, CONF_TOKEN
import voluptuous as vol

class DreameVacuumConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """
    Handle a config flow for Dreame Vacuum.
    """
    VERSION = 1

    async def async_step_user(self, user_input=None) -> FlowResult:
        """
        Handle the initial step where the user enters IP and token.
        """
        errors = {}
        if user_input is not None:
            # Optionally, validate the input here (e.g., try connecting)
            return self.async_create_entry(title=user_input[CONF_IP], data=user_input)

        data_schema = vol.Schema({
            vol.Required(CONF_IP): str,
            vol.Required(CONF_TOKEN): str,
        })
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
        ) 