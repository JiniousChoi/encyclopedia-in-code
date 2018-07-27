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

## [Pushing and Pulling to and from Docker Hub](https://ropenscilabs.github.io/r-docker-tutorial/04-Dockerhub.html)
1. Sign-in to docker hub and create a public repository
1. Create Dockerfile
1. `docker build --tag username/servername .`
1. `docker login`
1. `docker push username/servername`


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
