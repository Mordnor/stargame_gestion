# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Customer, Sheet

# Create your views here.
class CustomerListView(ListView):
    models = Customer
    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query != None:
            return Customer.objects.filter(last_name=query)
        else:
            return Customer.objects.all()

class CustomerCreateView(CreateView):
    models = Customer
    fields = '__all__'
    template_name = 'gestion_intervention/customer_update_form.html'
    success_url="/" 
    
    def get_queryset(self):
        return Customer.objects.all()