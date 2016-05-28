# PDS Graph API Service
## Installation

*NOTE: Requires [virtualenv](http://virtualenv.readthedocs.org/en/latest/), [vagrant](https://www.vagrantup.com/docs/installation/index.html),
[Tyk API Gateway](https://tyk.io/docs/tyk-api-gateway-v-2-0/installation-options-setup/vagrant/).*

* Fork this repository.
* `$ git clone https://github.com/Sunnepah/pdsservice.git`
* `$ cd pdsservice`
* `$ git clone https://github.com/Sunnepah/ansible-role-tyk.git ansible/roles/Sunnepah.tyk`
Change Tyk variables if necessary here `ansible/roles/Sunnepah.tyk/var/main.yml` 
* `$ vagrant up`
* `$ vagrant ssh`
* `$ /opt/tyk-dashboard/install/bootstrap.sh tyk-local.com` # To bootstrap Tyk Test-User
* `$ cd /vagrant/pdsservice`
* `$ virtualenv venv`
* `$ pip install -r requirements.txt`
* `$ python manage.py migrate`
* `$ python manage.py runserver`
