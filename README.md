# The IIMAS Buildout

## Quickstart

```shell
git clone https://github.com/imatem/iimas-buildout
```

```shell
cd iimas-buildout
```

Add a file that contains a passwort. Do **not** use ``admin`` as a password in production!

```shell
echo -e "[buildout]\nlogin = admin\npassword = admin" > secret.cfg
```

Add local distributions credentials to ``secret.cfg``

```shell
inks-login =
links-password =
```

Symlink to the file that best fits you local environment. At first that is usually development. Later you can use production or test. This buildout only uses ``local.cfg`` and ignores all ``profiles/local_*.cfg``.

```shell
ln -s profiles/local_production.cfg local.cfg
```

```shell
apt-get install pyenv
```

```shell
apt-get install pyenv-virtualenv
```

```shell
pyenv install 3.13.13
```

setup a virtual environment

```shell
pyenv virtualenv 3.13.13 plone6
pyenv local plone6
```

### Build Plone

```shell
pip install -r requirements.txt
```

> [!NOTE]
> Solo en MaC
> ```shell
> export LDFLAGS="-L$(brew --prefix zlib)/lib"
> ```

```shell
buildout
```

> [!IMPORTANT]
> Siempre que tengamos una actualización hay que ejecutar el comando anterior


Iniciar Zeoserver

```shell
bin/zeoserver start
```

Iniciar clientes

```shell
bin/zeoclient1 start
```

```shell
bin/zeoclient2 start
```

Detener cliente

```shell
bin/zeoclient1 stop
```
