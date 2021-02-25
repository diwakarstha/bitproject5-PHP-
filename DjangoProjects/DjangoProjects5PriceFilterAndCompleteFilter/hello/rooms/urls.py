from django.contrib import admin
from django.urls import path
from rooms import views
from rooms.views import AddRoomView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.rooms, name='rooms'),
    path("addroom", AddRoomView.as_view(), name='addroom'),
    path("viewroom", views.viewroom, name='viewroom'),
    path("editroom/<str:pk>", views.editroom, name='editroom'),
    path("rooms", views.rooms, name='rooms'),
    path("roomdetail", views.roomdetail, name='roomdetail'),
    path('ajax/load-locations/', views.load_locations,
         name='ajax_load_locations'),  # AJAX
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
