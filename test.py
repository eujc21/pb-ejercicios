from os import chdir
from subprocess import call


for session in range(9):
    chdir("session{}".format(session))
    call("nosetests --with-doctest *.py", shell=True)
    chdir("complete")
    call("nosetests --with-doctest *.py", shell=True)
    chdir("../..")
