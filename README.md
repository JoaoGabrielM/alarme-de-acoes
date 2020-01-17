# alarme-de-acoes
Aplicativo para notificar usuários sobre preços das ações




# local_settings.py
Para esse projeto funcionar, é necessário criar um arquivo dentro de `AlarmeDeAcoes/AlarmeDeAcoes` chamado `local_settings.py`

Dentro desse arquivo deve conter as seguintes configurações

```
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n^@sy4x7puv_5!u7(zbzb6-_h#$o+b_y20(7#y54k!3$ebeh-b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```