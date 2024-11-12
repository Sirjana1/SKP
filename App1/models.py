from django.db import models
from django.utils.text import slugify
# # Create your models here.
# django dynamic forms:
# from django.conf import settings
# formset 
# forms.Form 
# models.Model 

# class Meta:
#     model = User
#     fields = []
# initial data 
# widget 
# extra field
# htmx.org
# matt Freire


# just for practice
class Author(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return self.name
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length= 59)
    number_of_pages = models.PositiveIntegerField(default =1)

    def __str__(self):
        return self.title
    

# models.py


class Feedback(models.Model):
    p = 'pr'
    n = 'ng'
    choices_type = [
        ('p', 'Positive'),
        ('n', 'Negative')
    ]

    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback_type = models.CharField(max_length=100, choices=choices_type, default = 'p')
    comment = models.TextField()

    def __str__(self):
        return self.name
    


class CustomerID(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length= 50)
    citizenshipIDNo = models. IntegerField()
    upload_photo = models.ImageField()
    requestDate = models.DateField()


    # def __str__(self):
    #     return self.name
    def __str__(self):
        return self.firstName

class Item(models.Model):
    name = models.CharField('Item Name',max_length= 100)
    total_quantity = models.PositiveIntegerField(default = 0)
    total_price = models.DecimalField(max_digits= 10, decimal_places=2, default= 0.00)
    last_added_date = models. DateTimeField(auto_now_add= True)
    # date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


    


class Members(models.Model):
    fname = models.CharField(max_length=100) 
    lname = models.CharField(max_length = 100)
    email = models. EmailField(max_length=200)
    password = models.CharField(max_length=300)
    age = models.IntegerField()

    def __str__(self):
        return self.fname + ' ' + self.lname
    


class BlogPost(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)




    
class BolckPostCreaterDetail(models.Model):
    title = models.ForeignKey(BlogPost, on_delete= models.CASCADE)
    fname = models.CharField(max_length= 100, verbose_name='First Name:', help_text=" * First Name Field Mandatory ")
    lname = models.CharField(max_length= 100, blank= True,  default= True)