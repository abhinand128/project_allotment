from django import forms
from .models import Student, Course

class LoginForm(forms.Form):
    stud_adm_no = forms.CharField(max_length=50, label="Admission Number")
    dob = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))


class CourseSelectionForm(forms.Form):
    pathway = forms.ChoiceField(choices=[], label="Pathway")
    ds1 = forms.ChoiceField(choices=[], label="DS1")
    ds2 = forms.ChoiceField(choices=[], label="DS2")
    ds3 = forms.ChoiceField(choices=[], label="DS3")
    mdc = forms.ChoiceField(choices=[], label="MDC")
