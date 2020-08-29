from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from todo import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.createTask, name='create-task'),
    path('delete/<int:pk>', views.deleteTask, name='delete-task'),
    path('update/<int:pk>', views.updateTask, name='update-task'),
    path('status/<int:pk>', views.updateTaskStatus, name='update-status-task'),

    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

