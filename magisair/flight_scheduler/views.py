from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from .models import Schedule, Flight
from .forms import *

def view_schedule(request):
    # initialize forms
    schedule_form = ScheduleForm()
    flight_form = FlightForm()

    if request.method == 'POST':
        if 'create_schedule' in request.POST:  # check which form is submitted
            schedule_form = ScheduleForm(request.POST)
            if schedule_form.is_valid():
                schedule_form.save()
                return redirect('/flight_scheduler/view-schedule/')  
        elif 'create_flight' in request.POST:
            flight_form = FlightForm(request.POST)
            if flight_form.is_valid():
                flight_form.save()
                return redirect('/flight_scheduler/view-schedule/')  

    # query existing schedules and flights
    schedules = Schedule.objects.all()
    flights = Flight.objects.select_related('schedule').all()

    return render(request, 'flight_scheduler/schedule_list.html', {
        'schedules': schedules,
        'flights': flights,
        'schedule_form': schedule_form,
        'flight_form': flight_form,
    })

def schedule_queries(request):
    queries = Schedule.objects.all()
    form = ScheduleQueryForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        schedule_id = form.cleaned_data.get('schedule_id')
        date = form.cleaned_data.get('date')

        if schedule_id:
            queries = queries.filter(schedule_id__iexact=schedule_id)
        if date:
            queries = queries.filter(date__exact=date)

    return render(request, 'flight_scheduler/schedule_queries.html', {
        "form": form,
        "queries": queries,
    })


def flight_queries(request):
    queries = Flight.objects.select_related('schedule').all()
    form = FlightQueryForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        flight_no = form.cleaned_data.get('flight_no')
        origin = form.cleaned_data.get('origin')
        duration = form.cleaned_data.get('duration')
        cost = form.cleaned_data.get('cost')
        schedule = form.cleaned_data.get('schedule')

        if flight_no:
            queries = queries.filter(flight_no__iexact=flight_no)
        if origin:
            queries = queries.filter(origin__iexact=origin)
        if duration:
            queries = queries.filter(duration__exact=duration)
        if cost:
            queries = queries.filter(cost__exact=cost)
        if schedule:
            queries = queries.filter(schedule=schedule)

    return render(request, 'flight_scheduler/flight_queries.html', {
        "form": form,
        "queries": queries,
    })

# edit schedule
class ScheduleUpdateView(UpdateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'flight_scheduler/edit_schedule.html'

    def get_success_url(self):
        return reverse_lazy('flight_scheduler:homepage')

# edit flight 
class FlightUpdateView(UpdateView):
    model = Flight
    form_class = FlightForm
    template_name = 'flight_scheduler/edit_flight.html'

    def get_success_url(self):
        return reverse_lazy('flight_scheduler:homepage')  # redirect to the schedule list page after editing

from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Schedule, Flight

# delete schedule
class ScheduleDeleteView(DeleteView):
    model = Schedule
    template_name = 'flight_scheduler/confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('flight_scheduler:homepage')  


# delete flight
class FlightDeleteView(DeleteView):
    model = Flight
    template_name = 'flight_scheduler/confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('flight_scheduler:homepage')  