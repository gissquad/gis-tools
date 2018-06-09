# gis-tools
##Control machine:
Install Ansible
```bash
$ sudo apt-get update
$ sudo apt-get install software-properties-common
$ sudo apt-add-repository ppa:ansible/ansible
$ sudo apt-get update
$ sudo apt-get install ansible
```

Generate & copy the ssh keys on taret machine
```bash
ssh-keygen
ssh-copy-id -i ~/.ssh/id_rsa user@ip
```
##Target Machine:
```bash
sudo apt-get update && /usr/bin/apt-get install -y python2.7 python-apt
```

#Run playbooks
Ansible scripts for installation of geoserver, postgis and qgis server on a target machine
```bash
ansible-playbook -i gis-servers x_xxxxx.yml  --ask-sudo-pass
```