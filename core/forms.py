from django import forms
from .models import Ticket, Comment

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'name', 'email', 'priority']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3})
        }
