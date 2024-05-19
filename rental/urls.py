# Импортируем функцию path из django.urls и наш views модуль
from django.urls import path
from . import views

# Определяем список маршрутов для нашего приложения
urlpatterns = [
    # Маршрут для главной страницы. Когда пользователь заходит на корневой URL (''), вызывается функция index из views.
    path('', views.index, name='index'),

    # Маршрут для бронирования автомобиля. Когда пользователь заходит на URL, который включает ID автомобиля,
    # вызывается функция book_car из views.
    path('book/<int:car_id>/', views.book_car, name='book_car'),

    # Маршрут для регистрации. Когда пользователь заходит на URL '/register/', вызывается функция register из views.
    path('register/', views.register, name='register'),

    # Маршрут для входа в систему. Когда пользователь заходит на URL '/login/', вызывается функция login_view из views.
    path('login/', views.login_view, name='login'),
]
