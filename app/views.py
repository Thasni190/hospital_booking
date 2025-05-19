from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import Departments
from .models import Doctors


from .forms import BookingForm

# Create your views here.


def index(request):
    return render(request, 'hospital/index.html')

def about(request):
    return render(request, 'hospital/about.html')

def contact(request):
    return render(request, 'hospital/contact.html')


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'hospital/confirmation.html')  # Redirect after saving
    else:
        form = BookingForm()

    dict_from = {
        'form': form,
        'doctors': Doctors.objects.all()  # For manual rendering if needed
    }
    return render(request, 'hospital/booking.html', dict_from)

def doctors(request):
    dict_docs={
        'doctors':Doctors.objects.all()
    }
    return render(request, 'hospital/doctors.html',dict_docs)


def departments(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'hospital/departments.html', dict_dept)