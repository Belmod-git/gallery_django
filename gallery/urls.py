from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('login/',login,name='login'),
    path('add/',add,name='add'),
    path('show/<int:aid>',showinfo,name='show'),
    path('delete/<int:aid>',delete,name='delete')
]
