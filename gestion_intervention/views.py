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
from .form import SheetForm, RequestForm
from .models import Customer, Sheet, Request

# Create your views here.
class CustomerListView(ListView):
    models = Customer
    paginate_by = 21
    def get_queryset(self):
        return Customer.objects.all().order_by('-id')


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
        context['request_form'] = RequestForm(initial={"customer" : self.object})
        context['sheets'] = Sheet.objects.filter(customer = self.object)
        context['requests'] = Request.objects.filter(customer = self.object)
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

class CustomerDeleteView(DeleteView):
    model = Customer

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return '/'

        
class SheetListView(ListView):
    models = Sheet
    paginate_by = 21
    def get_queryset(self):
        return Sheet.objects.all().order_by('-date')


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

class SheetDeleteView(DeleteView):
    model = Sheet

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return '/'


class SheetPdfDetailView(WeasyTemplateResponseMixin, SheetDetailView):
    def get_context_data(self, **kwargs):
        context = SheetDetailView.get_context_data(self, **kwargs)
        context['is_pdf'] = True
        return context


class RequestListView(ListView):
    models = Request
    paginate_by = 21
    def get_queryset(self):
        return Request.objects.all().order_by('-date')

class RequestCreateView(CreateView):
    models = Request
    fields = '__all__'
    template_name = 'gestion_intervention/request_update_form.html'
    
    def get_success_url(self):
        return reverse('request-detail', kwargs={'pk' : self.object.pk})
    
    def get_queryset(self):
        return Request.objects.all()

class RequestDetailView(DetailView):
    models = Request
    
    def get_queryset(self):
        return Request.objects.all()

class RequestUpdateView(UpdateView):
    models = Request
    fields = '__all__'
    template_name = 'gestion_intervention/request_update_form.html'

    def get_success_url(self):
        return reverse('request-detail', kwargs={'pk' : self.object.id})

    def get_queryset(self):
        return Request.objects.all()

class RequestDeleteView(DeleteView):
    model = Request

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return '/'

class RequestPdfDetailView(WeasyTemplateResponseMixin, RequestDetailView):
    def get_context_data(self, **kwargs):
        context = RequestDetailView.get_context_data(self, **kwargs)
        context['is_pdf'] = True
        return context

