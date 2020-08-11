#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)

#locate this directory at the root of the file that contains the __init__ with the instance "app"
sys.path.insert(0,"/var/www/webapp/")

#locate in this directory the file "activate_this.py". It is located in the "virtualenv" folder created in step 2
activate_this = '/usr/local/virtualenv/bin/activate_this.py'

#This syntax is for python3. Activate the virtual environment, within your project, allowing it to be activated online
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
    
#Call "webapp", because this folder has been declared as a "module" in flask, when creating and initializing "app" in the root within its directory.
from webapp import app as application

#secret key to forms
application.secret_key = "any-key"
