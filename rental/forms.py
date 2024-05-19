# Импортируем необходимые модули и классы из Django и других библиотек
from django import forms
from .models import Booking
from tempus_dominus.widgets import DateTimePicker
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Определяем форму для бронирования автомобилей
class BookingForm(forms.ModelForm):
    # Поле для ввода времени начала бронирования с использованием виджета DateTimePicker
    start_time = forms.DateTimeField(
        widget=DateTimePicker(
            options={
                'useCurrent': True,  # Использовать текущее время по умолчанию
                'collapse': False,
                'locale': 'ru',  # Установить локаль на русский
                'format': 'DD.MM.YYYY HH:mm',  # Формат даты и времени
                'icons': {
                    'time': 'fa fa-clock',
                    'date': 'fa fa-calendar',
                    'up': 'fa fa-chevron-up',
                    'down': 'fa fa-chevron-down',
                    'previous': 'fa fa-chevron-left',
                    'next': 'fa fa-chevron-right',
                    'today': 'fa fa-screenshot',
                    'clear': 'fa fa-trash',
                    'close': 'fa fa-remove'
                }
            },
            attrs={
                'append': '',
                'icon_toggle': False,
            }
        )
    )
    
    # Поле для ввода времени окончания бронирования с использованием виджета DateTimePicker
    end_time = forms.DateTimeField(
        widget=DateTimePicker(
            options={
                'useCurrent': True,  # Использовать текущее время по умолчанию
                'collapse': False,
                'locale': 'ru',  # Установить локаль на русский
                'format': 'DD.MM.YYYY HH:mm',  # Формат даты и времени
                'icons': {
                    'time': 'fa fa-clock',
                    'date': 'fa fa-calendar',
                    'up': 'fa fa-chevron-up',
                    'down': 'fa fa-chevron-down',
                    'previous': 'fa fa-chevron-left',
                    'next': 'fa fa-chevron-right',
                    'today': 'fa fa-screenshot',
                    'clear': 'fa fa-trash',
                    'close': 'fa fa-remove'
                }
            },
            attrs={
                'append': '',
                'icon_toggle': False,
            }
        )
    )

    class Meta:
        model = Booking
        fields = ['car', 'start_time', 'end_time']
        widgets = {
            'car': forms.HiddenInput(),  # Скрытое поле для автомобиля
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        car = initial.get('car')
        super().__init__(*args, **kwargs)
        if car:
            self.fields['car'].initial = car  # Установка начального значения для автомобиля

    def clean(self):
        cleaned_data = super().clean()
        car = cleaned_data.get('car')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        # Проверка, чтобы время окончания было позже времени начала
        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError("Время окончания должно быть позже времени начала.")
        
        # Проверка, доступен ли автомобиль для бронирования
        if car and not car.available:
            raise forms.ValidationError("Этот автомобиль недоступен.")
        
        return cleaned_data

# Форма для регистрации новых пользователей
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Дополнительное поле для ввода email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Форма для входа пользователей в систему
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))