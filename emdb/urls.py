from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls',namespace='movies')),
    path('login/', include('registeration.urls',namespace='registeration')),
    path('review/', include('review.urls',namespace='review')),
]