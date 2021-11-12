#Overview

## 1. Architectural design
Pending refinement..

## 2. Getting Started
Run the management command as follows in order to launch the application using local configurations.
```
$ cd myshop
$ ./manage.py runserver --settings=myshop.settings.local
```

OR (using uWSGI)
```
uwsgi --http :8000 --home /home/shadowfox/envs/shopEnv  --module=myshop.wsgi --env=DJANGO_SETTINGS_MODULE=myshop.settings.local
```
The options are:
* **http**: Option(PORT) for accepting and routing HTTP requests
* **home**: Path to the virtual environment
* **module**: The WSGI module to use
* **env**: The django project settings file to use

## 3. CloudFormation guide

Coming soon...

## 4. References

1. Django by Example
2. Django documentation - Managing static files
3. Django documentation - How to use Django with uWSGI
4. The uWSGI project - Setting up Django and your web server with uWSGI and nginx 

## 5.Deployment guide

Please refer to this [page](Deployment_guide.md) on how to deploy the e-commerce platform.

## 6. Training and Consulting
My name is Bonface Thaa, I am a software consultant, engineer and a tech lead. I work on technologies trends that shape the future, particularly in web, data and devops. Need some help with any tools used in this repo? Inbox me @ thaabonface@gmail.com and lets deliver your product!