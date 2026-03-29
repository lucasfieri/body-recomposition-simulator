"""Shared utility helpers."""

from datetime import date, timedelta

import pandas as pd


def safe_dates(start: date | None, end: date | None) -> tuple[date, date]:
    if start is None:
        start = date.today()
    if end is None:
        end = start + timedelta(days=90)
    if end <= start:
        end = start + timedelta(days=1)
    return start, end


def date_range(start: date, end: date) -> pd.DatetimeIndex:
    return pd.date_range(start=start, end=end, freq="D")
