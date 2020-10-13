from django import forms
from .models import AllOrder


class StudentForm(forms.Form):
    rn = forms.IntegerField()
    name = forms.CharField()
    marks = forms.FloatField()


class CustomerForm(forms.Form):
    cname = forms.CharField()
    caddr = forms.CharField()
    cemail = forms.CharField()
    cphone = forms.IntegerField()

# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'         #for all fields to show
#         #fields = ('pname','pqty')  #For selected fields to show
#         #exclude = ['pseller']       #To exclude pericular fields


class AllOrderForm(forms.ModelForm):
    class Meta:
        model = AllOrder
        fields = '__all__'