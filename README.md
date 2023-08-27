# SimpleChat
Итоговый проект к модулю E6.

<H2>Описание реализованных в проекте функций.</H2> 

- На первой странице Чата пользователю предлагается зарегистрироваться на сайте или войти с уже имеющимся логином и паролем.<br>
- После авторизации пользователю становятся доступны Комнаты Чата и редактирование Профиля пользователя.<br>
- У зарегистрированного пользователя есть возможность создать собственную Комнату или перейти в существующую.<br>
- В Комнате пользователь может оставить сообщение в общем чате или отправить приватное сообщение любому пользователю из списка подлюченных пользователей.<br>
- Для редактирования своего профиля пользователю неоходимо перейти по ссылке в панели навигации. В профиле пользователь может добавить/отредактировать информацию о почтовом адресе, о себе и добавить аватар.<br>

<H2>Быстрый старт</H2>

Инструция составлена для операционной системы Windows.<br>

Клонируем проект в заранее созданную директорию SimoleChat_proj
```bash
git clone https://github.com/ZakharovAlexA/SimpleChat.git
```

Из директории SimpleChat_proj запускаем и настраиваем виртуальное окружение проекта
```bash
python -m venv venv
venv\scripts\activate
cd .\SimpleChat\ 
pip install -r requirements.txt
```

Генерируем Django secret-key
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
И вставляем его в .\SimpleChat\settings.py
```python
SECRET_KEY = ''
```
Запускаем сервер
```bash
python manage.py runserver
```
