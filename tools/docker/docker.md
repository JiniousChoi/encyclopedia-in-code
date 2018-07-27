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


## Troubleshooting

#### [Cannot connect to the internet from your Docker containers?](https://odino.org/cannot-connect-to-the-internet-from-your-docker-containers)

1. login as root
1. `printf '# Docker Upstart and SysVinit configuration file\n\n# Use DOCKER_OPTS to modify the daemon startup options.\nDOCKER_OPTS="--dns 208.67.222.222 --dns 208.67.220.220"' > /etc/defaults/docker`
1. restart docker
   - (for mae) `killall Docker && open /Applications/Docker.app`
   - (for ubuntu) /etc/init.d/docker restart
   - (for centos) service docker restart


## reference

- http://longbe00.blogspot.com/2015/03/docker_98.html
