I am trying to learn reduce function in CouchDB with examples online.

reference: http://www.bitsbythepound.com/writing-a-reduce-function-in-couchdb-370/

# view 만들기

## design doc: _design/db

## index name: stats

## 맵 함수

```
function(doc){
        if( typeof(doc.name) === 'string'
         && typeof(doc.score) === 'number' ) { 
          emit(doc.name, doc.score);
        };  
```

## Custom Reduce Fn

```
function(keys,values,rereduce){
        if( rereduce ) {
          var result = {
            topScore: values[0].topScore
            ,bottomScore: values[0].bottomScore
            ,sum: values[0].sum
            ,count: values[0].count
          };
          
          for(var i=1,e=values.length; i<e; ++i) {
            result.sum = result.sum + values[i].sum;
            result.count = result.count + values[i].count;
      
            if( result.topScore < values[i].topScore ) {
              result.topScore = values[i].topScore;
            };
            if( result.bottomScore > values[i].bottomScore ) {
              result.bottomScore = values[i].bottomScore;
            };
          };
          
          result.mean = (result.sum / result.count);
        
          log('rereduce keys:'+toJSON(keys)+' values:'+toJSON(values)+' result:'+toJSON(result));
        
          return result;
        };
        
        // Non-rereduce case
        var result = {
          topScore: values[0]
          ,bottomScore: values[0]
          ,sum: values[0]
          ,count: 1
        };
        
        for(var i=1,e=keys.length; i<e; ++i) {
          result.sum = result.sum + values[i];
          result.count = result.count + 1;
          
          if( result.topScore < values[i] ) {
            result.topScore = values[i];
          };
          if( result.bottomScore > values[i] ) {
            result.bottomScore = values[i];
          };
        };
        
        result.mean = (result.sum / result.count);
        
        log('reduce keys:'+toJSON(keys)+' values:'+toJSON(values)+' result:'+toJSON(result));
        
        return result;
      }
```

# Load Documents

```bash
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Alicia","score":85}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Beth","score":87}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Carmen","score":58}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Dalida","score":62}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Elizabeth","score":71}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Fiona","score":75}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Gertrude","score":94}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Halle","score":76}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Irene","score":82}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Julia","score":73}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Kim","score":75}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Lynn","score":91}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Mary","score":56}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Nancy","score":66}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Olie","score":80}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Pat","score":69}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Queen","score":89}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Roseline","score":93}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Sally","score":62}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Trudy","score":71}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Una","score":80}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Victoria","score":79}'
curl -X POST http://whisk_admin:some_passw0rd@127.0.0.1:5984/db -H 'Content-Type: application/json' -d '{"name":"Willow","score":68}'
```

# To include reduction
```
curl -X GET http://127.0.0.1:5984/db/_design/db/_view/stats
```

# 동작원리

```
documents:
    {key: jin1, val: 1}
    {key: jin2, val: 2}
    {key: jin3, val: 3}
    {key: jin4, val: 4}
    {key: jin5, val: 5}
    {key: jin6, val: 6}
    {key: jin7, val: 7}
    {key: jin8, val: 8}

reduce by process 1 (for the first 4):
    {key: null, val: {sum:10, cnt:4, max:4, min:1, avg:2.5}}

reduce by process 2 (for the rest):
    {key: null, val: {sum:26, cnt:4, max:8, min:5, avg:6.5}}

re-reduce (= final result)
    {key: null, val: {sum:36, cnt:8, max:8, min:1, avg:4.5}}
```

위 사례에서와 같이, 도큐먼트를 처음 reduce 할때와 reduced를 re-reduce 할떄의 데이터 형식이 다르므로, reduce fn 작성시 분기를 타게 된다. 또한, reduced나 re-reduced나 key값은 무의미해지므로 줄곧 null이 된다.
