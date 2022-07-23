# Requisitos-Previos

Installar python 3.8 o superior en to computadora:

* Windows: https://www.python.org/downloads/release/python-395/
* Mac OS X: https://www.python.org/downloads/release/python-395/
* Linux: Porfavor mire a lost documentos de tu distro (on Debian/Ubuntu `sudo apt get install python3` esto deberia funcionar)

Install a pip:

Descargar este scrip: https://bootstrap.pypa.io/get-pip.py

Correr (Quizas vas a necesitar a specificar la version de `python3` si tambien tienes a `python2` instalado)

```sh
$ python get-pip.py
```

Instalar git:

https://git-scm.com/downloads

Instalar [virtualenv](https://rukbottoland.com/blog/tutorial-de-python-virtualenv/)

```sh
  $ pip install virtualenv
```

# Descargar pb-exercises requisitos

```sh
    $ git clone https://github.com/jimmysong/pb-exercises
    $ cd pb-exercises
    $ virtualenv -p python3 .venv
```

Linux/OSX:

```sh
    $ . .venv/bin/activate
    (.venv) $ pip install -r requirements.txt
```
Windows:
```sh
    > .venv\Scripts\activate.bat
    > pip install -r requirements.txt
```

# Correr [jupyter notebook](https://www.ikkaro.com/jupyter-notebook/)
```sh
    (.venv) $ jupyter notebook
```
