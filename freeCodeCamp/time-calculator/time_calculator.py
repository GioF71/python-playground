am_pm = ["AM", "PM"]
_dow = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

def _start_to_minutes(start):
    return __start_tuple_to_minutes(__parse_start_to_tuple(start))

def _duration_to_minutes(duration):
    return __duration_tuple_to_minutes(__parse_duration_to_tuple(duration))

def __parse_start_to_tuple(start):
    period = start[len(start) - 2:len(start)]
    ndx = start.index(":")
    h = start[0:ndx]
    m = start[ndx + 1:ndx + 3]
    return (h, m, period)

def __start_tuple_to_minutes(start_tuple):
    period = 1 if start_tuple[2] == "PM" else 0
    hv = int(start_tuple[0]) 
    h = 0 if (period == 0 and hv == 12) else \
        12 if (period == 1 and hv == 12) else \
        hv + 12 if period == 1 else \
        hv
    h = 12 * period if (hv == 12) else \
        hv + (12 * period)
    m = int(start_tuple[1])
    return m + (h * 60)

def __parse_duration_to_tuple(duration):
    ndx = duration.index(":")
    h = duration[0:ndx]
    m = duration[ndx + 1:len(duration)]
    return (h, m)

def __duration_tuple_to_minutes(duration_tuple):
    h = int(duration_tuple[0])
    m = int(duration_tuple[1])
    return m + (h * 60)

def _sum_times(start_minutes, duration_minutes):
    total_min = start_minutes + duration_minutes
    m = total_min % 60
    h = int(int((total_min - m) / 60) % 24)
    d = int((total_min - m - (h * 60)) / (60 * 24))
    return (d, h, m)

def _get_minutes(sum_in_minutes):
    return sum_in_minutes % 60

def _get_hours(sum_in_minutes):
    return (int) (sum_in_minutes / 60) 

def _get_day_index(dayOfWeek):
    return _dow.index(dayOfWeek.lower())

def add_time(start, duration, dayOfWeek = None):
    sum_tuple = _sum_times(_start_to_minutes(start), _duration_to_minutes(duration))

    # decompose 
    h = sum_tuple[1]
    period = "PM" if h >= 12 else "AM"
    hourStr = 12 if h == 0 else str(h) if h <= 12 else str(h - 12)
    minStr = str(sum_tuple[2])     
    
    # base h:mm AM|PM covered
    result = "{}:{} {}".format(hourStr, minStr.rjust(2, '0'), period)

    # how many days more?
    day = sum_tuple[0]

    # day of week
    if dayOfWeek is not None:
        result_day = _dow[(_get_day_index(dayOfWeek) + day) % len(_dow)]
        result += ", {}".format(result_day.capitalize())

    # prepare days later
    days = sum_tuple[0]
    if (days > 0):
        day_cnt = " (next day)" if days == 1 else " ({} days later)".format(days)
        result += day_cnt

    return result
