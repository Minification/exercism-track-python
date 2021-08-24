from __future__ import annotations

MINUTES_PER_DAY = 1440
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60

class Clock:
    def __init__(self, hour: int, minute: int) -> None:
        self.minutes = (hour * MINUTES_PER_HOUR + minute) % MINUTES_PER_DAY

    def __repr__(self) -> str:
        hour = self.minutes // MINUTES_PER_HOUR
        minute = self.minutes % MINUTES_PER_HOUR
        return f"{hour:02}:{minute:02}"

    def __eq__(self, other: Clock) -> bool:
        return self.minutes == other.minutes

    def __add__(self, minutes: int) -> Clock:
        return Clock(0, self.minutes + minutes)

    def __sub__(self, minutes: int) -> Clock:
        return Clock(0, self.minutes - minutes)

