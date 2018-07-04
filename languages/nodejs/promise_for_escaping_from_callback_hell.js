// add two numbers remotely using observable

let resultA, resultB, resultC;

function addAsync(num1, num2) {
    // use ES6 fetch API, which return a promise
    return new Promise((resolve, reject) => resolve(num1 + num2))
}

//addAsync(1, 2)
//    .then(success => {
//        resultA = success;
//        return resultA;
//    })
//    .then(success => addAsync(success, 3))
//    .then(success => {
//        resultB = success;
//        return resultB;
//    })
//    .then(success => addAsync(success, 4))
//    .then(success => {
//        resultC = success;
//        return resultC;
//    })
//    .then(success => {
//        console.log('total: ' + success)
//        console.log(resultA, resultB, resultC)
//    });

addAsync(1, 2)
    .then(success => {
        resultA = success;
        return addAsync(success, 3)
    })
    .then(success => {
        resultB = success;
        return addAsync(success, 4)
    })
    .then(success => {
        resultC = success;
        return resultC;
    })
    .then(success => {
        console.log('total: ' + success)
        console.log(resultA, resultB, resultC)
    });
