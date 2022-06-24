from django import forms


class FeeForms(forms.Form):
	Roll_no = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Roll No", "class":"form-control", "style":"width:350px;margin:4px;margin-left:15px"}), max_length=500)
	date_of_birth = forms.DateField(widget= forms.TextInput(attrs={"type":"date","placeholder":"Date", "class":"form-control", "style":"width:350px;margin:4px;margin-left:15px"}))
	