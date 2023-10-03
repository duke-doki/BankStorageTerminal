from datacenter.models import Visit
from django.shortcuts import render
from datacenter.format_visitor import(
    format_duration, format_entering, 
    get_duration, is_visit_long
)


def storage_information_view(request):
    non_closed_visits = []
    visitors_not_left = Visit.objects.filter(leaved_at=None)
    
    for visitor in visitors_not_left:
        person_in_vault = visitor.passcard
        duration = get_duration(visitor)
        non_closed_visits.append(
            {
                'who_entered':person_in_vault.owner_name,
                'entered_at':format_entering(visitor),
                'duration':format_duration(duration),
                'is_strange': is_visit_long(visitor)
            }
        )

    context = {
        'non_closed_visits': non_closed_visits
    }
    return render(request, 'storage_information.html', context)

