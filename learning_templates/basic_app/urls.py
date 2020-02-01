from django.urls import path
from basic_app import views

# template tagging - django look for that particular vairiable i.e. app_name
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name= 'other'),
]
