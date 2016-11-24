# PDS Graph API Service
## Installation 
The following will be setup in the VM
* [Tyk API Gateway](https://tyk.io/docs/tyk-api-gateway-v-2-0/installation-options-setup/vagrant/)
* MySQL
* PDS Graph API Service (Django App)

*NOTE: Requires [Virtualbox](https://www.virtualbox.org/), [Vagrant](https://www.vagrantup.com/docs/installation/index.html), [Ansible](http://docs.ansible.com/ansible/intro_installation.html),[Virtuoso](https://github.com/openlink/virtuoso-opensource).*

#### Setup Steps.
* `$ git clone --recursive https://github.com/Sunnepah/pdsservice.git`
* `$ cd pdsservice`
* NOTE: If ansible/roles/Sunnepah.tyk is still missing, `git submodule` didn't work, then clone normally in next step.
* `$ git clone https://github.com/Sunnepah/ansible-role-tyk.git ansible/roles/Sunnepah.tyk`
* Change Tyk variables here `ansible/roles/Sunnepah.tyk/var/main.yml` if necessary or leave defaults.
* `$ vagrant up`
* `$ vagrant ssh`
* `$ /opt/tyk-dashboard/install/bootstrap.sh my-tyk-instance.dev` # Note: This step bootstraps Tyk dashboard user, take note of credentials to login.
* add this `192.168.33.30 http://my-tyk-instance.dev` to your `/etc/hosts` file
* Visit [http://my-tyk-instance.dev:3000/](http://my-tyk-instance.dev:3000/) - Follow the instruction on the page to obtain tyk community edition license.
* After obtaining the license and inserting it, the login screen should be displayed, use the user credentials obtained during the user bootstrap step.

#### Run PDS Graph API Service in VM
* `$ cd /vagrant/pdsservice`
* `$ python manage.py runserver 0.0.0.0:9000`

#### TODO
* Serve Django App with uWSGI and Nginx.
