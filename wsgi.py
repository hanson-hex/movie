#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname
from app import app


sys.path.insert(0, abspath(dirname(__file__)))
application = app

"""
建立一个软连接
ln -s /var/www/movie/movie.conf /etc/supervisor/conf.d/movie.conf

ln -s /var/www/movie/movie.nginx /etc/nginx/sites-enabled/movie



➜  ~ cat /etc/supervisor/conf.d/movie.conf

[program:movie]
command=/usr/local/bin/gunicorn wsgi -c gunicorn.config.py
directory=/var/www/movie
autostart=true
autorestart=true




/usr/local/bin/gunicorn wsgi
--bind 0.0.0.0:2002
--pid /tmp/飙泪og.pid
"""