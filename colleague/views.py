from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Gender, Classmate
from .forms import ClassmateForm
from django.views.generic import ListView, DetailView


# Create your views here.
def ClassmatesCreate(request):
    classmate_form = ClassmateForm()

    if request.method == "POST":
        classmate_form = ClassmateForm(request.POST)

        if classmate_form.is_valid():
            classmate = classmate_form.save(commit = False)

            is_male = request.POST.get("is_male", False)
            gender = Gender.objects.get(id = 1)

            if is_male == "on":
                Classmate.objects.create(first_name = classmate.first_name, last_name = classmate.last_name, age = classmate.age, email = classmate.email, phone_number = classmate.phone_number, address = classmate.address, gender = gender)
                messages.success(request, "Information input was recorded.")
                return redirect("Classmates List")

            is_female = request.POST.get("is_female", False)
            gender = Gender.objects.get(id = 2)
            if is_female == "on":
                Classmate.objects.create(first_name = classmate.first_name, last_name = classmate.last_name, age = classmate.age, email = classmate.email, phone_number = classmate.phone_number, address = classmate.address, gender = gender)
                messages.success(request, "Information input was recorded.")
                return redirect("Classmates List")

            is_other = request.POST.get("is_other", False)
            gender = Gender.objects.get(id = 3)
            if is_other == "on":
                Classmate.objects.create(first_name = classmate.first_name, last_name = classmate.last_name, age = classmate.age, email = classmate.email, phone_number = classmate.phone_number, address = classmate.address, gender = gender)
                messages.success(request, "Information input was recorded.")
                return redirect("Classmates List")
        
        else:
            messages.error(request, "Information input is not valid.")
            messages.error(request, classmate_form.errors) 
    
    else:
        classmate_form = ClassmateForm()
        
    context = {"classmate_form": classmate_form}
    return render(request, "create.html", context)

def ClassmatesList(request):
    classmates = Classmate.objects.all()

    context = {"classmates": classmates}
    return render(request, "list.html", context)

def ClassmatesDetails(request, id):
    classmates = Classmate.objects.filter(id = id)

    context = {"classmates": classmates}
    return render(request, "details.html", context)

def ClassmatesDelete(request, id):
    classmates = Classmate.objects.get(id = id)
    classmates.delete()

    messages.success(request, "Information input was vanished.")
    return redirect("Classmates List")

def ClassmatesEdit(request, id):
    classmates = Classmate.objects.get(id = id)

    if request.method == "POST":
        classmate_form = ClassmateForm(request.POST, request.FILES, instance = classmates)

        if classmate_form.is_valid():
            classmate = classmate_form.save(commit = False)

            is_male = request.POST.get("is_male", False)
            is_female = request.POST.get("is_female", False)
            is_other = request.POST.get("is_other", False)
            gender = None

            if is_male == "on":
                gender = Gender.objects.get(id = 1)

            elif is_female == "on":
                gender = Gender.objects.get(id = 2)

            elif is_other == "on":
                gender = Gender.objects.get(id = 3)

            if gender:
                classmate.first_name = request.POST.get("first_name")
                classmate.last_name = request.POST.get("last_name")
                classmate.age = request.POST.get("age")
                classmate.email = request.POST.get("email")
                classmate.phone_number = request.POST.get("phone_number")
                classmate.address = request.POST.get("address")
                classmate.gender = gender
                classmate.save()
                messages.success(request, "Information input was updated.")
                return redirect("Classmates List")

            else:
                messages.error(request, "Invalid gender selection.")

        else:
            messages.error(request, "Information input is not valid.")
            messages.error(request, classmate_form.errors)

    else:
        classmate_form = ClassmateForm(instance=classmates)

    context = {"classmate_form": classmate_form}
    return render(request, "edit.html", context)
