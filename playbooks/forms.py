from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from .models import Playbook
import os



class PlaybookForm(BSModalModelForm):
    # def clean_file(self):
    #     file = self.cleaned_data.get("playbook", False)
    #     filetype = magic.from_buffer(file.read())
    #     if not "XML" in filetype:
    #         raise ValidationError("File is not XML.")
    #     return file

    class Meta:
        model = Playbook
        exclude = ('create_at',)

