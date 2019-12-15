.SILENT:
.PHONY: all
all: setup ping_test_servers install_nginx health_check

.SILENT:
.PHONY: setup
setup: setup_network setup_node_machine setup_control_machine ping_test_servers

.PHONY: setup_network
setup_network:
	## setup ansible-bridge
	docker network create ansible-bridge || echo "already exists"

.PHONY: setup_node_machine
setup_node_machine:
	## setup ansible-node-machine
	docker run --rm -dt --hostname ansible-node-machine --name ansible-node-machine \
			   --network ansible-bridge bigjin0/ansible-node-machine:0.1
	docker exec ansible-node-machine /bin/sh -c "/etc/init.d/ssh start"
	
.PHONY: setup_control_machine
setup_control_machine:
	## setup ansible-control-machine
	docker run --rm -dt --hostname ansible-control-machine --name ansible-control-machine \
			   --network ansible-bridge bigjin0/ansible-control-machine
	docker exec ansible-control-machine /bin/sh -c "apk update && apk add sshpass -y"
	docker exec ansible-control-machine /bin/sh -c 'ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa'
	docker exec ansible-control-machine \
	   	   /bin/sh -c "sshpass -p root ssh-copy-id -o StrictHostKeyChecking=no root@ansible-node-machine"

	docker exec ansible-control-machine sed -i '1i [test-servers]\nansible-node-machine\n' /etc/ansible/hosts
	docker cp ./nginx.yml ansible-control-machine:/root

.PHONY: ping_test_servers
ping_test_servers:
	docker exec ansible-control-machine ansible -m ping test-servers

.PHONY: install_nginx
install_nginx:
	docker exec ansible-control-machine ansible-playbook /root/nginx.yml

.PHONY: health_check
health_check:
	docker exec ansible-control-machine curl ansible-node-machine


.SILENT:
.PHONY: clean
clean: clean_node_machine clean_control_machine clean_network

.PHONY: clean_node_machine
clean_node_machine:
	docker kill ansible-node-machine || echo "not running"
	
.PHONY: clean_control_machine
clean_control_machine:
	docker kill ansible-control-machine || echo "not running"
	
.PHONY: clean_network
clean_network:
	docker network rm ansible-bridge || echo "removed already"

