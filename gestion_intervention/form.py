from django.forms import ModelForm
from .models import Sheet, Customer

class SheetForm(ModelForm):
    class Meta:
        model = Sheet
        fields = "__all__"
        success_url = "/"


