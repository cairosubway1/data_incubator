#!/bin/sh

#Installs Heroku command line client
wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh -y

#Installs dependencies for Travis CI command line client
sudo apt-get install python-software-properties -y
sudo apt-add-repository ppa:brightbox/ruby-ng -y
sudo apt-get update
sudo apt-get install ruby2.1 ruby-switch -y
sudo ruby-switch --set ruby2.1 -y

#Installs application dependencies
pip3 install -r requirements.txt

#Runs tests locally
python3 tests.py

#Runs application locally
python3 app.py


