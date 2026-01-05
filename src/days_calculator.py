import datetime
from typing import Literal

import holidays
import numpy as np

Inclusivity = Literal["left", "right", "both", "neither"]


def calculate_days_between(
    start_date: datetime.date,
    end_date: datetime.date,
    day_type: Literal["calendar", "business"] = "calendar",
    inclusive: Inclusivity = "neither",
) -> int:
    if day_type == "calendar":
        # by default, the timedelta is not inclusive to both sides
        num_days = end_date - start_date - datetime.timedelta(days=1)
        if inclusive == "left":
            num_days += datetime.timedelta(days=1)
        elif inclusive == "right":
            num_days += datetime.timedelta(days=1)
        elif inclusive == "both":
            num_days += datetime.timedelta(days=2)
        num_days = num_days.days
    elif day_type == "working":
        # get all holidays between the two dates
        start_year = start_date.year
        end_year = end_date.year
        all_holidays = {}
        for year in range(start_year, end_year + 1):
            holidays_for_year = holidays.Indonesia(years=year)
            all_holidays.update(holidays_for_year)

        # convert all holidays into an array of datetime
        all_holidays_arr = [np.datetime64(d) for d in list(all_holidays.keys())]

        # by default, np.busday is inclusive to start but exclusive to end
        # therefore, we need to add one day to start to make it exclusive
        start_date += datetime.timedelta(days=1)
        if inclusive == "left":
            start_date -= datetime.timedelta(days=1)
        elif inclusive == "right":
            end_date += datetime.timedelta(days=1)
        elif inclusive == "both":
            start_date -= datetime.timedelta(days=1)
            end_date += datetime.timedelta(days=1)
        num_days = np.busday_count(start_date, end_date, holidays=all_holidays_arr)
    else:
        raise Exception("day_type should be 'calendar' or 'working'")
    return num_days


def get_holidays_between(
    start_date: datetime.date,
    end_date: datetime.date,
    inclusive: Inclusivity = "neither",
):
    start_year = start_date.year
    end_year = end_date.year
    if inclusive == "left":
        start_date -= datetime.timedelta(days=1)
    elif inclusive == "right":
        end_date += datetime.timedelta(days=1)
    elif inclusive == "both":
        start_date -= datetime.timedelta(days=1)
        end_date += datetime.timedelta(days=1)
    all_holidays = {}
    for year in range(start_year, end_year + 1):
        holidays_for_year = holidays.Indonesia(years=year)
        all_holidays.update(holidays_for_year)
    holidays_between = {
        d.strftime("%d %b %Y"): name  # format in in human readable
        for d, name in all_holidays.items()
        if start_date < d < end_date
    }
    return holidays_between
