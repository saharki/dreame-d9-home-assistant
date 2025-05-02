"""
Vacuum platform for Dreame Vacuum integration
"""
import logging
from homeassistant.components.vacuum import (
    VacuumEntity,
    SUPPORT_START,
    SUPPORT_STOP,
    SUPPORT_RETURN_HOME,
    SUPPORT_STATUS,
    SUPPORT_PAUSE,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import DiscoveryInfoType

from .const import DOMAIN, CONF_IP, CONF_TOKEN, SUPPORT_DREAME
from .dreame_api import DreameVacuumAPI

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    """
    Set up Dreame vacuum entity from a config entry.
    """
    ip = entry.data[CONF_IP]
    token = entry.data[CONF_TOKEN]
    api = DreameVacuumAPI(ip, token)
    entity = DreameVacuumEntity(api, name="Dreame Vacuum")
    async_add_entities([entity], update_before_add=True)

class DreameVacuumEntity(VacuumEntity):
    """
    Representation of a Dreame robot vacuum as a Home Assistant VacuumEntity.
    """
    def __init__(self, api: DreameVacuumAPI, name: str):
        self._api = api
        self._name = name
        self._is_on = False
        self._status = None

    @property
    def name(self):
        """Return the name of the vacuum."""
        return self._name

    @property
    def is_on(self):
        """Return True if vacuum is cleaning."""
        return self._is_on

    @property
    def supported_features(self):
        """Return the supported features."""
        return SUPPORT_DREAME

    async def async_start(self):
        await self._api.async_start()
        self._is_on = True
        await self.async_update_ha_state()

    async def async_stop(self, **kwargs):
        await self._api.async_stop()
        self._is_on = False
        await self.async_update_ha_state()

    async def async_return_to_base(self, **kwargs):
        await self._api.async_return_to_base()
        self._is_on = False
        await self.async_update_ha_state()

    async def async_update(self):
        """Fetch state from the vacuum."""
        status = await self._api.async_status()
        self._status = status
        # Example: set _is_on based on status
        self._is_on = getattr(status, "is_on", False) 