from django import forms
from todolist.models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class' : 'form-control',
                'style' : 'border-radius: 5px',
            }),
            'description': forms.Textarea(attrs={
                'class' : 'form-control',
                'style' : 'border-radius: 5px; resize: none',
                'rows' : '7',
            })
        }

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=200,
        required = True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
    )
    password1 = forms.CharField(
        required = True,
        label = "Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
    )

    password2 = forms.CharField(
        required = True,
        label = "Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
    )

    check = forms.BooleanField(
        label = "I Agree to the Terms of Use and Privacy Policy",
        required = True)

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]
