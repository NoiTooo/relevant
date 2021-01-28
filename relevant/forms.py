from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from .models import Client, Adviser, Relevant, Post, Answer


User = get_user_model()


class RelevantForm(ModelForm):
    class Meta:
        model = Relevant
        fields = ['adviser', 'client']