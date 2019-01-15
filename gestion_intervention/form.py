from django.forms import ModelForm
from .models import Sheet, Customer, Request

class SheetForm(ModelForm):
    class Meta:
        model = Sheet
        fields = "__all__"
        success_url = "/"

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = "__all__"
        success_url = "/"



