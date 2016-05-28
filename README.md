# PDS Graph API Service
## Installation 
The following will be setup in the VM
* [Tyk API Gateway](https://tyk.io/docs/tyk-api-gateway-v-2-0/installation-options-setup/vagrant/)
* MySQL
* PDS Graph API Service (Django App)

*NOTE: Requires [Virtualbox](https://www.virtualbox.org/), [Vagrant](https://www.vagrantup.com/docs/installation/index.html), [Ansible](http://docs.ansible.com/ansible/intro_installation.html).*

* Fork this repository.
* `$ git clone https://github.com/Sunnepah/pdsservice.git`
* `$ cd pdsservice`
* `$ git clone https://github.com/Sunnepah/ansible-role-tyk.git ansible/roles/Sunnepah.tyk` # Change Tyk variables here `ansible/roles/Sunnepah.tyk/var/main.yml` if necessary or leave defaults.
* `$ vagrant up`
* `$ vagrant ssh`
* `$ /opt/tyk-dashboard/install/bootstrap.sh my-tyk-instance.dev` # Note: This step bootstraps Tyk dashboard user, take note of credentials to login.
* `$ cd /vagrant/pdsservice`
* `$ python manage.py runserver 9000`
