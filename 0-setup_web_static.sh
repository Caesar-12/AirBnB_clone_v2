#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

sudo apt-get install nginx
mkdir /data
mkdir /data/web_static
mkdir /data/web_static/releases
mkdir /data/web_static/shared
mkdir /data/web_static/releases/test
touch /data/web_static/releases/test/index.html
ln data/web_static/current /data/web_static/releases/test
chown -R /data ubuntu:ububtu
