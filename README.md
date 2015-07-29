# Virtual Judge

## Features

- Redis
- Celery
- MongoDB

## Installation

- sudo pip install virtualenvwrapper
- add the following lines to your ~/.bashrc:

```shell
if [ -f /usr/local/bin/virtualenvwrapper.sh ]; then
    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh
fi
```
- source ~/.bashrc
- git clone https://github.com/Junnplus/Virtual_Judge.git && cd Virtual_Judge
- mkvirtualenv VJ
- pip install -r requirements.txt

## Usage

- python manage.py runserver
- redis-server
- celery -A VJ.libs.tasks:celery worker -B -l debug

## 

- export VJ_SERVER_NAME="localhost:3000"
- export MAIL_USERNAME="example@sina.cn"
- export MAIL_PASSWORD="password"
