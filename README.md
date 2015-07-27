# Virtual Judge

## Features

- Redis
- Celery
- MongoDB

## Installation

- sudo pip install virtualenvwrapper
- add the following lines to your ~/.bashrc:

```
export WORKON_HOME=~/.virtualenvs
source /usr/bin/virtualenvwrapper.sh
```
- source ~/.bashrc
- git clone https://github.com/Junnplus/Virtual_Judge.git && cd Virtual_Judge
- mkvirtualenv VJ
- pip install -r requirements.txt

## Usage

- python manage.py runserver
- redis-server
- celery -A VJ.libs.tasks:celery worker
