
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path("i18n/", include("django.conf.urls.i18n")),
    path('',include('myapp.urls')),
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += i18n_patterns(
#     path('',include('myapp.urls')),
# )

























# urlpatterns += i18n_patterns(
#     # Your internationalized URL patterns go here
#     path('', include('myapp.urls')),
#     path("i18n/", include("django.conf.urls.i18n")),
# )