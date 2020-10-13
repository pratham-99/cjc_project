from django import forms
from django.core import validators

def marks_validator(m):
    if m%2 !=0:
        raise forms.ValidationError("Invalid marks")


class StudentForm(forms.Form):
    rn = forms.IntegerField(label='Enter Roll_no' ,validators=[validators.MinValueValidator(1),validators.MaxValueValidator(50)])
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter name'}))
    marks = forms.FloatField(validators=[marks_validator])
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    city = forms.CharField(required=False)

    def clean(self):
        all_data = super().clean()
        p1 = all_data['password1']
        p2 = all_data['password2']
        if p1!=p2:
            raise forms.ValidationError("password didn't matched !!")

'''
    def clean_marks(self):
        m = self.cleaned_data['marks']
        if m %2 !=0:
            raise forms.ValidationError('mmarks cant be odd !!')
        else:
            return m
'''