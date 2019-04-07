# flask-hair

### How to start 

```
export FLASK_APP=main.py
```
systemd  servise (```/etc/systemd/system/nastekahair.service```)
```
[Unit]
Description=Gunicorn instance to serve nastekahair
After=network.target

[Service]
User=nastekahair
Group=www-data
WorkingDirectory=/var/www/www.nastekahair.kiev.ua
Environment="PATH=/var/www/www.nastekahair.kiev.ua/venv/bin"
ExecStart=/var/www/www.nastekahair.kiev.ua/venv/bin/gunicorn --workers 3 --bind unix:nastekahair.sock -m 007 -b localhost:8002  main:app

[Install]
WantedBy=multi-user.target

```

nginx setups

```
server {
        listen       80;
        server_name  nastekahair.kiev.ua www.nastekahair.kiev.ua;
        return       301 https://www.nastekahair.kiev.ua$request_uri;
}

server {
        listen       443 ssl ;
        server_name  nastekahair.kiev.ua;
        return       301 https://www.nastekahair.kiev.ua$request_uri;
}
server {
#        root /var/www/nastekahair.kiev.ua;
#        index index.html index.htm;
        server_name www.nastekahair.kiev.ua;

        location / {
#                try_files $uri $uri/ =404;
                include proxy_params;
      			proxy_pass http://localhost:8002/;
        }

        listen 443 ssl http2 default_server;
        ssl_certificate /etc/letsencrypt/live/www.nastekahair.kiev.ua/fullchain.pem; 
        ssl_certificate_key /etc/letsencrypt/live/www.nastekahair.kiev.ua/privkey.pem;
        include /etc/letsencrypt/options-ssl-nginx.conf; 
        ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

        gzip on;
        gzip_disable "msie6";
        gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript application/javascript;

#        location ~* ^.+\.(jpg|jpeg|gif|png|ico|css|pdf|ppt|txt|bmp|rtf|js)$ {
#                root /var/www/nastekahair.kiev.ua/; 
#                access_log off; 
#                expires 3d; 
#        }

        location ~ /.well-known {
                root /var/www/html;
                allow all;
        }
}

``` 