# Bank security console

### Description

Bank security console allows to operate data of bank vault visitors via their passcards, names 
and other required information. The main purpose is to check if visitor suspicious or not, based on visitor's time spent in the vault.

### How to install

This project uses env variables such as website address and passwords. They can be setted up via `settings.py`.
The main ones are `DEBUG`, `DB_HOST`, `DB_PASSWORD`, `SECRET_KEY`, `ALLOWED_HOSTS`. They
respectively affect debugging, database's address and password, secret key and also allowed local hosts.
Turn the `DEBUG` option on to see detailed error pages, enter your host name, password and secret
key to access the site and select the host/domain names that this Django site can serve with `ALLOWED_HOSTS`.

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
