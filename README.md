# PDS Graph API Service
## Installation

*NOTE: Requires [virtualenv](http://virtualenv.readthedocs.org/en/latest/), [vagrant](https://www.vagrantup.com/docs/installation/index.html),
[Tyk API Gateway](https://tyk.io/docs/tyk-api-gateway-v-2-0/installation-options-setup/vagrant/).*

* Fork this repository.
* `$ git clone https://github.com/Sunnepah/pdsservice.git`
* `$ cd pdsservice`
* `$ git clone https://github.com/Sunnepah/ansible-role-tyk.git ansible/roles/Sunnepah.tyk` # Change Tyk variables here `ansible/roles/Sunnepah.tyk/var/main.yml` especially `license_key` Go to [Tyk License key](https://tyk.io/tyk-professional-licenses/) and Check for `Tyk Professional Edition : Startup License
Use Professional Edition for FREE!`
* `$ vagrant up`
* `$ vagrant ssh`
* `$ /opt/tyk-dashboard/install/bootstrap.sh tyk-local.com` # Note: This step bootstraps Tyk dashboard user, take note of credentials to login.
* `$ cd /vagrant/pdsservice`
* `$ python manage.py runserver 9000`
