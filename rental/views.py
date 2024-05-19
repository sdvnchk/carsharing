# Импортируем необходимые функции и классы из Django
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Car, Booking
from .forms import BookingForm, UserRegisterForm, UserLoginForm

# Представление для главной страницы
def index(request):
    # Получаем список всех доступных автомобилей
    cars = Car.objects.filter(available=True)
    # Отображаем страницу index.html с переданными данными об автомобилях
    return render(request, 'rental/index.html', {'cars': cars})

# Представление для бронирования автомобиля. Только авторизованные пользователи могут бронировать автомобили.
@login_required
def book_car(request, car_id):
    # Получаем автомобиль по ID или возвращаем ошибку 404, если автомобиль не найден
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        # Копируем данные POST-запроса и добавляем ID автомобиля
        post_data = request.POST.copy()
        post_data['car'] = car.id
        # Создаем форму бронирования с переданными данными
        form = BookingForm(post_data)
        if form.is_valid():
            # Если форма валидна, создаем объект бронирования, но не сохраняем его в базу данных сразу
            booking = form.save(commit=False)
            # Устанавливаем пользователя и автомобиль для бронирования
            booking.user = request.user
            booking.car = car
            # Вычисляем общую стоимость бронирования
            booking.calculate_total_price()
            # Сохраняем бронирование в базу данных
            booking.save()
            # Обновляем доступность автомобиля
            car.available = False
            car.save()
            # Перенаправляем пользователя на главную страницу
            return redirect('index')
        else:
            # Если форма не валидна, выводим ошибки в консоль
            print(form.errors)
    else:
        # Если запрос не POST, создаем форму с начальным значением для автомобиля
        form = BookingForm(initial={'car': car.id})
    # Отображаем страницу бронирования с переданной формой и данными об автомобиле
    return render(request, 'rental/book_car.html', {'form': form, 'car': car})

# Представление для регистрации пользователя
def register(request):
    if request.method == 'POST':
        # Создаем форму регистрации с данными POST-запроса
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Если форма валидна, сохраняем нового пользователя
            form.save()
            # Аутентифицируем пользователя после регистрации
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            # Выполняем вход пользователя в систему
            login(request, user)
            # Перенаправляем пользователя на главную страницу
            return redirect('index')
    else:
        # Если запрос не POST, создаем пустую форму регистрации
        form = UserRegisterForm()
    # Отображаем страницу регистрации с переданной формой
    return render(request, 'registration/register.html', {'form': form})

# Представление для входа пользователя в систему
def login_view(request):
    if request.method == 'POST':
        # Создаем форму входа с данными POST-запроса
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            # Если форма валидна, получаем пользователя
            user = form.get_user()
            # Выполняем вход пользователя в систему
            login(request, user)
            # Перенаправляем пользователя на главную страницу
            return redirect('index')
    else:
        # Если запрос не POST, создаем пустую форму входа
        form = UserLoginForm()
    # Отображаем страницу входа с переданной формой
    return render(request, 'registration/login.html', {'form': form})
