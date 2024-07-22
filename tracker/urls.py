from django.contrib import admin
from django.urls import path, include
from tracker import views as tracker_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', tracker_views.register, name='register'),
    path('login/', tracker_views.login_view, name='login'),
    path('logout/', tracker_views.logout_view, name='logout'),
    path('', tracker_views.index, name='index'),
    path('add_intake/<int:amount>/', tracker_views.add_intake, name='add_intake'),
    path('history/', tracker_views.history, name='history'),
    path('accounts/', include('django.contrib.auth.urls')),  # Adicione esta linha
]
