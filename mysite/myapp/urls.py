from django.urls import path,include
from . import views
from django.conf import settings

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('',views.home,name="homepage"),
   
] 

