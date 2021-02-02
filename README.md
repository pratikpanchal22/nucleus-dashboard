# Nucleus-Dashboard
Web application to manage cluster of Nucleus nodes


### Run application within virtual environment (recomended):
```
cd ~/nucleus-dashboard
source venv/bin/activate
python3 nucleus-dashboard/nucleus-dashboard.py
```
   
### Collect required pacakges in requirements.txt:
```
pip3 freeze > requirements.txt
```
   
### Exit virtual environment:
```
deactivate
```
   
### Install verified packages from virtual environment to main environment:
```
user@phroneo:~/nucleus-dashboard$ pip3 install -r requirements.txt 
```

It will install all the missing pacakges:
```
Collecting click==7.1.2
  Using cached click-7.1.2-py2.py3-none-any.whl (82 kB)
Requirement already satisfied: Flask==1.1.2 in /home/user/.local/lib/python3.8/site-packages (from -r requirements.txt (line 2)) (1.1.2)
Collecting Flask-MySQL==1.5.1
  Using cached Flask_MySQL-1.5.1-py2.py3-none-any.whl (3.8 kB)
Requirement already satisfied: itsdangerous==1.1.0 in /home/user/.local/lib/python3.8/site-packages (from -r requirements.txt (line 4)) (1.1.0)
Collecting Jinja2==2.11.2
  Using cached Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
Collecting MarkupSafe==1.1.1
  Downloading MarkupSafe-1.1.1-cp38-cp38-manylinux2010_x86_64.whl (32 kB)
Collecting PyMySQL==0.10.1
  Using cached PyMySQL-0.10.1-py2.py3-none-any.whl (47 kB)
Requirement already satisfied: Werkzeug==1.0.1 in /home/user/.local/lib/python3.8/site-packages (from -r requirements.txt (line 8)) (1.0.1)
Installing collected packages: click, PyMySQL, Flask-MySQL, MarkupSafe, Jinja2
Successfully installed Flask-MySQL-1.5.1 Jinja2-2.11.2 MarkupSafe-1.1.1 PyMySQL-0.10.1 click-7.1.2
```
