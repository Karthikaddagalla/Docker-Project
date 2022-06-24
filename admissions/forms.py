# import form class from django
from django import forms
from django.forms import TextInput, fields

# import Students from models.py
from admissions.models import Students_info as Students

# create a ModelForm
class FormForStudents(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Students
		fields = ['name', 'father_name', "class_name", "contact", "date_of_birth"]
		widgets = {
			
			"name":forms.TextInput(attrs={"placeholder":"Name", "class":"form-control", "style":"width:350px;margin:4px;margin-left:15px"}),
			"father_name": forms.TextInput(attrs={"placeholder":"Father Name", "class":"form-control", "style":"width:350px;margin:4px;margin-left:15px"}),
			"class_name": forms.NumberInput(attrs={"placeholder":"Class Name", "class":"form-control", "style":"width:350px;margin:4px;margin-left:15px"}),
			"contact": forms.TextInput(attrs={"placeholder":"Contact Details", "class":"form-control", "style":"width:350px;margin:4px;margin-left:15px"}),
			"date_of_birth": forms.DateInput(attrs={"type":"date","placeholder":"Contact Details", "class":"form-control", "style":"width:350px;margin:4px;margin-left:15px"})



		}
		


class NormalForms(forms.Form):
	name = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Name", "class":"form-control", "style":"width:350px;margin:4px;margin-left:15px"}), max_length=500)
	address = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Father Name", "class":"form-control", "style":"width:350px;margin:4px;margin-left:15px"}),max_length = 500)
	contact = forms.CharField(widget= forms.NumberInput(attrs={"placeholder":"Class Name", "class":"form-control", "style":"width:350px;margin:4px;margin-left:15px"}),max_length = 500)
	items = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Contact Details", "class":"form-control", "style":"width:350px;margin:4px;margin-left:15px"}),max_length=500)