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
  sys.path.insert(0,"/var/www/oswflask.com/")

  activate_this = '/usr/local/virtualenv/bin/activate_this.py'
  with open(activate_this) as file_:
      exec(file_.read(), dict(__file__=activate_this))

  from webapp import app as application
  application.secret_key = "oswaldo"


