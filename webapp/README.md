# Simple Flask MVC Structure Python3

## /----------------- DEPLOY -----------------/

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

#### 8 - Clone this project and locate the ``` webapp ``` file into ```/var/www/webapp.com/ ```

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

#### 10 - In the directory of our project and with virtualenv activated, we install the requirements of our project
``` bash
cd /var/www/webapp.com/webapp
```
``` bash
sudo pip freeze > requirements.txt && sudo pip install requirements.txt
```

#### 11 - Configure app.wsgi file in the ``` /var/www/webapp.com/webapp/app.wsgi ```
``` bash
sudo nano /var/www/webapp.com/webapp/app.wsgi
```
... and copy...
```python
  #!/usr/bin/python3
  import sys
  import logging
  logging.basicConfig(stream=sys.stderr)
  
  #locate the path in the main directory "/var/www/webapp.com/", because the "/var/www/webapp.com/webapp/app.wsgi" file will interpret the "/var/www/webapp.com/webapp/" folder as a module, since the "app" instance is in a "/var/www/webapp.com/webapp/__init__.py" file
  sys.path.insert(0,"/var/www/webapp.com/")
  
  #locate in this directory the file "activate_this.py". It is located in the "/usr/local/virtualenv/bin/" folder created in step 6
  activate_this = '/usr/local/virtualenv/bin/activate_this.py'
  
  #Activate the virtual environment automatically, within your project, allowing it to be activated online. Note: Only for python3
  with open(activate_this) as file_:
      exec(file_.read(), dict(__file__=activate_this))
      
  #import webapp as a module and call the app instance in the
  from webapp import app as application
  
  #key to forms
  application.secret_key = "any-key"
  ```
#### 12 - Restart apache2
``` bash
sudo service apache2 restart
```

#### 13 - If you are working on localhost, you will need to add the domain to the ```/etc/hosts``` file (optional)
``` bash
sudo nano /etc/hosts
```
... it should look like this...
```python
127.0.0.1 localhost
127.0.1.1 oswscript-PC
127.0.0.2 webapp.com
```
#### 14 - Restart apache2
``` bash
sudo service apache2 restart
```

## Special note
- If an error occurs, because your linux operating system does not meet all the requirements to make flask work, or some other internal problem, you can see the apache errors in: ``` /var/www/webapp.com/webapp/error.log ```. This debug option is configured in step 3. Open the file and you can check and resolve any errors that occur.
