"""rento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('superadmin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('useradmin/', include('useradmin.urls')),
    path('user/', include('user.urls')),
    path('rooms/', include('rooms.urls')),
    path('rent/', include('rent.urls')),
    path('enquiry/', include('enquiry.urls')),
    path('complaint/', include('complaint.urls')),
    path('feature/', include('feature.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

