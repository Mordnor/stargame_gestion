"""stargame_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from gestion_intervention.views import CustomerListView, CustomerCreateView, SheetListView
from gestion_intervention.views import SheetCreateView, CustomerDetailView, SheetDetailView
from gestion_intervention.views import SheetPdfDetailView, CustomerUpdateView, SheetUpdateView
from gestion_intervention.views import CustomerDeleteView, SheetDeleteView, RequestListView
from gestion_intervention.views import RequestCreateView, RequestDetailView, RequestUpdateView
from gestion_intervention.views import RequestDeleteView, RequestPdfDetailView


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^login/$', auth_views.LoginView.as_view()),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='/')),

    url(r'^$', CustomerListView.as_view(), name='customer-list'),
    url(r'^customer/create/$', CustomerCreateView.as_view(), name='customer-create'),
    url(r'^customer/(?P<slug>[-\w]+)/(?P<pk>[-\w]+)/$', CustomerDetailView.as_view(),
    name='customer-detail'),
    url(r'^customer/(?P<slug>[-\w]+)/(?P<pk>[-\w]+)/update/$', CustomerUpdateView.as_view(),
    name='customer-update'),
    url(r'^customer/(?P<slug>[-\w]+)/(?P<pk>[-\w]+)/delete/$', CustomerDeleteView.as_view(),
    name='customer-delete'),

    url(r'^sheet/$', SheetListView.as_view(), name='sheet-list'),
    url(r'^sheet/create/$', SheetCreateView.as_view(), name='sheet-create'),
    url(r'^sheet/(?P<pk>[-\w]+)/$', SheetDetailView.as_view(),
    name='sheet-detail'),
    url(r'^sheet/(?P<pk>[-\w]+)/update/$', SheetUpdateView.as_view(),
    name='sheet-update'),
    url(r'^sheet/(?P<pk>[-\w]+)/delete/$', SheetDeleteView.as_view(),
    name='sheet-delete'),
    url(r'^sheet/pdf/(?P<pk>[-\w]+)/$', SheetPdfDetailView.as_view(),
    name='sheet-pdf-detail'),

    url(r'^request/$', RequestListView.as_view(), name='request-list'),
    url(r'^request/create/$', RequestCreateView.as_view(), name='request-create'),
    url(r'^request/(?P<pk>[-\w]+)/$', RequestDetailView.as_view(),
    name='request-detail'),
    url(r'^request/(?P<pk>[-\w]+)/update/$', RequestUpdateView.as_view(),
    name='request-update'),
    url(r'^request/(?P<pk>[-\w]+)/delete/$', RequestDeleteView.as_view(),
    name='request-delete'),
    url(r'^request/pdf/(?P<pk>[-\w]+)/$', RequestPdfDetailView.as_view(),
    name='request-pdf-detail'),

]
