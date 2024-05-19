<!-- Админка -->
Username : superuser
Email address: superuser@rental.com
Password: 123451

<!-- Тестовый юзер -->
Username : testuser
Email address: testuser@gmail.com
Password: test12345userpassword

<!-- Запуск сервера -->
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

<!-- Установка всех нужных библиотек проекта -->
pip install -r requirements.txt