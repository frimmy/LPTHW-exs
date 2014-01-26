#This is a README for my first package with a script.

Anyone with python >=2.7 should be able to download this and run the game as 
an executable hello-world. 

I"ll likely reupload this with a different command to run, BUUUT...type in hello-world
and have fun!

Before I forget, here's what I did for exercise 46:

1. Set up my skeleton project.
2. In the setup.py file:
    1. I named my packages after my project
    2. Declared the FrimmyGame package that held the executable's dependencies
    3. For scripts, I specified the location of the script file that users call to run the package
    4. I specified the bin script that users could install in the bin director
3. saved, and used the python setup.py sdist to create a distribution of the package for install
4. Package can be installed by running pip install in any folder. Installs globally, and can be executed from any location in windows.
