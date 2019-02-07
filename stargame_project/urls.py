from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from gestion_intervention.views import CustomerListView, CustomerCreateView, SheetListView
from gestion_intervention.views import SheetCreateView, CustomerDetailView, SheetDetailView
from gestion_intervention.views import SheetPdfDetailView, CustomerUpdateView, SheetUpdateView
from gestion_intervention.views import CustomerDeleteView, SheetDeleteView, RequestListView
from gestion_intervention.views import RequestCreateView, RequestDetailView, RequestUpdateView
from gestion_intervention.views import RequestDeleteView, RequestPdfDetailView, SheetChangeImportantTrue
from gestion_intervention.views import SheetChangeImportantFalse, SheetArchiveView, SheetListArchiveView
from gestion_intervention.views import SheetRemoveArchiveView


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # LOG URLS
    url(r'^login/$', auth_views.LoginView.as_view()),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='/')),


    # CUSTOMERS VIEWS
    url(r'^$', CustomerListView.as_view(), name='customer-list'),
    url(r'^customer/create/$', CustomerCreateView.as_view(), name='customer-create'),
    url(r'^customer/(?P<slug>[-\w]+)/(?P<pk>[-\w]+)/$', CustomerDetailView.as_view(),
    name='customer-detail'),
    url(r'^customer/(?P<slug>[-\w]+)/(?P<pk>[-\w]+)/update/$', CustomerUpdateView.as_view(),
    name='customer-update'),
    url(r'^customer/(?P<slug>[-\w]+)/(?P<pk>[-\w]+)/delete/$', CustomerDeleteView.as_view(),
    name='customer-delete'),


    # SHEET URLS
    url(r'^sheet/$', SheetListView.as_view(), name='sheet-list'),
    url(r'^sheet/$', SheetListView.as_view(), name='sheet-list'),
    url(r'^sheet/create/$', SheetCreateView.as_view(), name='sheet-create'),
    url(r'^archives/$', SheetListArchiveView.as_view(), name='archive-list'),
    url(r'^sheet/(?P<pk>[-\w]+)/$', SheetDetailView.as_view(),
    name='sheet-detail'),
    url(r'^sheet/(?P<pk>[-\w]+)/update/$', SheetUpdateView.as_view(),
    name='sheet-update'),
    url(r'^sheet/(?P<pk>[-\w]+)/delete/$', SheetDeleteView.as_view(),
    name='sheet-delete'),
    url(r'^sheet/pdf/(?P<pk>[-\w]+)/$', SheetPdfDetailView.as_view(),
    name='sheet-pdf-detail'),
    url(r'sheet/(?P<pk>[-\w]+)/change/true$', SheetChangeImportantTrue.as_view(), name='change-sheet-important-true'),
    url(r'sheet/(?P<pk>[-\w]+)/change/false$', SheetChangeImportantFalse.as_view(), name='change-sheet-important-false'),
    url(r'sheet/(?P<pk>[-\w]+)/archive$', SheetArchiveView.as_view(), name='change-sheet-archive'),
    url(r'sheet/(?P<pk>[-\w]+)/archive/remove$', SheetRemoveArchiveView.as_view(), name='remove-sheet-archive'),


    # REQUEST SHEET URLS
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
