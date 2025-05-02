"""
Dreame API wrapper for python-miio
"""
import asyncio
from functools import partial
from miio import DreameVacuum

class DreameVacuumAPI:
    """
    Async wrapper for the python-miio DreameVacuum class.
    Provides async methods for controlling the vacuum.
    """
    def __init__(self, ip: str, token: str):
        self._vacuum = DreameVacuum(ip, token)

    async def async_start(self):
        """Start cleaning."""
        await asyncio.get_event_loop().run_in_executor(None, self._vacuum.start)

    async def async_stop(self):
        """Stop cleaning."""
        await asyncio.get_event_loop().run_in_executor(None, self._vacuum.stop)

    async def async_return_to_base(self):
        """Return to charging dock."""
        await asyncio.get_event_loop().run_in_executor(None, self._vacuum.home)

    async def async_status(self):
        """Get current status."""
        return await asyncio.get_event_loop().run_in_executor(None, self._vacuum.status) 