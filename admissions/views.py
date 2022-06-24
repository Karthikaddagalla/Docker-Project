from django.shortcuts import render
from django.http import HttpResponse
from admissions.models import Students_info as Students

from admissions.forms import FormForStudents
from admissions.forms import NormalForms

from django.views.generic import View, DetailView, ListView, CreateView, UpdateView


# Create your views here.
values = {"college_name":"MNR Institute of College", "money": 40000}
#1st view for adding the new admissions


def homepage(request):   # These view is for homepage
    return render(request, "index.html", values)
    
#1st view for adding the new admissions


def new_admissions(request):
    # Here we will add the form for adding students
    form = FormForStudents
    values = {"college_name":"MNR Institute of College", "money": 40000, "admission_form":form}

    if request.method == "POST":              # If someone is pressions on submit button these will be true.
        form_filled = FormForStudents(request.POST)  # Now the form variable contains the information entered in form

        if form_filled.is_valid():                   # These will be true when user enters varchar in varchar field and so on.
            form_filled.save()

        return homepage(request)    # These will return the user to homepage.
        



    return render(request, "admissions/new_admission.html", values)

#2ns view for knowing the total no of admissions


def total_admissions(request):
# You need to all the opeartions inside the view and send the results as dictionary into template.

    results = Students.objects.all()  #  SQL equivalent = select * from admissions_students
    students_dict = {"all_students":results}
    return render(request, "admissions/total_admission.html", students_dict)


def UpdateInformation(request, id):
    stud = Students.objects.get(Roll_no = id)
    form = FormForStudents(instance=stud)    # Here we wrote instance of that student means new student will not created old student get updated
    values = {"college_name":"MNR Institute of College", "money": 40000, "student_form":form}

    if request.method == "POST":
        form = FormForStudents(request.POST, instance=stud)

        if form.is_valid():
            form.save()

            return homepage(request)

    return render(request, "admissions/updating_form.html", values)


def DeleteInformation(request, id):
    stud = Students.objects.get(id = id)
    stud.delete()

    return total_admissions(request)



def gooder(request):
    return HttpResponse("I am a gooder method")


def fee_paid(request, id):
    student = Students.objects.get(Roll_no = id)

    student.amount_fee_paid = 0
    student.save()

    return homepage(request)


