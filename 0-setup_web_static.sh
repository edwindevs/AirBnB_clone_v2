#!/usr/bin/env bash
# setting up a web server for static deployment

sudo apt-get -y update
sudo apt-get -y install nginx
mkdir -p /data/web_static/{releases/test,shared}
echo "<html>
        <head></head>
        <body>
                <p>Nobby Test</p>
        </body>
</html>" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i '59i\\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

service nginx restart
