from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from datacenter.format_visitor import(
    format_duration, format_entering, 
    get_duration, is_visit_long
)


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    
    for visit in passcard_visits:
        if not visit.leaved_at:
            duration = get_duration(visit)
        else:
            duration = (visit.leaved_at - visit.entered_at).total_seconds()
        this_passcard_visits.append(
            {
                'entered_at': format_entering(visit),
                'duration': format_duration(duration),
                'is_strange': is_visit_long(visit)
            }
        )
    
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
