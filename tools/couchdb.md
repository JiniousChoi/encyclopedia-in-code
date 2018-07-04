#(How to create users via script)[https://wiki.apache.org/couchdb/How_to_create_users_via_script]
```console
$ COUCH=http://admin:passwd@localhost:5984

# create user
$ curl -HContent-Type:application/json -XPUT $COUCH/_users/org.couchdb.user:wubble --data-binary '{"_id": "org.couchdb.user:wubble","name": "wubble","roles": [],"type": "user","password": "tubble"}'
{"ok":true,"id":"org.couchdb.user:wubble","rev":"1-2e5fe1cfee2ab231788f73be8043acb5"}

# user info
$ curl -HContent-Type:application/json http://wubble:tubble@localhost:5984/_users/org.couchdb.user:wubble
{
  "_id": "org.couchdb.user:wubble",
  "_rev": "1-2e5fe1cfee2ab231788f73be8043acb5",
  "name": "wubble",
  "roles": [],
  "type": "user",
  "password_sha": "96ccc474390c8754ffe225b30740b42a2e01c46b",
  "salt": "03f9e0f7e36d3b4c6f83a31c4c51868e"
}

# set roles on user
$ curl -HContent-Type:application/json -XPUT $COUCH/_users/org.couchdb.user:wibble --data-binary '{"_id": "org.couchdb.user:wibble","name": "wibble","roles": ["admin"],"type": "user","password": "tubble"}'
{
  "error": "forbidden",
  "reason": "Only _admin may set roles"
}

# create db
$ curl -X PUT $COUCH/guestbook
{"ok":true}

# update the DB security object
$ curl -X PUT $COUCH/guestbook/_security  \
   -Hcontent-type:application/json \
   --data-binary '{"admins":{"names":[],"roles":[]},"members":{"names":["wibble"],"roles":[]}}'
{"ok":true}
```

