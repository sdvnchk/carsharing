"""
URL configuration for carsharing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

# Импортируем нужные функции и классы из Django
from django.contrib import admin
from django.urls import path, include

# Здесь мы определяем URL-ы, которые будут доступны в нашем приложении
urlpatterns = [
    # URL для админки Django, доступен по адресу /admin/
    path('admin/', admin.site.urls),

    # URL для нашего приложения "rental". Все пути из rental/urls.py будут доступны с корня сайта.
    path('', include('rental.urls')),

    # URL для встроенных страниц аутентификации Django, например, для входа и выхода из аккаунта.
    path('accounts/', include('django.contrib.auth.urls')),
]
