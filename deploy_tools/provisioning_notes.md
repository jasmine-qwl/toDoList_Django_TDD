Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.8
* virtualenv + pip
* Git

eg, on Ubuntu:

	sudo add-apt-repository ppa:deadsnakes/ppa
	sudo apt update
	sudo apt install nginx git python3 python3.8-venv

## Nginx Virtual Host Config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com

## Systemd service

* see gunicorn-systeme.template.service
* replace DOMAIN with, e.g, staging.my-domain.com

## Folder structure:

Assume we have a user account at /home/username

/home/username
|___sites
    |---DOMAIN1
    |	 |-- .env
    |	 |-- db.sqlite3
    |    |-- manage.py etc
    |    |-- static
    |	 |__virtualenv
    |___DOMAIN2
         |-- .env
         |-- db.sqlite3
         |-- etc
