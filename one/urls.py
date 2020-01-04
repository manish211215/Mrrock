from . import views
from . import models
from django.urls import path


urlpatterns = [
 
  
  path('LHD BASKET/',views.basket,name='Big_basket'),
  #this byme
  path('dashboard/',views.dashboard,name = 'Dashboard'),
  path('applicationsetup/',views.application_setup,name = 'Application-Setup'),
  path('neworder/',views.new_order,name = 'New-Order'),
  path('checkonlineorder/',views.check_online_order,name ='Check-Online-Order'),
  path('tracking/',views.tracking,name='Tracking'),
  path('reports/',views.reports,name='Reports'),
  path('counter/',views.counter,name='Counter'),
  

]