from django.conf.urls import url 
from tutorials import views 
 
urlpatterns = [ 
    path('crud/', views.crud_list),
]
