from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
