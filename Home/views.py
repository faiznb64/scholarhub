from django.shortcuts import render
from django.http import HttpResponse
from . models import Subject, Mentor
from . forms import BookingForm

def index(request):
    numbers={
        'fruits':['banana','apple','grapes']
    }
    return render(request, 'index.html', numbers)

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == "POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request, 'booking.html',dict_form)

def mentor(request):
    dict_men={
        'mentor':Mentor.objects.all()
    }
    return render(request, 'mentor.html',dict_men)

def contact(request):
    return render(request, 'contact.html')

def subject(request):
    dict_sub={
        'sub':Subject.objects.all()
    }
    return render(request, 'subject.html',dict_sub)

