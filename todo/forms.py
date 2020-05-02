from .models import Todo,Feedback
from django import forms


class TodoForm(forms.ModelForm):
    """Form definition for Todo."""

    class Meta:
        """Meta definition for Todoform."""

        model = Todo
        fields = ['title', 'details']
class FeebackForm(forms.ModelForm):
    """Form definition for feeback."""

    class Meta:
        """Meta definition for feebackform."""

        model = Feedback
        fields =[ 'email','feeds']
