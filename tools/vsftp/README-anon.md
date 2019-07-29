## /etc/vsftpd.conf for anonymous users

```bash
$ sudo mkdir -p /srv/ftp/upload/
$ sudo chown -R ftp:ftp /srv/
$ sudo chmod 0555 /srv/ftp/
$ sudo chmod 0777 /srv/ftp/upload/
```
