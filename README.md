# Проект YATUBE_API
API для Социальной сети
## Меню
- [Описание](#описание-)
- [Технологии](#технологии-)
- [Запуск проекта](#запуск-проекта-)
- [Примеры api запросов](#примеры-api-запросов-)
- [Автор](#автор-)

## Описание 
```
Это Пет-проект API для мини-социальной сети для блогеров Yatube.
```
## Технологии
Python, Django, DRF
## Запуск проекта
- Клонировать репозиторий: git clone https://github.com/SokoDi/api_final_yatube.git
- Установите и активируйте виртуальное окружение:
```
Для пользователей Windows:
python -m venv env
source env/Scripts/activate
python -m pip install --upgrade pip
```
```
В зависимости от вашей IDE
py -m venv env
source env/Scripts/activate
py -m pip install --upgrade pip
```
```
Установка зависимостей pip install -r requirements.txt
```
```
Выполнить миграции: python manage.py migrate
```
```
Запуск проекта: python manage.py runserver
```
## Примеры api запросов
- `api/v1/jwt/create/` (POST): передаём логин и пароль, получаем токен.
- `api/v1/jwt/refresh/` (GET) Обновление токена
- `api/v1/jwt/verify/` (GET) Проверка токена
- `api/v1/posts/` (GET, POST): получаем список всех постов или создаём новый пост.
- `api/v1/posts/{post_id}/` (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост.
- `api/v1/groups/` (GET): получаем список всех групп.
- `api/v1/groups/{group_id}/` (GET): получаем информацию о группе.
- `api/v1/posts/{post_id}/comments/` (GET, POST): получаем список всех комментариев поста с поста по `id` или создаём новый, указав `id` поста, который хотим прокомментировать.
- `api/v1/posts/{post_id}/comments/{comment_id}/` (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по `id` у `post_id`
- `api/v1/posts/follw/` (GET, POST): Возвращает все подписки пользователя, подписка на автора .
## Автор
```
Соколов Дмитрий
```