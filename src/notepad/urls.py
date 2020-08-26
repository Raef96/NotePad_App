from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from notes import views


urlpatterns = [
    path('', views.note_list_view, name='main_list'),
    path('finished_items/<id>/', views.done_item, name='finish_item'),
    path('deleted_items/<id>/', views.delete_item, name='delete_item'),
    path('recovered_items/<id>/', views.recover_item, name='recover_item'),


    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
