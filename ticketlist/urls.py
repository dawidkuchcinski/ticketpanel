from django.conf.urls import url
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('',views.ticketindex,name='index'),
    #path('add-ticket/',views.addticketform,name='add-ticket'),
    #path('add/', views.addticketform, name='add-ticket'),
    path('<int:ticket_id>/', views.ticketdetails, name='ticket-detail'),
    path('deletedamage/', views.deletedamage, name="deletedamage"),
]
