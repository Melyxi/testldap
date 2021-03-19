from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

from .forms import (

    PlaybookForm
)
from .models import Playbook

def playbook_add(request):
    pass

def playbook(request):
    return render(request, 'playbooks/playbook.html')

class PlaybookCreateView(BSModalCreateView):
    template_name = 'examples/create_playbook.html'
    form_class = PlaybookForm

    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('playbooks:book')

