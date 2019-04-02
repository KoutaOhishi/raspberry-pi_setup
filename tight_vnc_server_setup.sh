#! bin/bash

#tightvncserver
sudo apt-get install openssh-server
sudo apt-get install tightvncserver
vncserver :1 -geometry 1440x900 -depth 24
sudo cp ./vncserver@.service /etc/systemd/system/
sudo systemctl daemon-reload 
sudo systemctl enable vncserver@1.service
