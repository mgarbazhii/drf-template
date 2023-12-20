# drf-template

drf template with djoser, swagger

# Создаем виртуальное окружение

    python3 -m venv env

# Активируем окружение и обновляем менеджер

    source env/bin/activate
    pip install --upgrade pip

# Устанавливаем Django и пакеты

    pip install django
    pip install djangorestframework django-filter django-environ django-cors-headers django-extensions psycopg2-binary

# Или устанавливаем все из файла requirements.txt

    pip install -r requirements.txt

# В случае добавления пакетов схраняем в requirements.txt

    pip freeze > requirements.txt

# Создаем проект в текущей директории

    django-admin startproject core .

# Обновляем файл settings

    import environ
    import os

    env = environ.Env()  # get environment variables from .env file
    root = environ.Path(__file__) - 2  # get root of the project
    environ.Env.read_env(env.str(root(), '.env'))  # reading .env file

    BASE_DIR = root()
    SECRET_KEY = env.str('SECRET_KEY')
    DEBUG = env.bool('DEBUG', default=False)
    ALLOWED_HOSTS = env.str('ALLOWED_HOSTS').split(' ')

# Запускаем БД PostGreSQL в docker

    sudo docker run -itd -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=ПАРОЛЬ -p 5432:5432 -v data:/var/lib/postgresql/data --name hwb_postgres postgres
