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

Symlink to the file that best fits you local environment. At first that is usually development. Later you can use production or test. This buildout only uses ``local.cfg`` and ignores all ``profiles/local_*.cfg``.

```shell
ln -s profiles/local_production.cfg local.cfg
```

setup a virtual environment

```shell
pyenv virtualenv 3.12.13 plone6
pyenv local plone6
```

### Build Plone

```shell
pip install -r requirements.txt
```

MaC Users
```shell
export LDFLAGS="-L$(brew --prefix zlib)/lib"
```

```shell
buildout
```