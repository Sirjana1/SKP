from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from App1.models import Feedback, CustomerID, Item, Members

class SignupForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)



class LoginForm(forms.Form):
    username =  forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)



# for practice:

from django import forms
from .models import Book
from django.forms.models import (
    inlineformset_factory,
    modelform_factory,
    modelformset_factory
)

class BookForm(forms.ModelForm):
    class Meta:
        model: Book
        firlds = (
            'title',
            'number_of_pages'

        )




class Contact_form(forms.Form):
    name = forms.CharField(max_length= 50)
    contactNo = forms.CharField()
    emailID = forms.EmailField()
    registered_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date' }))







class CustomerIdForm(forms.ModelForm):
    
    class Meta:
        model = CustomerID
       # fields = ['firstName', 'lastName', 'citizenshipIDno', 'upload_photo','requestDate        ']
        fields = '__all__'


class addItemForm(forms.ModelForm):
    class Meta :
        model = Item
        fields = [
            'name',
            'total_quantity',
            'total_price'
        ]

class addSellItemForm(forms.ModelForm):
    class Meta :
        model = Item
        fields = [
            'name',
            'total_quantity',
            'total_price'
        ]
    quantity_sold = forms.IntegerField(min_value=1)
    price_per_item = forms.DecimalField(max_digits=10, decimal_places= 2)


class MembersForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = [
            'fname', 'lname', 'email', 'password', 'age'
        ]



from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email','feedback_type', 'comment']

