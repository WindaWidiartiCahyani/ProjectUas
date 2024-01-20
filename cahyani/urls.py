from django.urls import path
from . import views


urlpatterns = [
    path('', views.cahyani_detail, name='cahyani_detail'),
    path('add/<product_id>', views.cahyani_add, name='cahyani_add'),
    path('remove/<product_id>', views.cahyani_remove, name='cahyani_remove'),


    
]