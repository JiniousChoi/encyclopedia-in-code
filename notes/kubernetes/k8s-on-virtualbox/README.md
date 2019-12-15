# How to configure k8s on VirtualBox

## Step1 - Install VirtualBox on host machine

## Step2 - Install One Ubuntu-Server-18.04-LTS Instance

## Step3 - Configure the instance

### Network Adapters
1. Menu > Host Network Manager > Create vboxnet0 (192.168.99.1/24, DHCP)
1. Host-only Adapter as the 1st ([issue](https://github.com/kubernetes/kubeadm/issues/203))
1. NAT Adapter for Internet Access as the 2nd

### Swap off
- ``` # swapoff -a ```
- comment out all swap entries in /etc/fstab
- ``` rm -rf /swap.img ```

### Install sshd for convenient maintanence
```
# apt-get update && \
  apt-get install -y ssh
```

### Install docker-ce=18.06.1~ce~3-0~ubuntu
```
$ sudo apt update && \
  sudo apt install apt-transport-https \
                   ca-certificates \
                   curl \
                   software-properties-common && \
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  | sudo apt-key add - && \
  sudo add-apt-repository "deb [arch=amd64] \
  https://download.docker.com/linux/ubuntu bionic stable" && \
  sudo apt update && \
  apt-cache policy docker-ce && \
  sudo apt install docker-ce=18.06.1~ce~3-0~ubuntu && \
  sudo systemctl status docker && \
  sudo usermod -aG docker ${USER} && \
  sudo reboot
```

### Install kubeadm, kubelet and kubectl
```
# apt-get update && \
  apt-get install -y apt-transport-https curl && \
  curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg \
  | apt-key add - && \
  echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" >/etc/apt/sources.list.d/kubernetes.list && \
  apt-get update && \
  apt-get install -y kubelet kubeadm kubectl && \
  apt-mark hold kubelet kubeadm kubectl
```

## Step4 - Clone the vm instance for kubemaster

### Full clone and Initialize the MAC address 

### Change hostname
- ``` # hostnamectl set-hostname kubemaster ```
- `preserve_hostname: false` -> `preserve_hostname: true` in /etc/cloud/cloud.cfg

### Assign static ip address in /etc/network/interfaces
```
auto <network-interface-name>
iface <network-interface-name> inet static
address 192.168.99.20
netmask 255.255.255.0
network 192.168.99.1
broadcast 192.168.99.255
```

### Init the k8s master
Save the `kubeadm join` command with token and all for kubenodes setup
```
$ sudo kubeadm init --apiserver-advertise-address=192.168.99.20 --pod-network-cidr=192.168.0.0/16
```

To make kubeadm runnable for normal user
```
$ mkdir -p $HOME/.kube
$ sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
$ sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

Install Pod Network Add-on by Calico
```
$ sudo kubectl apply -f https://docs.projectcalico.org/v3.3/getting-started/kubernetes/installation/hosted/rbac-kdd.yaml
$ sudo kubectl apply -f https://docs.projectcalico.org/v3.3/getting-started/kubernetes/installation/hosted/kubernetes-datastore/calico-networking/1.7/calico.yaml
```

## Step5 - Clone the vm instance for kubenode1
### Full clone and Initialize the MAC address 

### Change hostname
- ``` # hostnamectl set-hostname kubenode1 ```
- `preserve_hostname: false` -> `preserve_hostname: true` in /etc/cloud/cloud.cfg

### Assign static ip address in /etc/network/interfaces
```
auto <network-interface-name>
iface <network-interface-name> inet static
address 192.168.99.21
netmask 255.255.255.0
network 192.168.99.1
broadcast 192.168.99.255
```

### Init the k8s node1
```
# Run the saved `kubeadm join` command. For example,
# kubeadm join 192.168.99.20:6443 --token <placeholder> --discovery-token-ca-cert-hash sha256:<placeholder>
```

## Step 6 - Repeat Step 5 for as many kubenodes as you want

## Step 7 -Finally, you need to see the similar result on kubemaster
```
Every 2.0s: kubectl get nodes -o wide                                                                        kubemaster: Thu Nov 15 23:27:01 2018

NAME         STATUS   ROLES    AGE   VERSION   INTERNAL-IP     EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME
kubemaster   Ready    master   16h   v1.12.2   192.168.99.20   <none>        Ubuntu 18.04.1 LTS   4.15.0-39-generic   docker://18.6.1
kubenode1    Ready    <none>   15h   v1.12.2   192.168.99.21   <none>        Ubuntu 18.04.1 LTS   4.15.0-39-generic   docker://18.6.1
kubenode2    Ready    <none>   16h   v1.12.2   192.168.99.22   <none>        Ubuntu 18.04.1 LTS   4.15.0-39-generic   docker://18.6.1
```

## Reference
- https://kubernetes.io/docs/setup/independent/install-kubeadm/
- https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/
- https://medium.com/@KevinHoffman/building-a-kubernetes-cluster-in-virtualbox-with-ubuntu-22cd338846dd
- https://stackoverflow.com/questions/51857953/kubectl-port-forward-reports-error-error-upgrading-connection-unable-to-upgra
- https://github.com/kubernetes/kubeadm/issues/203
- https://askubuntu.com/questions/935569/how-to-completely-uninstall-docker
- https://docs.docker.com/install/linux/docker-ce/ubuntu/
