# Flask System MVC in Python3 with deploy in WSGI

## 1 Install Virtualenv
- sudo apt-get install python3-virtualenv
  
## 2 Create Virtualenv in /usr/local/ with python 3.7
- virtualenv --python=/usr/bin/python3.7 /usr/local/virtualenv/

## 3 Activate virtualenv
 - Activate: source env/bin/activate

## 4 Go to the project directory and install requirements
- pip freeze > requirements.txt
- pip install -r requirements.txt

## 5 Configure .wsgi file
```python
  #!/usr/bin/python3
  import sys
  import logging
  logging.basicConfig(stream=sys.stderr)
  
  #Place this rude in the folder that will start the __init__.py module that contains the "app" instance
  sys.path.insert(0,"/var/www/webapp/")
  
  #locate in this directory the file "activate_this.py". It is located in the "virtualenv" folder created in step
  activate_this = '/usr/local/virtualenv/bin/activate_this.py'
  
  #Activate the virtual environment, within your project, allowing it to be activated online. Only for python3
  with open(activate_this) as file_:
      exec(file_.read(), dict(__file__=activate_this))
      
  #Llama a "webapp", debido a q esta carpeta ha sido declarada como un "modulo" en flask, al crear e inicializar "app" en la raiz dentro de su directorio.
  from webapp import app as application
  
  #key to forms
  application.secret_key = "any-key"
