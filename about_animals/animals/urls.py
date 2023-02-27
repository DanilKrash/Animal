from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import animal_detail_view, save_img_view


urlpatterns = [
    path('', views.list, name='home'),
    path('create', views.create, name='create'),
    path('post/<int:animal_id>/', animal_detail_view, name='animal_detail'),
    path('save-image/', save_img_view, name='save_image'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
