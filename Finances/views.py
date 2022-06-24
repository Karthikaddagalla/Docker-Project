from django.shortcuts import render
from django.http import HttpResponse
from Finances.forms import FeeForms 
from admissions.views import homepage
from admissions.models import Students_info as Students

values = {"college_name":"MNR Institute of College", "money": 40000}

# Create your views here.
def total_money(request):  
    return render(request, "Finances/total_amount.html", values)


def total_money_teachers(request): 
    return render(request, "Finances/total_money_teachers.html", values)

def students_fees(request):

    form = FeeForms
    values = {"fee_form": form, "fee_to_be_paid": "Not Known"}

    if request.method == "POST":              # If someone is pressions on submit button these will be true.
        form =  FeeForms(request.POST)

        if form.is_valid():                   # These will be true when user enters varchar in varchar field and so on.
            roll = form.cleaned_data["Roll_no"]
            date = form.cleaned_data["date_of_birth"]

            values["Roll_no"] = roll
            
            qs = Students.objects.filter(Roll_no__in = [roll])
            

            if len(qs) == 1:
                if qs[0].date_of_birth == date:
                    values["fee_to_be_paid"] = qs[0].amount_fee_paid
                    values["name"] = qs[0].name

                else:
                    values["fee_to_be_paid"] = "Not Found"

            else:
                values["fee_to_be_paid"] = "Not Found"


                


              
              # You can access the submitted information by form.cleaned_data[""]
            

        

    return render(request, "Finances/students_fees.html", values)


        
