const path = require('path');
const app = require('express')();
const http = require('http').createServer(app);
const io = require('socket.io')(http);
const port = 8000

app.get('/', (req, res) => res.sendFile(__dirname + '/index.html'));

io.on('connection', function(socket){
  console.log('a user connected');
  socket.on('msg', function(msg) {
    console.log('msg: ' + msg);
  });
});

http.listen(port, () => console.log(`listening on *:${port}`))
