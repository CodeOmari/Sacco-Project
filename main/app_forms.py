from django import forms

from main.models import Customer, Deposits

GENDER_CHOICES = {"Male": "Male", "Female": "Female"}
class CustomerForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'dob', 'weight', 'gender', 'profile_pic']
        widgets = {
            'dob' : forms.DateInput(attrs={'type': 'date', 'min':'1980-01-01', 'max':'2005-12-31'}),
            'weight': forms.NumberInput(attrs={'type': 'number', 'min':'35', 'max':'100'})
        }

class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposits
        fields = ['amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'type': 'number', 'min':'0', 'max':'100000'})
        }
