from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control', 'placehodler' : "Nom complet"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class' : 'form-control', 'placehodler' : "Adresse email"}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class' : 'form-control', 'placehodler' : "Message", 'rows' : 5}))
