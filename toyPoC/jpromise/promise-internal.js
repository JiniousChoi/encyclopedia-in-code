new Promise((resolve, reject) => {
 console.log("1");
 resolve(1);
}).then((res) => {
 console.log("2");
 return res+1;
});
console.log("end");

// What's going on?
// expected (no multithreading in Promise): 1 -> 2 -> end
// actual : 1 -> end -> 2 (multi-threading under the hood?!)

