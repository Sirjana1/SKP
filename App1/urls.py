
from django.urls import path
from .import views

urlpatterns = [
     path('', views.signup, name = 'signup'),
    path('index/', views.index, name='index'),
    path('login_view/', views.login_view, name='login_view'),
    path('signup/', views.signup, name='signup'),
    path('logout_view/', views.logout_view , name= 'logout_view'),
    path('contact_form/', views.contact_form, name = 'contact_form'),
    path('feedback_view/', views.feedback_view, name = 'feedback_view'),
    path('cu/', views.cu, name = 'customerID'),
    path('logout_view/', views.logout_view, name = 'logout'),
    path('add_item/', views.add_item, name='add_grocery_item'),
    path('sell_item/', views.sell_item, name='sell_grocery_item'),
    path('inventory_view/', views.inventory_view, name='inventory'),
    path('members_view/', views.members_view, name = 'members_view'),
    path('MembersForm_view/', views.MembersForm_view, name = 'membersform'),
    path('blog_post_detail/', views.blog_post_detail, name='blog_post_detail'),
    # path('item_list/', views.item_list, name='item_list'),
]



