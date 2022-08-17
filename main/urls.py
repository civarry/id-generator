from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name = 'success'),
    path('identification/', views.identification, name = 'identification'),
    path('identification/delete/<int:id>', views.delete, name='delete'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)