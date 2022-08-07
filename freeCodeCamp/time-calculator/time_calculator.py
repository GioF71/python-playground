am_pm = ["AM", "PM"]
_dow = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

def _parse_start(start):
    period = start[len(start) - 2:len(start)]
    ndx = start.index(":")
    h = start[0:ndx]
    m = start[ndx + 1:ndx + 3]
    return (h, m, period)

def _start_to_minutes(start_tuple):
    h = int(start_tuple[0])
    m = int(start_tuple[1])
    period = 1 if start_tuple[2] == "PM" else 0
    return m + ((period * 12) * 60 + h * 60)

def _parse_duration(duration):
    ndx = duration.index(":")
    h = duration[0:ndx]
    m = duration[ndx + 1:len(duration)]
    return (h, m)

def _duration_to_minutes(duration_tuple):
    h = int(duration_tuple[0])
    m = int(duration_tuple[1])
    return m + (h * 60)

def _sum_times(start_minutes, duration_minutes):
    total_min = start_minutes + duration_minutes
    m = total_min % 60
    h = int(int((total_min - m) / 60) % 24)
    d = int((total_min - m - (h * 60)) / (60 * 24))
    return (d, h, m)

def add_time(start, duration):
    period = start[len(start) - 2:len(start)]
    ndx = start.index(":")
    h = start[0:ndx]
    m = start[ndx + 1:ndx + 3]

    return ""

print(_parse_start("12:15 AM"))
print(_start_to_minutes(_parse_start("12:15 AM")))
print(_parse_duration("24:05"))
print(_duration_to_minutes(_parse_duration("24:05")))
print(_sum_times(_start_to_minutes(_parse_start("12:15 AM")), _duration_to_minutes(_parse_duration("24:05"))))

print(_parse_start("6:15 PM"))
print(_start_to_minutes(_parse_start("6:15 PM")))
print(_parse_duration("466:02"))
print(_duration_to_minutes(_parse_duration("466:02")))
print(_sum_times(_start_to_minutes(_parse_start("6:15 PM")), _duration_to_minutes(_parse_duration("466:02"))))