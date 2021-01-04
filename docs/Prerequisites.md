# Prerequisites:

* Installed Ubuntu
* Docker CE & docker-compose, to install them hit next command in terminal and press enter or yes:

```shell
sudo apt-get update;
sudo apt-get -y install apt-transport-https ca-certificates gnupg-agent software-properties-common;
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -;
sudo apt-key fingerprint 0EBFCD88;
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable";
sudo apt-get update;
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose;
```
