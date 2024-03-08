from django.shortcuts import render
from .models import Club
from django.db.models import Q

def get_side_menu():
    return {
        'side_menu1': Club.objects.filter(club_type=1),
        'side_menu2': Club.objects.filter(club_type=2),
        'side_menu3': Club.objects.filter(club_type=3),
    }


def main_home(request):
    template_name = 'main.html'
    clubs = Club.objects.all()

    keyword = request.GET.get("keyword")
    if keyword:
        clubs = clubs.filter(Q(club_name__icontains=keyword))
    
    if request.GET.get('rank'):
        clubs = clubs.order_by('rank')
    else:
        clubs = clubs.order_by('?')

    context = {'club_list': clubs}
    context.update(get_side_menu())

    return render(request, template_name, context)


def main_type(request, club_type):
    template_name = f'club_list{club_type}.html'
    clubs = Club.objects.filter(club_type=club_type)

    keyword = request.GET.get("keyword")
    if keyword:
        clubs = clubs.filter(Q(club_name__icontains=keyword))

    context = {
        'club_list': clubs.order_by('club_name'),
        'club_type': club_type,
    }
    context.update(get_side_menu())

    return render(request, template_name, context)
