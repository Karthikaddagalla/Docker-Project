from django.urls import path
from django.views.generic.edit import CreateView
import admissions.views as views
from django.contrib.auth.decorators import login_required


urlpatterns = [

    path("new_admissions/", views.new_admissions),
    path("total_admissions/", views.total_admissions),
    path("update/<int:id>", views.UpdateInformation),
    path("delete/<int:id>", views.DeleteInformation ),
    path("fee-paid/<int:id>", views.fee_paid)

]