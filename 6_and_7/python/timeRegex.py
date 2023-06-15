import re


def minutesAfterMidnight(time_string):
    pattern = r'\b(?P<hour>\d{1,2})(?::(?P<minute>\d{2}))?(?P<period>am|pm)?\b'
    match = re.match(pattern, time_string)

    if match:
        hour = int(match.group('hour'))
        minute = int(match.group('minute')) if match.group('minute') else 0
        period = match.group('period')

        if hour > 23 or minute > 59:
            return None

        if period:
            if period.lower() == 'pm' and hour != 12:
                hour += 12
            if period.lower() == 'am' and hour == 12:
                hour = 0

        minutes = hour * 60 + minute
        return minutes

    return None
