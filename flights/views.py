from django.shortcuts import render

# Create your views here.
from .models import Flight, Airport, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()

    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    
    })


def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        #in the passenger table, add a new flight for the passenger with this pk
        passenger.flights.add(flight)

        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))