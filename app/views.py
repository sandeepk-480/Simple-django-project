from django.shortcuts import render
from app.models import Student
from app.forms import StudentForm
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


def home(request):
    stu = Student.objects.all()
    return render(request, 'app/home.html', {'stu': stu})


def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Vehicle data Added")
            return redirect(reverse('home'))
    else:
        form = StudentForm()
    return render(request, 'app/add.html', {'form':form})


def update(request, pk):
    if request.method == 'POST':
        a = Student.objects.get(id=pk)
        b = StudentForm(request.POST, instance=a)
        if b.is_valid():
            b.save()
            messages.success(request, "Data Updated Successfully")
            return redirect(reverse('home'))
    else:
        a = Student.objects.get(id=pk)
        b = StudentForm(instance=a)
    return render(request, 'app/update.html', {'form':b, 'pk':pk})


def delete(request, pk):
    vehicle = Student.objects.get(id=pk)
    vehicle.delete()
    messages.success(request, "Vehicle data Deleted Successfully")
    return redirect(reverse('home'))