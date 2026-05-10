"""Compatibility exports for upstream EventUtils split.

The upstream project moved event helper types into ``event_utils.py``.  This
fork still keeps the implementations in ``user_manager.py`` to preserve the
local LLM-ban changes, but exposes the same module-level names so imports that
follow the upstream layout continue to work.
"""

from .exceptions import AtUserCountError
from .user_manager import AtNumberError, EventUtils

__all__ = ["AtNumberError", "AtUserCountError", "EventUtils"]
