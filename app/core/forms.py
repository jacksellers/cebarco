from django.forms import ModelForm, Textarea

from core.models import Message


class MessageForm(ModelForm):

    class Meta:
        model = Message
        fields = ('name', 'email', 'phone', 'subject', 'message')
        widgets = {
            'message': Textarea(),
        }
