from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    """Form for the contact page."""
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'subject': forms.TextInput(attrs={'class': 'form-input'}),
            'message': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 5}),
        }
        labels = {
            'name': 'Your Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Your Message',
        }
