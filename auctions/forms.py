from django import forms
from django.forms import ModelForm
from . models import AuctionListing, Komentar, User

class CommentForm(forms.ModelForm):
     class Meta:
        model = Komentar
        fields = ['komentar']
        labels = {
            'komentar' : "Add a comment:",
        }

class Bid(forms.ModelForm):
    class Meta:
        model = AuctionListing
        fields = ['cena']

        labels={
            'cena':"",
        }


class Endbid(forms.Form):
    endbid = forms.BooleanField()



class AuctionForm(ModelForm):
    class Meta:
        model = AuctionListing
        fields = ['naslov','opis','cena','kategorija','slika']
        widgets = {
            'naslov':forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Input your title here",}),
            'opis':forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Input your description here",}),

        }
        labels = {
            'naslov': "Title:",
            'opis': "Description:",
            'cena' :"Starting Price:",
            'slika':'Image:',
            'kategorija' :'Category:'
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        help_texts = {
            'username':""
        }
        widgets = {
            'username':forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Input your username here",}),
            'password':forms.TextInput(attrs={'type':'password','class': 'form-control', 'placeholder':"Input your password here",}),

         }

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email', 'password', 'password1']

        help_texts = {
            'username':""
        }
        widgets = {
            'username':forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Input your username here",}),
            'email':forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Input your emai; here",}),
            'password':forms.TextInput(attrs={'type':'password','class': 'form-control', 'placeholder':"Input your password here",}),
            'password1':forms.TextInput(attrs={'type':'password','class': 'form-control', 'placeholder':"Confirm your password here",}),

         }