## Multiple environment setup

1. Create a settings module in the project(myshop) directory.
2. Move the ```settings.py``` file to the module and rename it to ```base.py```.
3. Create ```local.py``` for the local enviroment settings and ```prod.py``` for the production environment settings.

Update the ```BASE_DIR``` configuration in the ```base.py``` file to point to the parent directory.

## Setting up uWSGI application server
1. Install pre-requisite.
```
apt install build-essential
``` 

2. Install uWSGI using pip.
```
pip install uwsgi
```

3. Create a folder named ```config``` and a uwsgi configuration file using the following template.

```
[uwsgi]
# variables
projectname = name of the django project (myshop)
base = absolute path to the django project (/home/projects/myshop)

# configuration
master = enable master process (true)
virtualenv = path to the virtual environment (/home/env/(%projectname)
chdir = path to the project directory (%base)
env = DJANGO_SETTINGS_MODULE=settings for the production environment (DJANGO_SETTINGS_MODULE=%(projectname).settings.pro)
module = the application callable in the wsgi (%(projectname).wsgi:application)
socket = UNIX/TCP socker to bind the server (/tmp/%(projectname).sock)
chmod-socket = file permissions to apply to socket file (666)
```

4. Run the command as follows in order to launch the application using production configurations.
```
$ uwsgi --ini config/uwsgi.ini
```

## setting up NGINX

1. Install nginx
```
$ sudo apt install nginx
```

2. Run the following command to activate the webserver:
```
$ sudo nginx
```

3. Create the webserver configuration file ```nginx.conf``` and place in the ```config``` project folder. Use the template below:
```
upstream myshop {
    server  unix:///tmp/myshop.sock;
}

server {
    listen  8888;
    server_name localhost;
    access_log  off;
    error_log   /tmp/nginx_error.log;

    location / {
        include /etc/nginx/uwsgi_params;
        uwsgi_pass  myshop;
    }

    location /static/ {
        alias /home/shadowfox/projects/myshop/myshop/static/;
    }

    location /media/ {
        alias /home/shadowfox/projects/myshop/myshop/media/;
    }
}
```

The configurations are several blocks, namely:
1. upstream: points to the socket created by uWSGI
2. server:
    * **listen:** port the web server should listen
    * **server_name:** domain name that the web server will serve requests for
    * **access_log:** directive to store access logs
    * **error_log:** directive on where to store access logs
    * **location /:** default uWSGI NGINX configurations
    * **location /static/:** corresponds to the path of **STATIC_URL**
    * **location /media/:** corresponds to the path of **MEDIA_URL**
    
3. Locate the default ```nginx.conf``` file and add the following line of configuration to the ```header``` block:
```
include /home/projects/myshop/myshop/config/nginx.conf;
```

4. Reload nginx to effect the changes using the following command:
```
$ sudo nginx -s reload
```

5. Add the appropriate domain name to the ```ALLOWED_HOSTS``` configuration in the ```prod.py``` settings file

- All products
- Category products X
- product detail view X
- shopping cart view X
- checkout view X
- payment view
- payment confirmation/notification page
- 500 view X
- 400 view X

Testing
- accounts
    - signals(update_user_profile)
    - views(register,account_profile,account_orders, account_order_details)
- cart
    - views(cart_add, cart_remove, cart_details)
    - cart(TODO research testing of classes)
- coupon
    - views(coupon_apply)
- orders
    - views(ord_admin_pdf)
    - forms(OrderComplaintForm: clean_order_id)
    - signals(save_create_order_id)
- payment
    - views(payment_process)
    - tasks (payment_completed)
- shop
    - forms(ProductImageFormset(clean))

# Remember to to check for template tags and URLs to test
