# 1.
```
kubectl apply -f redis-master-deployment.yaml
```

# 2.
This manifest file creates a Service named redis-master with a set of labels that match the labels previously defined, so the Service routes network traffic to the Redis master Pod.

```
kubectl apply -f redis-master-service.yaml
```
```
$ kubectl describe svc/redis-master
Name:              redis-master
Namespace:         default
Labels:            app=redis
                   role=master
                   tier=backend
Annotations:       kubectl.kubernetes.io/last-applied-configuration={"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"labels":{"app":"redis","role":"master","tier":"backend"},"name":"redis-master","names...
Selector:          app=redis,role=master,tier=backend
Type:              ClusterIP
IP:                10.103.42.179
Port:              <unset>  6379/TCP
TargetPort:        6379/TCP
Endpoints:         172.17.0.6:6379
Session Affinity:  None
Events:            <none>
```
