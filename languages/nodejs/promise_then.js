Promise.reject()
  .then( () => 99, () => 42 ) // onRejected returns 42 which is wrapped in a resolving Promise
  .then( (s) => s+1, (s) => 'n/a')
  .then( solution => console.log( 'Resolved with ' + solution ) ); // Resolved with 43

Promise.reject()
  .then( () => 99, () => Promise.reject(42) ) // onRejected returns 42 which is wrapped in a rejecting Promise
  .then( (s) => 'n/a', (s) => s+2)
  .then( solution => console.log( 'Resolved with ' + solution ) ); // Resolved with 44
