from pyexpat.errors import messages
from django.shortcuts import render, render, redirect


# for signup and login
#...........................
from django import forms
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from App1.forms import SignupForm, Contact_form, CustomerIdForm, addItemForm, addSellItemForm, MembersForm, FeedbackForm
from .models import Members, BlogPost
from django.contrib import messages
from App1.models import Feedback
#...........................

from App1.middlewares import auth, guest


# Create your views here.

# @auth
def index(request):
    return render(request, 'index.html')

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST) 
        if form.is_valid():
            user = form.get_user()
            login(request, user)   
            print(f"User {user.username} logged in") 
            return redirect('index')
    
    else:
        initial_data = {
            'username': '',
            'email': '',
            'password': ''
        }
        form = AuthenticationForm(initial=initial_data)
        
    return render(request, 'login.html', {'form':form})
# @guest
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)    
            return redirect('login_view')
    
    else:
        initial_data = {
            'username': '',
            'email': '',
            'password1': '',
            'password2': ''
        }
        form = SignupForm(initial=initial_data)
    return render(request, 'signup.html', {'form':form})
def logout_view(request):
    logout(request)
    return redirect( 'login_view')


'''
def register_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid:
            user =form.save()
            login(request, user)

    else:
        form = SignupForm(request.POSt)
        return render(request, 'home.html', {'form':form})'''


def contact_form(request):
    if request.method == 'POST':
        form = Contact_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            contactID = form.cleaned_data['contactID']
            emailID = form.cleaned_data['emailID']
            registered_date = form.cleaned_data['registered_date']
            messages.success("message sent successfully")
            print(f"Message sent! \nNAme: {name} \ncontactID: {contactID} \nemailID : {emailID} \nregostered_date: {registered_date}")
            return render(request, 'contactform.html', {'messege':'messege sent successfully'})
    else:
        initial_data = {
            'name' : '',
            'contactID': '',
            'emailID': '',
            'registered_date': ''

        }
        
        form = Contact_form(initial= initial_data)
        print('forms errors', form.errors)
    return render(request, 'contact_form.html', {'form': form})
    



from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        fee = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback.html')  # Redirect to a thank you page or home page
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'fee': fee})




    


from django.shortcuts import render, redirect
from .forms import CustomerIdForm  # Ensure the form is imported correctly

def cu(request):
    if request.method == 'POST':
        form = CustomerIdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect after saving
    else:
        form = CustomerIdForm()  # Initialize form if not POST
    
    # Render the form regardless of the request method
    return render(request, 'customerIdForm.html', {'form': form})


from django.utils import timezone

from .models import Item
from django.shortcuts import HttpResponse

def inventory_view(request):
 
    items1 = Item.objects.all()
    items2 = Feedback.objects.all()

    context = {
        'items1': items1,
        'items2': items2
    }
    
    return render(request, 'inventory.html', context)


def add_item(request):
    if request.method == 'POST':
        form = addItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            price_per_item = form.cleaned_data['total_price']  # Assuming you have a 'price' field in the form
            item.total_price = form.cleaned_data['total_quantity'] * price_per_item
            item.last_added_date = timezone.now()
            item.save()
            return redirect('inventory')
    else:
        form = addItemForm()
    return render(request, 'add_item.html', {'form': form})

def sell_item(request):
    if request.method == 'POST':
        form = addSellItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity_sold = form.cleaned_data['quantity_sold']
            price_per_item = form.cleaned_data['price_per_item']

            try:
                item = Item.objects.get(name=name)
                if item.total_quantity >= quantity_sold:
                    item.total_quantity -= quantity_sold
                    item.total_price -= quantity_sold * price_per_item
                    item.save()
                else:
                    return HttpResponse('Not enough items in stock')
            except Item.DoesNotExist:
                return HttpResponse('Item does not exist')
            return redirect('inventory')
    else:
        form = addSellItemForm()
    return render(request, 'sell_item.html', {'form': form})




def members_view(request):
    all_members = Members.objects.all
    return render(request, 'members.html', {'all': all_members}) #context


def MembersForm_view(request):
    if request.method == 'POST':
        form = MembersForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, "Please fill correct value")
            return redirect('membersform')
        messages.success(request, "Form submitted successfully")
        return redirect('membersform')
    else:
        form = MembersForm()
    return render(request, 'membersForm.html', {'form':form})


def blog_post_detail(request, slug):
    post = BlogPost.objects.get(slug=slug)
    return render(request, 'post_detail.html', {'post': post})
