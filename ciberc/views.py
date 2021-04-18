# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, ListView
from django.shortcuts import render
from django.core import serializers

# Models
from ciberc.models import FileLoad, Inventory

# Forms
from ciberc.forms import UploadFileForm

# Python
import json


class UploadFileView(FormView):

    template_name = 'upload_file.html'
    form_class = UploadFileForm
    success_url = '/upload/'

    def form_valid(self, form):
        """Save form data."""
        file_summary = form.process_data()
        saved_instance = form.save()
        saved_instance.summary = json.dumps(file_summary)
        saved_instance.save()
        return super().form_valid(form)


class InventoryListView(ListView):

    context_object_name = 'inventory_list'
    queryset = Inventory.objects.all()
    template_name = 'inventory_list.html'


class UploadsListView(ListView):

    context_object_name = 'file_list'
    queryset = FileLoad.objects.all()
    template_name = 'file_list.html'
