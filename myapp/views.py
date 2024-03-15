from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,BookingForm,RegisterForm
from .models import Doctor,Booking
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
# User auth start
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            user = authenticate(username=clean_data['username'],password=clean_data['password'])
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form = LoginForm()

    return render(request,'myapp/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request,'myapp/register.html',{'form':form})

# User auth end

# Page functions
def index(request):
    doctors = Doctor.objects.all()
    return render(request,'myapp/index.html',{'docs':doctors})

def doctors(request):
    doctors = Doctor.objects.all()
    return render(request,'myapp/doctors.html',{'docs':doctors},)

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    return render(request, 'myapp/doctor_detail.html', {'doctor': doctor})


def booking(request, id):
    doctor = Doctor.objects.get(pk=id)
    bookings = Booking.objects.filter(doctor=doctor.id)

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = BookingForm(request.POST)
            if form.is_valid():
                inpTime = form.cleaned_data['book_time']

                mybooking_time = Booking.objects.filter(book_time=inpTime, user=request.user)
                mybooking_doctor = mybooking_time.filter(doctor=doctor)

                if mybooking_time.exists() or mybooking_doctor.exists():
                    msg = 'You have a booking at this time with a doctor'
                    return render(request, 'myapp/booking.html', {'form': form, 'bookings': bookings, 'msg': msg,'doctor':doctor})
                else:
                    form.instance.doctor = doctor
                    form.instance.user = request.user
                    form.save()
                    msg = 'Booked successfully'
                    return render(request, 'myapp/booking.html', {'form': form, 'bookings': bookings, 'msg': msg,'doctor':doctor})
        else:
            return redirect('login')
    else:
        form = BookingForm()

    return render(request, 'myapp/booking.html', {'form': form, 'bookings': bookings,'doctor':doctor})

def num_user(request):
    user_count = User.objects.count()
    print("User Count:", user_count)
    return render(request, 'myapp/index.html', {'user_count': user_count})