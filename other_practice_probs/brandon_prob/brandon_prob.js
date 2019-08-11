//---------------------PROMISE example-------------------

// let p = new Promise((resolve, reject) => {
//   let a = 1 + 1;
//   if (a == 2) {
//     resolve('Success!');
//   } else {
//     reject('Failed!');
//   }
// });

// p.then(message => {
//   console.log('This is in the then: ' + message);
// }).catch(message => {
//   console.log('This is in the catch: ' + message);
// });

//---------------------CALLBACK example-------------------

// const userLeft = false;
// const userWatchingCatVideo = false;

// function watchTutorialCallback(callback, errorCallback) {
//   if (userLeft) {
//     errorCallback({
//       name: 'User Left',
//       message: ':(',
//     });
//   } else if (userWatchingCatVideo) {
//     errorCallback({
//       name: 'User Watching Cat Video',
//       message: 'WebDevSimplified < Cat',
//     });
//   } else {
//     callback('Thumbs up and Subscribe!');
//   }
// }

// watchTutorialCallback(
//   message => {
//     console.log('Success: ' + message);
//   },
//   error => {
//     console.log(error.name + ' ' + error.message);
//   }
// );

//------------CALLBACK => PROMISE EXAMPLE---------------
// -copy code from 'watchTutorialCallback()' above
// -remove parameters because Promise will handle that for us
// -replace all instances of 'callback' with 'resolve'
// -replace all instances of 'errorCall

// function watchTutorialPromise() {
//   return new Promise((resolve, reject) => {
//     if (userLeft) {
//       reject({
//         name: 'User Left',
//         message: ':(',
//       });
//     } else if (userWatchingCatVideo) {
//       reject({
//         name: 'User Watching Cat Video',
//         message: 'WebDevSimplified < Cat',
//       });
//     } else {
//       resolve('Thumbs up and Subscribe!');
//     }
//   });
// }

// watchTutorialPromise()
//   .then(message => {
//     console.log('Success: ' + message);
//   })
//   .catch(error => {
//     console.log(error.name + ' ' + error.message);
//   });

//------------MULTIPLE PROMISES EXAMPLE---------------

const recordVideoOne = new Promise((resolve, reject) => {
  resolve('Video 1 Recorded');
});

const recordVideoTwo = new Promise((resolve, reject) => {
  resolve('Video 2 Recorded');
});

const recordVideoThree = new Promise((resolve, reject) => {
  resolve('Video 3 Recorded');
});

// Promise.all waits for all of these promises to resolve before doing anything.
// This allows all of these separate processes to happen simultaneously.
// Promise.all([recordVideoOne, recordVideoTwo, recordVideoThree]).then(
//   messages => {
//     console.log(messages);
//   }
// );

// Promise.race is similar to Promise.all, but instead of waiting for ALL the promises
//    to resolve, it only waits for ONE of these promises to resolve before doing anything.
// This still allows all of these separate processes to happen simultaneously, but now they
//    are racing one another to see which one can resolve first.
Promise.race([recordVideoOne, recordVideoTwo, recordVideoThree]).then(
  messages => {
    console.log(messages);
  }
);

//------------Brandon's Code Challenge---------------

// friends = ['Jake', 'Ryan', 'Brandon', 'Jamie', 'Julian', 'Lowell'];

// function fetch_ticos_friends(arr) {
//   return new Promise(function(resolve, reject) {
//     get_friends(arr, function(error, result) {
//       if (error) {
//         reject(error);
//       } else {
//         resolve(result);
//       }
//     });
//   });
// }

// async function get_ticos_async_friends_data(value) {
//   const result = await fetch_ticos_friends(value);
//   return result;
// }

// console.log(get_ticos_async_friends_data());
