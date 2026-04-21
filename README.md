# IIMAS Buildout

## Inicio rápido

```shell
git clone https://github.com/imatem/iimas-buildout
```

```shell
cd iimas-buildout
```

Agrega un archivo que contenga una contraseña; **no** uses ``admin`` como contraseña en producción.

```shell
echo -e "[buildout]\nlogin = admin\npassword = admin" > secret.cfg
```

Agrega las credenciales del índice de paquetes local a ``secret.cfg``

```shell
inks-login =
links-password =
```

Symlink to the file that best fits you local environment. At first that is usually development. Later you can use production or test. This buildout only uses ``local.cfg`` and ignores all ``profiles/local_*.cfg``.

Crea un enlace simbólico al archivo de configuración de producción. Esta configuración solo utiliza ``local.cfg`` e ignora todos los ``profiles/local_*.cfg``.

```shell
ln -s profiles/local_production.cfg local.cfg
```

Crea un entorno virtual de Python

```shell
python -m venv .
```

### Instala Plone

```shell
bin/pip install -r requirements.txt
```

> [!NOTE]
> For Mac users
> ```shell
> export LDFLAGS="-L$(brew --prefix zlib)/lib"
> ```

```shell
bin/buildout
```

> [!IMPORTANT]
> Cada vez que haya una actualización, ejecuta el comando anterior.


### Inicia Plone

Inicia el servidor ZEO

```shell
bin/zeoserver start
```

Inicia los clientes de ZEO

```shell
bin/zeoclient1 start
```

Para detener los clientes, ejecuta el siguiente comando

```shell
bin/zeoclient1 stop
```

Para detener el servidor ZEO, ejecuta el siguiente comando

```shell
bin/zeoserver stop
```
