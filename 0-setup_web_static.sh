#!/usr/bin/env bash
# Update package list
sudo apt-get update

# Install Nginx if not already installed
sudo apt-get -y install nginx

# Allow Nginx HTTP through firewall
sudo ufw allow 'Nginx HTTP'

# Create necessary directories if they don't already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file to test the Nginx configuration
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link, forcefully
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo echo "
server {
    listen 80 default_server;
    server_name localhost;

    location /hbnb_static {
        alias /data/web_static/current;
    }

    location / {
        try_files \$uri \$uri/ =404;
    }
}" | sudo tee /etc/nginx/sites-available/default

echo "web server ready"

# Restart Nginx to apply the changes
sudo systemctl restart nginx
exit 0
