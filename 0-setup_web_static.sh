#!/usr/bin/env bash

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    <p>Hello, welcome here.</p>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create or recreate the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_text="server {
    listen 80;
    server_name _;
    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }
    location /redirect_me {
        rewrite ^ https://www.youtube.com permanent;
    }
    error_page 404 /custom_404.html;
    location = /custom_404.html {
        root /usr/share/nginx/html;
        internal;
    }
}"
echo "$config_text" | sudo tee /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

