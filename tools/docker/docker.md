## Docker Commands

- start a container and attach to a terminal
  - `docker run -it <image> bash`
- detach the tty without exiting the shell
  - hit the escape sequence `<Ctrl+p> and then <Ctrl+q>`
- attach back to the container again
  - `docker attach <container_name>`
- remove all dontainers in an elegant way
  - ``` docker rm `docker ps --no-trunc -aq` ```
- remove all images
  - ``` docker rmi `docker ps --no-trunc -aq` ```
- override entrypoint and attach to a terminal
  - ``` docker run --rm -it --entrypoint sh bigjin0/ansible-playbook-player ```
- [run a container in background. alive!](https://stackoverflow.com/a/30209974)
  - as-was: `docker run -d --name alpine-d alpine tail -f /dev/null`
  - as-now: `docker run -d -t --name alpine-d alpine`
  - to attach to the terminal of the container in background:
    `docker exec -it alpine-d sh`
- send a single command to a container
  - `docker exec <container_id> command arg1 arg2 ..`
- mount volume between host machine and docker container
  - `$ docker run --rm -d --name mongo34 -v /data:/data/db mongo:3.4`


## [Pushing and Pulling to and from Docker Hub](https://ropenscilabs.github.io/r-docker-tutorial/04-Dockerhub.html)

1. Sign-in to docker hub and create a public repository
1. Create Dockerfile
1. `docker build --tag username/servername .`
1. `docker login`
1. `docker push username/servername`


## Restore Dockerfile from History of [a Docker Image](https://hub.docker.com/r/bigjin0/ansible-control-machine/)

#### Save history of an docker image as [Dockerfile.in](./Dockerfile.in)

1. `docker history --format "{{.CreatedBy}}" --no-trunc <dockerimage> | tee Dockerfile.in`

#### Touch up the [Dockerfile.in](./Dockerfile.in) to get a working [Dockerfile.out](./Dockerfile.out)

1. relocate ENV commands atop (just in case it's used in CMD command later in this Dockerfile)
1. and then CMD commands
1. remove rubbish lines (e.g. ADD file:6ee19b92d5cb1bf143947fe2e2481cb3b353d42e1e54888a8ba48c03dd4155f2 in /)
1. remove /bin/sh -c #(nop) prefixes


## Install Docker

Maybe the way to install docker on any distributions is using [docker-install project](https://github.com/docker/docker-install)

#### [on Ubuntu 18.04 LTS](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)

```
$ sudo apt update && \
  sudo apt install apt-transport-https ca-certificates curl software-properties-common && \
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - && \
  sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable" && \
  sudo apt update && \
  sudo apt install docker-ce && \
  sudo systemctl status docker && \
  sudo usermod -aG docker $USER && \
  sudo docker info
```

#### [on Ubuntu 14.04 LTS or 16.04 LTS](https://docs.docker.com/cs-engine/1.12/)

```
$ sudo apt-get update && \
  # Install packages to allow apt to use a repository over HTTPS: \
  sudo apt-get install -y --no-install-recommends \
                       apt-transport-https \
                       curl \
                       software-properties-common && \
  # Optionally, install additional kernel modules to add AUFS support. \
  sudo apt-get install -y --no-install-recommends \
                       linux-image-extra-$(uname -r) \
                       linux-image-extra-virtual && \
  # If the key server below does not respond, try `pgp.mit.edu` or `keyserver.ubuntu.com` \
  curl -fsSL 'https://sks-keyservers.net/pks/lookup?op=get&search=0xee6d536cf7dc86e2d7d56f59a178ac6c6238f52e' | sudo apt-key add - && \
  sudo add-apt-repository "deb https://packages.docker.com/1.13/apt/repo/ ubuntu-$(lsb_release -cs) main" && \
  sudo apt-get update && \
  sudo apt-get -y install docker-engine && \
  sudo docker info && \
  sudo usermod -a -G docker $USER
```

#### [Docker Compose on Linux](https://docs.docker.com/compose/install/#install-compose)
```
$ sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
```


## Install Docker Composer

```
$ sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose
```


## How to checkout a previous commit (on a new tag)

```
$ docker pull ubuntu
$ docker run --rm -dt --name ubuntu ubuntu
$ docker exec ubuntu touch jinchoi
$ docker commit -m "add a file" -a "jinchoiseoul@gmail.com" ubuntu ubuntu:test
$ docker images | grep ubuntu
ubuntu                          test                  51509821b96e        16 seconds ago      83.5MB
ubuntu                          latest                735f80812f90        12 days ago         83.5MB
```
```
$ docker history ubuntu:test
IMAGE               CREATED              CREATED BY                                      SIZE                COMMENT
51509821b96e        About a minute ago   /bin/bash                                       0B                  add a file
735f80812f90        12 days ago          /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B                  
<missing>           12 days ago          /bin/sh -c mkdir -p /run/systemd && echo 'do…   7B                  
<missing>           12 days ago          /bin/sh -c sed -i 's/^#\s*\(deb.*universe\)$…   2.76kB              
<missing>           12 days ago          /bin/sh -c rm -rf /var/lib/apt/lists/*          0B                  
<missing>           12 days ago          /bin/sh -c set -xe   && echo '#!/bin/sh' > /…   745B                
<missing>           12 days ago          /bin/sh -c #(nop) ADD file:4bb62bb0587406855…   83.5MB 
```
```
$ docker tag 735f80812f90 ubuntu:original
$ docker images | grep ubuntu
ubuntu                          test                  51509821b96e        2 minutes ago       83.5MB
ubuntu                          latest                735f80812f90        12 days ago         83.5MB
ubuntu                          original              735f80812f90        12 days ago         83.5MB
```


## [Where is docker daemon log?](https://stackoverflow.com/a/30970134)

- Ubuntu (new using systemd ) - sudo journalctl -fu docker.service
- Ubuntu (old using upstart ) - /var/log/upstart/docker.log
- Boot2Docker - /var/log/docker.log
- Debian GNU/Linux - /var/log/daemon.log
- CentOS - /var/log/daemon.log | grep docker
- CoreOS - journalctl -u docker.service
- Fedora - journalctl -u docker.service
- Red Hat Enterprise Linux Server - /var/log/messages | grep docker
- OpenSuSE - journalctl -u docker.service
- OSX - ~/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/log/d‌​ocker.log
- Windows - Get-EventLog -LogName Application -Source Docker -After (Get-Date).AddMinutes(-5) | Sort-Object Time, as mentioned here.


## Troubleshooting

#### [[MacOS] Cannot connect to the internet from your Docker containers?](https://odino.org/cannot-connect-to-the-internet-from-your-docker-containers)

1. login as root
1. `printf '# Docker Upstart and SysVinit configuration file\n\n# Use DOCKER_OPTS to modify the daemon startup options.\nDOCKER_OPTS="--dns 208.67.222.222 --dns 208.67.220.220"' > /etc/defaults/docker`
1. restart docker
   - (for mae) `killall Docker && open /Applications/Docker.app`
   - (for ubuntu) /etc/init.d/docker restart
   - (for centos) service docker restart

#### [MacOS] Cannot reach from host to containers and vice versa
- [docker-tuntap-osx](https://github.com/AlmirKadric-Published/docker-tuntap-osx)
- [docker-mac-network](https://github.com/wojas/docker-mac-network)

#### [[Ubuntu Container] Cannot use man-db](https://github.com/tianon/docker-brew-ubuntu-core/issues/122)
  ```
  # Do not exclude man pages & other documentation
  RUN rm /etc/dpkg/dpkg.cfg.d/excludes
  # Reinstall all currently installed packages in order to get the man pages back
  RUN apt-get update && \
      dpkg -l | grep ^ii | cut -d' ' -f3 | xargs apt-get install -y --reinstall && \
      rm -r /var/lib/apt/lists/*
  ```

## reference

- http://longbe00.blogspot.com/2015/03/docker_98.html
