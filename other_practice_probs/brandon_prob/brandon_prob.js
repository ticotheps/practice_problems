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

//--------------------------------------------------------

//---------------------CALLBACK example-------------------

const userLeft = false;
const userWatchingCatVideo = true;

function watchTutorialCallback(callback, errorCallBack) {
  if (userLeft) {
    errorCallBack({
      name: 'User Left',
      message: ':(',
    });
  } else if (userWatchingCatVideo) {
    errorCallBack({
      name: 'User Watching Cat Video',
      message: 'WebDevSimplified < Cat',
    });
  } else {
    callback('Thumbs up and Subscribe!');
  }
}

watchTutorialCallback(
  message => {
    console.log('Success: ' + message);
  },
  error => {
    console.log(error.name + ' ' + error.message);
  }
);

//--------------------------------------------------------

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
