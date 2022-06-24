from django.urls import path
import Finances.views as views


urlpatterns = [

    path("total_amount/", views.total_money),
    path("students_fees/", views.students_fees),
    path("total_money_teachers/", views.total_money_teachers),
    

]