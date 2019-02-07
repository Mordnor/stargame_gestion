# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import datetime
from django.utils import formats
from django_weasyprint import WeasyTemplateResponseMixin
from django.views.generic import ListView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from .form import SheetForm, RequestForm
from .models import Customer, Sheet, Request

# =================== CUSTOMERS VIEWS =================== #

# LIST ALL CUSTOMERS
class CustomerListView(ListView):
    models = Customer
    def get_queryset(self):
        return Customer.objects.all().order_by('-id')


# CUSTOMER DETAILS
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


# CREATE A CUSTOMER
class CustomerCreateView(CreateView):
    models = Customer
    fields = '__all__'
    template_name = 'gestion_intervention/customer_update_form.html' 
    success_url="/" 

    # redirect to customer detail 
    def get_success_url(self):
        return reverse('customer-detail', kwargs={'slug' : self.object.slug, 'pk' : self.object.id})
    
    def get_queryset(self):
        return Customer.objects.all()


# UPDATE CUSTOMERS 
class CustomerUpdateView(UpdateView):
    models = Customer
    fields = '__all__'
    template_name = 'gestion_intervention/customer_update_form.html'

    # redirect to customer detail 
    def get_success_url(self):
        return reverse('customer-detail', kwargs={'slug' : self.object.slug, 'pk' : self.object.id})

    def get_queryset(self):
        return Customer.objects.all()


# DELETE CURSTOMER
class CustomerDeleteView(DeleteView):
    model = Customer

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return '/'

        
# =================== SHEET VIEWS =================== #

# LIST ALL SHEET TO DO
class SheetListView(ListView):
    models = Sheet

    def get_queryset(self):
        return Sheet.objects.filter(archive=False).order_by('-date')


# LIST ALL SHEET ALREADY DONE
class SheetListArchiveView(ListView):
    models = Sheet
    template_name = 'gestion_intervention/archive_list.html'

    def get_queryset(self):
        return Sheet.objects.filter(archive=True).order_by('-date')


# LET CHANGE IMPORTANT ENTRY TO TRUE
class SheetChangeImportantTrue(View):
    models = Sheet

    def post(self, request, **kwargs):
        current_sheet = request.POST.get('sheet_id', None)
        sheet = Sheet.objects.get(pk=current_sheet)
        sheet.important = True
        sheet.save()
        return redirect('sheet-list',)


# LET CHANGE IMPORTANT ENTRY TO FALSE
class SheetChangeImportantFalse(View):
    models = Sheet

    def post(self, request, **kwargs):
        current_sheet = request.POST.get('sheet_id', None)
        sheet = Sheet.objects.get(pk=current_sheet)
        sheet.important = False
        sheet.save()
        return redirect('sheet-list',)


# LET ARCHIVE THE SHEETS
class SheetArchiveView(View):
    models = Sheet

    def post(self, request, **kwargs):
        current_sheet = request.POST.get('sheet_id', None)
        sheet = Sheet.objects.get(pk=current_sheet)
        sheet.archive = True
        sheet.save()
        return redirect('sheet-list',)


# REMOVE ARCHIVE STATUT FROM SHEETS
class SheetRemoveArchiveView(View):
    models = Sheet

    def post(self, request, **kwargs):
        current_sheet = request.POST.get('sheet_id', None)
        sheet = Sheet.objects.get(pk=current_sheet)
        sheet.archive = False
        sheet.save()
        return redirect('archive-list',)


# CREATE SHEET
class SheetCreateView(CreateView):
    models = Sheet
    fields = '__all__'
    template_name = 'gestion_intervention/sheet_update_form.html'
    
    # redirect to sheet detail
    def get_success_url(self):
        return reverse('sheet-detail', kwargs={'pk' : self.object.pk})
    
    def get_queryset(self):
        return Sheet.objects.all()


# DETAILS SHEET
class SheetDetailView(DetailView):
    models = Sheet
    
    def get_queryset(self):
        return Sheet.objects.all()


# UPDATE SHEET
class SheetUpdateView(UpdateView):
    models = Sheet
    fields = '__all__'
    template_name = 'gestion_intervention/sheet_update_form.html'

    # redirect to sheet detail
    def get_success_url(self):
        return reverse('sheet-detail', kwargs={'pk' : self.object.id})

    def get_queryset(self):
        return Sheet.objects.all()


# DELETE SHEET
class SheetDeleteView(DeleteView):
    model = Sheet

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return '/'


# TRANSFORM SHEET DETAIL TO PDF (WeasyPrint)
class SheetPdfDetailView(WeasyTemplateResponseMixin, SheetDetailView):
    def get_context_data(self, **kwargs):
        context = SheetDetailView.get_context_data(self, **kwargs)
        context['is_pdf'] = True
        return context



# =================== REQUESTS VIEWS =================== #

# LIST ALL REQUESTS
class RequestListView(ListView):
    models = Request
    def get_queryset(self):
        return Request.objects.all().order_by('-date')


# CREATE REQUEST
class RequestCreateView(CreateView):
    models = Request
    fields = '__all__'
    template_name = 'gestion_intervention/request_update_form.html'
    
    # redirect to request detail
    def get_success_url(self):
        return reverse('request-detail', kwargs={'pk' : self.object.pk})
    
    def get_queryset(self):
        return Request.objects.all()


# REQUEST DETAIL
class RequestDetailView(DetailView):
    models = Request
    
    def get_queryset(self):
        return Request.objects.all()


# UPDATE REQUEST
class RequestUpdateView(UpdateView):
    models = Request
    fields = '__all__'
    template_name = 'gestion_intervention/request_update_form.html'

    # redirect to request detail
    def get_success_url(self):
        return reverse('request-detail', kwargs={'pk' : self.object.id})

    def get_queryset(self):
        return Request.objects.all()


# DELETE REQUEST
class RequestDeleteView(DeleteView):
    model = Request

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return '/'


# TRANSFORM REQUEST DETAIL TO PDF (WeasyPrint)
class RequestPdfDetailView(WeasyTemplateResponseMixin, RequestDetailView):
    def get_context_data(self, **kwargs):
        context = RequestDetailView.get_context_data(self, **kwargs)
        context['is_pdf'] = True
        return context

