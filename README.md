# PDS Graph API Service
## Installation

*NOTE: Requires [virtualenv](http://virtualenv.readthedocs.org/en/latest/), [vagrant](https://www.vagrantup.com/docs/installation/index.html),
[Tyk API Gateway](https://tyk.io/docs/tyk-api-gateway-v-2-0/installation-options-setup/vagrant/).*

* Fork this repository.
* `$ git clone git@github.com:<your username>/pdsservice.git`
* `$ vagrant up`
* `$ vagrant ssh`
* `$ cd /vagrant/pdsservice`
* `$ virtualenv venv`
* `$ pip install -r requirements.txt`
* `$ python manage.py migrate`
* `$ python manage.py runserver`
