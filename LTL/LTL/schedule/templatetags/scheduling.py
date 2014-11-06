from datetime import datetime, timedelta
from django import template

register = template.Library()

from LTL.presenters import models as presenter_models


@register.assignment_tag
def get_available_time_slots():
    now = datetime.now()
    now = now - timedelta(minutes = 15 + (now.minute % 5), seconds = now.second, microseconds = now.microsecond )
    dummy_slots = [now + timedelta(minutes=(i*5)) for i in range(20)]
    return dummy_slots


@register.assignment_tag
def get_upcoming_talks():
    return (presenter_models.Talk.objects
        .filter(when__gte=datetime.now())[:5])
