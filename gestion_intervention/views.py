# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import datetime
from django.utils import formats
from django_weasyprint import WeasyTemplateResponseMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse
from .form import SheetForm
from .models import Customer, Sheet

# Create your views here.
class CustomerListView(ListView):
    models = Customer
    def get_queryset(self):
        return Customer.objects.all()


class CustomerCreateView(CreateView):
    models = Customer
    fields = '__all__'
    template_name = 'gestion_intervention/customer_update_form.html'
    success_url="/" 

    def get_success_url(self):
        return reverse('customer-detail', kwargs={'slug' : self.object.slug, 'pk' : self.object.id})
    
    def get_queryset(self):
        return Customer.objects.all()


class CustomerDetailView(DetailView):
    models = Customer
    
    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        today_date = datetime.now()
        context['date'] = today_date.strftime("%d/%m/%Y")
        context['sheet_form'] = SheetForm(initial={"customer" : self.object})
        context['sheets'] = Sheet.objects.filter(customer = self.object)
        return context

    def get_queryset(self):
        return Customer.objects.all()

class CustomerUpdateView(UpdateView):
    models = Customer
    fields = '__all__'
    template_name = 'gestion_intervention/customer_update_form.html'


    def get_success_url(self):
        return reverse('customer-detail', kwargs={'slug' : self.object.slug, 'pk' : self.object.id})

    def get_queryset(self):
        return Customer.objects.all()

        


class SheetListView(ListView):
    models = Sheet
    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query != None:
            return Sheet.objects.filter(last_name=query)
        else:
            return Sheet.objects.all()


class SheetCreateView(CreateView):
    models = Sheet
    fields = '__all__'
    template_name = 'gestion_intervention/sheet_update_form.html'
    
    def get_success_url(self):
        return reverse('sheet-detail', kwargs={'pk' : self.object.pk})
    
    def get_queryset(self):
        return Sheet.objects.all()


class SheetDetailView(DetailView):
    models = Sheet
    
    def get_queryset(self):
        return Sheet.objects.all()

class SheetUpdateView(UpdateView):
    models = Sheet
    fields = '__all__'
    template_name = 'gestion_intervention/sheet_update_form.html'


    def get_success_url(self):
        return reverse('sheet-detail', kwargs={'pk' : self.object.id})

    def get_queryset(self):
        return Sheet.objects.all()

class SheetPdfDetailView(WeasyTemplateResponseMixin, SheetDetailView):
    def get_context_data(self, **kwargs):
        context = SheetDetailView.get_context_data(self, **kwargs)
        context['is_pdf'] = True
        return context