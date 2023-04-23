#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

sudo apt-get install nginx
mkdir /data
mkdir /data/web_static
mkdir /data/web_static/releases
mkdir /data/web_static/shared
mkdir /data/web_static/releases/test
touch /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ububtu /data

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    error_page 404 /custom_404.html;
    location = /custom_404.html {
        root /usr/share/nginx/html;
        internal;
    }
    location /redirect_me {
        return 301 https://google.com;
    }
}" > /etc/nginx/sites-available/default

service nginx restart