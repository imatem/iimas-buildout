# IIMAS Buildout

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
> For Mac users
> ```shell
> export LDFLAGS="-L$(brew --prefix zlib)/lib"
> ```

```shell
buildout
```

> [!IMPORTANT]
> Whenever we have an update, we need to run the previous command.


Start Zeoserver

```shell
bin/zeoserver start
```

Start clients

```shell
bin/zeoclient1 start
```

```shell
bin/zeoclient2 start
```

Stop clients

```shell
bin/zeoclient1 stop
```
