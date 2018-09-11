# Ansible

## [How to run Ansible without specifying the inventory but the host directly?](https://stackoverflow.com/questions/17188147/how-to-run-ansible-without-specifying-the-inventory-but-the-host-directly)

```
jinchoi $ ansible all -i my.example.com, -a /bin/date [-u username]
my.example.com | SUCCESS | rc=0 >>
Tue Sep 11 08:41:34 KST 2018
```
