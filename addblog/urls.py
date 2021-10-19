from django.urls import path
from . import views

urlpatterns = [
    path('addblg',views.addblog, name='addblg'),
    
] 