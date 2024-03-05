from django.urls import path
from . import views

urlpatterns = [
    path('prod1',views.prod1,name='prod1'),
    path('prod2',views.prod2,name='prod2'),
    
]
