import datetime
from django.utils.timezone import localtime


def get_duration(visit):
    moscow_time = localtime(visit.entered_at)
    now_time = localtime()
    time_in_vault = now_time - moscow_time
    seconds = time_in_vault.total_seconds()
    return seconds


def format_duration(duration):
    rounded_seconds = round(duration)
    rounded_time = datetime.timedelta(seconds=rounded_seconds)
    return rounded_time


def format_entering(visit):
    moscow_time = localtime(visit.entered_at)
    formated_moscow_time = moscow_time.strftime('%d %B %Y г. %H:%M')
    return formated_moscow_time


def is_visit_long(visit, minutes=60):
    if visit.leaved_at is not None:
        time_in_vault = (visit.leaved_at - visit.entered_at).total_seconds()
        return time_in_vault >= minutes*60
    else:
        time_in_vault = get_duration(visit)
        return time_in_vault >= minutes*60