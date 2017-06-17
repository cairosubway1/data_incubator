# Data Incubator

[![Build Status](https://travis-ci.org/cairosubway1/data_incubator.svg?branch=master)](https://travis-ci.org/cairosubway1/data_incubator)

## Local Development Instructions

1.  `git clone`  the application to your local directory.
2.  If you run Ubuntu and want to run the install script, make the script executable with `chmod +x script.sh`.  

The script will:

1.  Install the Heroku Toolbelt, 
2.  Install the Travis CI command line client
3.  Install pip3
4.  Install the application's dependencies from `requirements.txt`
5.  Run the test(s) locally
6.  Start the application with Flask's built-in webserver

## Set Up a CI/CD Pipeline with Travis CI and Heroku

1.  Create a repo for the app in your GitHub account.
2.  Push the app to your new repo
3.  Create an account in Travis CI with your GitHub account.  The `travis.yml` file configures the Travis settings.
4.  Create an account with Heroku.
5.  Create an application in your Heroku account for the app.
6.  Configure your `travis.yml` file to deploy to the Heroku app.
