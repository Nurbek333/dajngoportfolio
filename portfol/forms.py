from django.forms import ModelForm
from .models import Contact
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name","email","phone_number","description"]



class ArticleForm(forms.Form):
    description = forms.CharField(
    widget=forms.Textarea(attrs={'placeholder': 'Maqola matnini kiriting'}))
    image = forms.ImageField()

class JamoaForm(forms.Form):
    description = forms.CharField(
    widget=forms.Textarea(attrs={'placeholder': 'Maqola matnini kiriting'}))
    image = forms.ImageField()