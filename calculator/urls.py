from django.urls import path
from . import views

app_name = 'calculator'

urlpatterns = [
    path('', views.loan_calculator_view, name='loan_calculator'),
]