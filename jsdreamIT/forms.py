from django import forms
from .models import Appointment,Contact, Contactus,Comment

class AppointmentForm(forms.ModelForm):
    
    class Meta:
        model = Appointment
        fields = ('name', 'email', 'department','time' )

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('name', 'email', 'department','message' )

class ContactusForm(forms.ModelForm):
        
    class Meta:
        model = Contactus

        fields = ('name', 'email', 'subject','message' )

class CommentForm(forms.ModelForm):
        
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body' )