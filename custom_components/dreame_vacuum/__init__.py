"""
Dreame Vacuum integration for Home Assistant
"""
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.helpers import discovery

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

# Called when Home Assistant starts (not used for config entries)
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """
    Set up the Dreame Vacuum integration from yaml (not used, config flow only).
    """
    return True

# Called when a config entry is created/loaded
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """
    Set up Dreame Vacuum from a config entry (UI flow).
    Loads the vacuum platform dynamically.
    """
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "vacuum")
    )
    return True

# Called when a config entry is unloaded
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """
    Unload a config entry.
    """
    return await hass.config_entries.async_forward_entry_unload(entry, "vacuum") 