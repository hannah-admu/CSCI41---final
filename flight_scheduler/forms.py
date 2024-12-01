from django import forms
from .models import Schedule, Flight

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['schedule_id', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default values
        self.fields['schedule_id'].initial = 'SCHD0000'
        self.fields['date'].initial = '2024-12-05'

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['flight_no', 'origin', 'duration', 'cost', 'schedule']  


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default values
        self.fields['flight_no'].initial = 'FL000'
        self.fields['origin'].initial = 'XXXXX'
        self.fields['duration'].initial = '00:00:00'
        self.fields['cost'].initial = '0.00'
        self.fields['schedule'].empty_label = "Select Schedule"

# Query form for schedules
class ScheduleQueryForm(forms.Form):
    schedule_id = forms.CharField(
        required=False,
        label="Schedule ID"
    )
    date = forms.DateField(
        required=False,
        label="Date",
        widget=forms.DateInput(attrs={'type': 'date'})
    )

# Query form for flights
class FlightQueryForm(forms.Form):
    flight_no = forms.CharField(
        required=False,
        label="Flight Number"
    )
    origin = forms.CharField(
        required=False,
        label="Origin"
    )
    duration = forms.DurationField(
        required=False,
        label="Duration"
    )
    cost = forms.DecimalField(
        required=False,
        label="Cost",
        max_digits=10,
        decimal_places=2
    )
    schedule = forms.ModelChoiceField(
        required=False,
        queryset=Schedule.objects.all(),
        label="Schedule"
    )
