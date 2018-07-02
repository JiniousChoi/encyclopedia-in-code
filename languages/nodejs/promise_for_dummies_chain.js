/* ES6 */
const isMomHappy = true;

// Promise
const willIGetNewPhone = new Promise(
    (resolve, reject) => { // fat arrow
        if (isMomHappy) {
            const phone = {
                brand: 'Samsung',
                color: 'black'
            };
            resolve(phone);
        } else {
            const reason = new Error('mom is not happy');
            reject(reason);
        }

    }
);

//// 2nd promise
//var showOff = function (phone) {
//    return new Promise(
//       function (resolve, reject) {
//            var message = 'Hey friend, I have a new ' +
//                phone.color + ' ' + phone.brand + ' phone';
//            resolve(message);
//        }
//    );
//};

const showOff = function (phone) {
    const message = 'Hey friend, I have a new ' +
                phone.color + ' ' + phone.brand + ' phone';
    // When a value is simply returned from within a then handler,
    // it will effectively return Promise.resolve(<value returned by whichever handler was called>).
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then
    // return Promise.resolve(message); // this is the same as the following return statement
    // as a callback function of `then` method:
    return message;
};

// call our promise
const askMom = function () {
    willIGetNewPhone
        .then(showOff)
        .then(fulfilled => console.log(fulfilled)) // fat arrow
        .catch(error => console.log(error.message)); // fat arrow
};

askMom();
