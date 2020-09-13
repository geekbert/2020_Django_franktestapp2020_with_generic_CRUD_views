from django.shortcuts import render

from django.http import HttpResponseRedirect 
from django.forms import modelformset_factory

#from django.http import HttpResponse

from .models import Entity
from .models import yearlydata

#def index(request): # function view replaced by generic list view (OO, class inheritance) below
    #entity_list = Entity.objects.all()
    #context = {'entity_list': entity_list}
    #return render(request, 'franktestapp2020/index.html', context)
    #return HttpResponse("Hello, world. You're at the APPs index.")

from django.views.generic.list import ListView

class EntityListView(ListView):
    model = Entity
    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    #context['now'] = timezone.now()
    #    return context


#def detailentity(request, Entity_id): # replaced by generic customized detailview below
#    entitydetail = get_object_or_404(Entity, pk=Entity_id)
#    related_yearlydata_list = yearlydata.objects.filter(entity=Entity_id)
#    return render(request, 'franktestapp2020/entitydetail.html', {'Entity': entitydetail,'yearlydata_list': related_yearlydata_list})        

from django.shortcuts import get_object_or_404 
from django.views.generic.detail import DetailView
class EntityDetailView(DetailView):
    model = Entity
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print(context['entity'])
        print(self.kwargs) # {'pk': 1}
        entitypk = get_object_or_404(Entity, pk=self.kwargs['pk']) # how to find PK of model - not easy 
        context['related_yearlydata_list'] = yearlydata.objects.filter(entity=entitypk) # add in custom context !! 
        print(context)  # {'object': <Entity: Test Entity> .....
        return context


# Generic Create View

from django.views.generic.edit import CreateView
from .models import Entity
from django.urls import reverse_lazy

class EntityCreate(CreateView): # assumes by convention template called entity_form.html
    model = Entity
    fields = '__all__'
    #fields = ['entity_name']
    success_url = reverse_lazy('entity-list') 


# Generic Update View

from django.views.generic.edit import UpdateView
from .models import Entity

class EntityUpdate(UpdateView):
    model = Entity
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('entity-list') 

# Generic Entity Delete View

from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Entity

class EntityDelete(DeleteView): # assumes by convention template called entity_confirm_delete.html
    model = Entity
    success_url = reverse_lazy('entity-list')


# Generic Yearlydata Listview
from django.views.generic.list import ListView

class YearlyDataListView(ListView):
    model = yearlydata

# Generic yearlydata detail view

from django.shortcuts import get_object_or_404 
from django.views.generic.detail import DetailView
class YearlyDataDetailView(DetailView):
    model = yearlydata
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print(self.kwargs) # {'pk': 1}
        #yearlydatapk = get_object_or_404(yearlydata, pk=self.kwargs['pk']) # how to find PK of model - not easy 
        context['yearlydata_detail'] = yearlydata.objects.filter(id=(self.kwargs['pk'])) # add in custom context !! 
        #print(context)  # {'object': <Entity: Test Entity> .....
        return context

# Generic YearlyData Create View

from django.views.generic.edit import CreateView
from .models import yearlydata
from django.urls import reverse_lazy

class YearlyDataCreate(CreateView): # assumes by convention template called entity_form.html
    model = yearlydata
    fields = '__all__'
    #fields = ['entity_name']
    success_url = reverse_lazy('yearlydata-list') 

# Generic YearlyData Update View 

from django.views.generic.edit import UpdateView
from .models import yearlydata

class YearlyDataUpdate(UpdateView):
    model = yearlydata
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('yearlydata-list') 

# Generic YearlyData Delete View 

from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import yearlydata

class YearlyDataDelete(DeleteView): # assumes by convention template called entity_confirm_delete.html
    model = yearlydata
    success_url = reverse_lazy('yearlydata-list')









# OLD SHIT BEFORE GENERIC VIEWS BUT STILL WORKS 

def yearlydataview(request): # html url is yearlydatalist.html see below 
    yearlydata_list = yearlydata.objects.all()
    context = {'yearlydata_list': yearlydata_list}
    return render(request, 'franktestapp2020/yearlydatalist.html', context)

from .forms import yearlydataForm
from django.shortcuts import redirect

def yearlydataform(request):    # this still works, despite already using Generic CRUD views 
    formcontext = {'form': yearlydataForm}
    if request.method == 'POST':
        form = yearlydataForm(request.POST) # this ensures {{ form }} in template finds this  
        if form.is_valid():
            form.save()
            # NEW to avoid POST Form Double POST when refreshing browser 
            success_url = reverse_lazy('yearlydata-list')
            return redirect(success_url) # from https://realpython.com/django-redirects/ and Charles Severance DJ4E 
            #return render(request, 'franktestapp2020/yearlydataform.html', formcontext)
        else: 
            print('Console prints: form not valid')
    else: 
        form = yearlydataForm() # render new empty form 
    return render(request, 'franktestapp2020/yearlydataform.html', formcontext)   

 

 
 