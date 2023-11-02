from django.shortcuts import render, redirect
from.models import Place
from .forms import NewPlaceForm
# Create your views here.
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
def about(request):
    author = 'Dakota'
    About = 'A website that helps u find places that u want to go to'
    return render(request, 'travel_wishlist/about.html', {'author': author},{'About': About})
