from django.forms import ModelForm

from .models import yearlydata
from .models import Entity

from django import forms

class EntityForm(ModelForm): # yearlydataForm with capital F to distinguish form methods in views.py 
    class Meta:
        model = Entity
        fields = '__all__'


class yearlydataForm(ModelForm): # yearlydataForm with capital F to distinguish form methods in views.py 
    class Meta:
        model = yearlydata
        fields = '__all__'
        #widgets = {'entity': Entity}
        #entity = forms.ModelChoiceField(queryset=yearlydata.objects.all()) 

 