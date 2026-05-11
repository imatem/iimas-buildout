# IIMAS Buildout

## Prerrequisitos ✅

- Python 13 🐍
- [uv](https://docs.astral.sh/uv/#installation)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Instalación ⚙️

Decarga el proyecto en tu máquina local:

```shell
git clone https://github.com/imatem/iimas-buildout
```

Entra en el directorio del proyecto

```shell
cd iimas-buildout
```

Crea un archivo con la contraseña inicial del administrador; **no** uses ``admin`` como contraseña en producción.

```shell
echo -e "[buildout]\nlogin = admin\npassword = admin" > secret.cfg
```

Edita el archivo ``secret.cfg`` y agrega las credenciales necesarias para acceder al indice de paquetes locales. Dichas credenciales seran asignadas por el departamento de Informática Académica.

```shell
links-login =
links-password =
```

Crea un enlace simbólico al archivo de configuración de producción. Esta configuración solo utiliza ``local.cfg`` e ignora todos los ``profiles/local_*.cfg``.

```shell
ln -s profiles/local_production.cfg local.cfg
```

### Entorno virtual de Python 🐍

Crear el entorno virtual con Python 3.13 e instalar `pip` en el entorno

```shell
uv venv --python 3.13 --seed .venv
```

Instala las dependencias base

```shell
.venv/bin/pip install -r requirements.txt
```

### Instalación de Plone 🔧

> [!NOTE]
> For Mac users if you use brew
> ```shell
> export LDFLAGS="-L$(brew --prefix zlib)/lib"
> ```

```shell
.venv/bin/buildout
```

> [!IMPORTANT]
> Cada vez que haya una actualización, ejecuta el comando anterior.


### Inicia los servicios ▶️

Inicia el servidor ZEO

```shell
bin/zeoserver start
```

Inicia los clientes de ZEO

```shell
bin/zeoclient1 start
```

### Creación del sitio 🔥

Abre `http://localhost:8080/` en tu navegador para acceder a la página de creación del sitio.

### Detén los servicios ⏹️

Para detener los clientes, ejecuta el siguiente comando

```shell
bin/zeoclient1 stop
```

Para detener el servidor ZEO, ejecuta el siguiente comando

```shell
bin/zeoserver stop
```

### Respaldos 💾

Los siguientes archivos deben incluirse en el backup:

- `Data.fs` (archivo de la base de datos)
- `blobstorage` (directorio de archivos)


```
var/filestorage/Data.fs
```

```
var/blobstorage
```

Para generar un respaldo ejecuta

```
bin/backup
```

los respaldos los pondra en el direcotorio `backup`


### Recuperar desde un respaldo ♻️

```
bin/restore
```
