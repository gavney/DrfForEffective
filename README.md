# DRF for Effective Development by @etogavrusha

Backend-приложение на Django REST Framework с JWT-аутентификацией и RBAC-авторизацией, реализованными вручную без готовых решений.

## Стек

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-red?style=flat)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)

---

## Быстрый старт

```bash
pip install -r requirements.txt
```

```sql
CREATE DATABASE auth_system;
```

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## Аутентификация

| Действие | Метод | Endpoint |
|---|---|---|
| Регистрация | POST | `/api/auth/register/` |
| Вход | POST | `/api/auth/login/` |
| Выход | POST | `/api/auth/logout/` |
| Обновление профиля | PUT | `/api/auth/profile/` |
| Удаление аккаунта | DELETE | `/api/auth/delete/` |

**Регистрация:** имя, фамилия, отчество, email, пароль.  
**Авторизация:** после логина передавать токен в заголовке:
```
Authorization: Bearer <token>
```
**Soft delete:** при удалении пользователь остаётся в БД с флагом `is_active = False`.

---

## RBAC — система прав доступа

```
User → UserRole → Role → Permission → Resource + Action
```

**Permission** задаётся в формате `resource:action`, например:
- `products:read`, `products:create`, `products:update`, `products:delete`
- `orders:read`, `orders:create`
- `reports:read`
- `rbac:manage`

### Встроенные роли

| Роль | Права |
|---|---|
| `admin` | Полный доступ |
| `manager` | products (read/update), orders (read/create), reports:read |
| `user` | products:read, orders:create |

---

## API

### RBAC (требует `rbac:manage`)

```
GET/POST   /api/rbac/resources/
GET/POST   /api/rbac/actions/
GET/POST   /api/rbac/permissions/
GET/POST   /api/rbac/roles/
GET/POST   /api/rbac/user-roles/
```

### Business (демо-модуль)

```
GET    /api/business/products/
POST   /api/business/products/create/
PUT    /api/business/products/<id>/update/
DELETE /api/business/products/<id>/delete/

GET    /api/business/orders/
POST   /api/business/orders/create/

GET    /api/business/reports/
```

---

## Коды ответов

| Код | Причина |
|---|---|
| `401` | Нет токена / невалидный / истёкший / пользователь неактивен |
| `403` | Нет нужного permission |

---

## Тестовые пользователи

| Роль | Email | Пароль |
|---|---|---|
| Admin | admin@test.com | Admin123! |
| Manager | manager@test.com | Manager123! |
