from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from.models import Place
from .forms import NewPlaceForm
# Create your views here.

@login_required
def place_list(request):
    if request.method == 'POST':
        #This makes a form for the view
        form = NewPlaceForm(request.POST)
        place = form.save()
        if form.is_valid():
            place.save()
            return redirect('place_list')



    places = Place.objects.filter(visited=False)
    new_place_form= NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})
@login_required

def places_visited(request):
    visited = Place.objects.filter(visited = True)
    return render(request, 'travel_wishlist/visited.hmtl', {'visited':visited})
@login_required

def place_was_visited(request, place_pk ):
    if request.method ==  "POST":
        place = Place.objects.get(pk == place_pk)
        places_visited= True
        place.save()

    return redirect('place_list')
@login_required

def about(request):
    author = 'Dakota'
    About = 'A website that helps u find places that u want to go to'
    return render(request, 'travel_wishlist/about.html', {'author': author},{'About': About})


@login_required

def delete(request, place_pk, HttpResponseForbiddin=None):
    place= get_object_or_404(Place,pk =place_pk)
    if place.user == request.user:
        place.delete()
        return redirect('place_list')
    else:
        return HttpResponseForbiddin()
