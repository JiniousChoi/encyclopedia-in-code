# ansible playbook upon docker

## setup network and containers

```
$ make all
```

```
6211f94c1758ae208390e604060602604832b02487d9c54f27235553c2dfbb9e
1d9e2661fbf4ef4542f3ab7bccd69686840803d19d3cc40646195e2152dffed9
 * Starting OpenBSD Secure Shell server sshd
   ...done.
bdfde592682b2be3253c37c14c5966f5891760a8923bce1367812d22542df863
fetch http://dl-cdn.alpinelinux.org/alpine/v3.7/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.7/community/x86_64/APKINDEX.tar.gz
v3.7.0-232-gcb703b0b3b [http://dl-cdn.alpinelinux.org/alpine/v3.7/main]
v3.7.0-229-g087f28e29d [http://dl-cdn.alpinelinux.org/alpine/v3.7/community]
OK: 9048 distinct packages available
apk: unrecognized option: y
OK: 106 MiB in 69 packages
Generating public/private rsa key pair.
Created directory '/root/.ssh'.
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:Mv1/ctfQdqTwAsbGZEtMTE9XRecHbAmArSZjXp7HVt0 root@ansible-control-machine
The key's randomart image is:
+---[RSA 2048]----+
|         B+.ooo+*|
|        . Bo .+o.|
|         B ..o .o|
|      +.+ B o . E|
|     oo*S= o o + |
|      .oo.+ . + +|
|         o.  . oo|
|           .. o o|
|            .+ . |
+----[SHA256]-----+
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/root/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
expr: warning: '^ERROR: ': using '^' as the first character
of a basic regular expression is not portable; it is ignored
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh -o 'StrictHostKeyChecking=no' 'root@ansible-node-machine'"
and check to make sure that only the key(s) you wanted were added.

ansible-node-machine | SUCCESS => {
    "changed": false, 
    "ping": "pong"
}

PLAY [test-servers] ************************************************************

TASK [Gathering Facts] *********************************************************
ok: [ansible-node-machine]

TASK [install nginx] ***********************************************************
changed: [ansible-node-machine]

RUNNING HANDLER [start nginx] **************************************************
changed: [ansible-node-machine]

PLAY RECAP *********************************************************************
ansible-node-machine       : ok=3    changed=2    unreachable=0    failed=0   

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
100   612  100   612    0     0   597k      0 --:--:-- --:--:-- --:--:--  597k
```


## cleanup containers

```
$ make clean
```

```
ansible-node-machine
ansible-control-machine
ansible-bridge
```
