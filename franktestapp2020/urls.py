from django.urls import path

from . import views

from .views import EntityListView
from .views import EntityDetailView

from .views import YearlyDataListView
from .views import YearlyDataDetailView
 
#app_name = 'autos'

urlpatterns = [
    # Generic Entity List View
    path('', EntityListView.as_view(), name='entity-list'),
    #path('', views.index, name='index'),
    #path('<int:Entity_id>/', views.detailentity, name='entitydetail'), 
    # Generic Entity Detail View
    path('<int:pk>/', EntityDetailView.as_view(), name='entity-detail'),
    # generic entity create form - .as_view() important otherwise error: init takes 1 posit arg but 2 were given
    path('entitycreateform', views.EntityCreate.as_view(), name='entitycreateform'), 
    # generic entity update form
    path('entityupdateform/<int:pk>', views.EntityUpdate.as_view(), name='entityupdateform'), 
    # generic entity delete form
    path('entitydeleteform/<int:pk>', views.EntityDelete.as_view(), name='entitydeleteform'), 
    # Generic YearlyData ListView - don't forget to import view
    path('yearlydata-list', YearlyDataListView.as_view(), name='yearlydata-list'),
    # Generic YearlyData Detail View
    path('yearlydata-detail/<int:pk>/', YearlyDataDetailView.as_view(), name='yearlydata-detail'),
    # Generic Yearlydata Create Form
    path('yearlydatacreateform', views.YearlyDataCreate.as_view(), name='yearlydatacreateform'),
    # Generic Yearlydata Update Form
     path('yearlydataupdateform/<int:pk>', views.YearlyDataUpdate.as_view(), name='yearlydataupdateform'), 
    # Generic Yearlydata Delete Form
    path('yearlydatadeleteform/<int:pk>', views.YearlyDataDelete.as_view(), name='yearlydatadeleteform'), 

    path('yearlydataform', views.yearlydataform, name='yearlydataform'),
    path('yearlydatalist', views.yearlydataview, name='yearlydataview'),
    
    #path('yearlydatadetail/<int:yearlydata_id>/', views.detail, name='yearlydatadetail'), # this url not important 
    #path('<int:Entity_id>/update/', views.entityupdate.as_view(), name='entityupdate'),
    #path('<int:Entity_id>/update/', views.entityupdate, name='entityupdate'),
    path('<int:Entity_id>/update/yearlydataform', views.yearlydataform, name='yearlydataform'), # still works, keep it 
    

]