# ckan-import

## Setup

```
$ cd ckan-import
$ python3 -m venv venv
$ source venv/bin/activate
(default)$ pip install -r requirements.txt
```

### Configurar variables de entorno

Actualice el valor de las variables de entorno en el archivo `.env`:

```
$ cp .env.example .env
$ vim .env
```

- `CKAN_SITE_URL`: URL del portal de datos
- `CKAN_API_TOKEN`: API token del usuario

---

## Uso

Revise y modifique el ejemplo presente en la función `main` en el archivo `main.py`.

```
(default)$ python main.py
```

Los campos definidos en el modelo [`Dataset`](models.py) coinciden con los campos especificados en la [documentación de CKAN](http://docs.ckan.org/en/2.9/api/index.html#ckan.logic.action.create.package_create)