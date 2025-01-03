from django import forms
from .models import *

class Menuform(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        
        
        labels = {
            'Item_name': "Item Name: ",
            'Item_prize' : " Item Prize:",
            
           
        }

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'contact', 'date', 'time', 'guests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
