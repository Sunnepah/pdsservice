# pdsservice

## Installation

*NOTE: Requires [virtualenv](http://virtualenv.readthedocs.org/en/latest/),
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/).*

* Fork this repository.
* `$ git clone  git@github.com:<your username>/pdsservice.git`
* `$ mkvirtualenv pdsservice`
* `$ cd pdsservice/`
* `$ pip install -r requirements-local.txt`
* `$ python manage.py migrate`
* `$ python manage.py runserver`
