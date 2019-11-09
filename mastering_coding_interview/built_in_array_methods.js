'ticothepsourinthone'.length; // O(1) built-in method of JavaScript

const nemo = ['nemo'];
const everyone = [
  'dory',
  'bruce',
  'marlin',
  'nemo',
  'gill',
  'bloat',
  'nigel',
  'squirt',
  'darla',
  'hank',
];
const large = new Array(100000).fill('nemo');

// written with a 'for' loop
function findNemo(array) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === 'nemo') {
      console.log('Found NEMO!');
    }
  }
}

findNemo(everyone);

const findNemo2 = array => {
  // using 'forEach()' is the same as a 'for' loop
  array.forEach(fish => {
    if (fish === 'nemo') {
      console.log('Found NEMO!');
    }
  });
};

const findNemo3 = array => {
  for (let fish of array) {
    if (fish === 'nemo') {
      console.log('Found NEMO!');
    }
  }
};

findNemo2(everyone);
findNemo3(everyone);
