"""Shared exception types for ReNeBan compatibility."""


class ReNeBanError(Exception):
    """Base exception for ReNeBan-specific errors."""


class PermanentRecordTimeError(ReNeBanError):
    """Raised when attempting to extend or shrink a permanent record."""


class AtUserCountError(ValueError):
    """Raised when a message contains too many non-bot At targets."""


class TimestrValueError(ValueError):
    """Raised when a time string cannot be parsed."""

    def __init__(self, invalid_timestr: str):
        self.invalid_timestr = invalid_timestr
        super().__init__(f"非法的时间字符串格式: {invalid_timestr!r}")


__all__ = [
    "AtUserCountError",
    "PermanentRecordTimeError",
    "ReNeBanError",
    "TimestrValueError",
]
