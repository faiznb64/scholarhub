from django import forms
from . models import Booking

class DateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'
        widgets={
            'booking_date':DateInput(),
            }
        labels={
            's_name':"Student Name :",
            's_phone':"Contact Number :",
            's_email':"Student Email :",
            'men_name':"Mentor Name :",
            'booking_date':"Booking Date :"
        }