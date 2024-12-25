1. Create folder in your desktop
2. ```
   git clone https://github.com/AlbertZaqaryan/django_login_register_user.git
   ```
   (in your empty folder)
3. ```
   py -m venv venv
   ```
4. ```
   .\venv\Scripts\activate
   ```
5. ```
   py -m pip install --upgrade pip
   ```
6. ```
   pip install django
   ```
7. ```
   pip install pillow
   ```
8. ```
   cd core
   ```
9. ```
   python manage.py makemigrations
   ```
10. ```
    python manage.py migrate
    ```
11. ```
    python manage.py createsuperuser
    ```
      -  create username for your admin
      -  email
      -  password1
      -  password2
    confirm registration
12. ```python manage.py runserver```
