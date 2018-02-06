from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from registeration.views import  AboutView
app_name='emdb'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls',namespace='movies')),
    path('login/', include('registeration.urls',namespace='registeration')),
    path('review/', include('review.urls',namespace='review')),
    path('', include('movies.urls',namespace='movies')),
    path('about/', AboutView.as_view(), name ='about'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)