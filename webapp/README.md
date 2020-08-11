# Flask System MVC in Python3 with deploy in WSGI

#### 1 - Create in ``` /var/www/ ``` the directory of our project; we will call it "webapp.com"
``` bash 
sudo mkdir /var/www/webapp.com 
```

#### 2 - Create a new site in apache2; we will call it "webapp.com.conf"
``` bash 
sudo nano /etc/apache2/sites-available/webapp.com.conf 
```

#### 3 - In ``` /etc/apache2/sites-available/webapp.com.conf```, we add the following configuration.

```python

<VirtualHost *:80>
    ServerName webapp.com
    ServerAlias www.webapp.com
    ServerAdmin email@email.com
    WSGIScriptAlias / /var/www/webapp.com/webapp/app.wsgi
    <Directory /var/www/webapp.com/webapp/>
                Order allow,deny
                Allow from all
    </Directory>
    Alias /static /var/www/webapp.com/webapp/static

    <Directory /var/www/webapp.com/webapp/static>
      Order allow,deny
      Allow from all
    </Directory>

    ErrorLog /var/www/webapp.com/webapp/error.log
    LogLevel warn
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

  ``` 
 #### 4 - Enabled the new site
``` bash 
sudo a2ensite webapp.com
```

#### 5 - Install Virtualenv
``` bash
sudo apt-get install python3-virtualenv
```
  
#### 6 - Create Virtualenv in ```/usr/local/``` with python 3.7

``` bash
sudo virtualenv --python=/usr/bin/python3.7 /usr/local/virtualenv/
```

#### 7 - Activate virtualenv
``` bash
 source /usr/local/virtualenv/bin/activate
```

#### 8 - Clone this project and locate the ``` webapp ``` file, inside your project in ```/var/www/webapp.com/ ```

#### 9 - Final and correct structure of the project

```
├─ var/         
│     ├─ www/            
│     │     ├─ webapp.com/
│     │     |            ├─ webapp/
│     │     |                    ├─ config/ 
│     │     |                    ├─ controllers/
│     │     |                    ├─ forms/
│     │     |                    ├─ helpers/
│     │     |                    ├─ models/
│     │     |                    ├─ static/
│     │     |                    ├─ templates/
│     │     |                    └─ README.md
│     │     |                    └─ __init__.py
│     │     |                    └─ app.wsgi
│     │     |                    └─ server.py
```

## 4 Go to the project directory and install requirements
- pip freeze > requirements.txt
- pip install -r requirements.txt

## 5 Configure .wsgi file in the project
```python
  #!/usr/bin/python3
  import sys
  import logging
  logging.basicConfig(stream=sys.stderr)
  
  #Place this rude in the folder that will start the __init__.py module that contains the "app" instance
  sys.path.insert(0,"/var/www/webapp/")
  
  #locate in this directory the file "activate_this.py". It is located in the "virtualenv" folder created in step 2
  activate_this = '/usr/local/virtualenv/bin/activate_this.py'
  
  #Activate the virtual environment, within your project, allowing it to be activated online. Only for python3
  with open(activate_this) as file_:
      exec(file_.read(), dict(__file__=activate_this))
      
  #Llama a "webapp", debido a q esta carpeta ha sido declarada como un "modulo" en flask, al crear e inicializar "app" en la raiz dentro de su directorio.
  from webapp import app as application
  
  #key to forms
  application.secret_key = "any-key"
  ```
