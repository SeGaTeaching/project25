"""
URL configuration for project25 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import wednesday.views

# Das hier brauchst du für die Bilder:
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('isitwednesday/', wednesday.views.is_wednesday, name="is_wednesday"),
    path('', include('start.urls')),
    path('query/', include('get_examples.urls')),
    path('models/', include('models_examples.urls')),
    path('weather/', include('weather.urls')),
    path('forms/', include('bia_forms.urls')),
    path('accounts/', include('accounts.urls')),
    path('movies/', include('movies.urls')),
    path('snippet/', include('api.urls')),
    path('api/', include('employee.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
