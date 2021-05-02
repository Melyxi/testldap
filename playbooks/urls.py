
from django.contrib import admin
from django.urls import path, include
import playbooks.views as playbook

app_name = 'playbooks'
urlpatterns = [
    path('', playbook.PlaybookListView.as_view(), name='book'),
    path('playbook_add/', playbook.PlaybookCreateView.as_view(), name='playbook_add'),
    #path('playbook_add/', playbook.playbook, name='playbook_add')
]

