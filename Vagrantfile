# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |tyk_virtuoso|

    tyk_virtuoso.vm.hostname = "pds-tyk-virtuoso"
    tyk_virtuoso.vm.box = "hashicorp/precise64"

    # Create a private network, which allows host-only access to the machine
    # using a specific IP.
    tyk_virtuoso.vm.network "private_network", ip: "192.168.33.30"
    tyk_virtuoso.vm.network :forwarded_port, guest: 3000, host: 3001
    tyk_virtuoso.vm.network :forwarded_port, guest: 8080, host: 9530
    tyk_virtuoso.vm.network :forwarded_port, guest: 80, host: 9541

    tyk_virtuoso.vm.provider "virtualbox" do |v|
      v.memory = 4048
      v.cpus = 2
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    end

    tyk_virtuoso.vm.provision "ansible" do |ansible|
       ansible.groups = {
       "dev" => ["default"]
       }
       ansible.playbook = "ansible/vagrant.yml"
    end

end
