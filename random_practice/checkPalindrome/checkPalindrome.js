const exampleString1 = 'Dad';
const exampleString2 = 'aba';
const exampleString3 = 'Dad:Tic!';
const exampleString4 = 'rotor';
const exampleString5 = '1009001';
const exampleString6 = '%@#@%';

function checkPalindrome(string) {
  console.time('checkPalindrome');
  console.log(string);
  console.timeEnd('checkPalindrome');
}

checkPalindrome(exampleString1);
checkPalindrome(exampleString2);
checkPalindrome(exampleString3);
checkPalindrome(exampleString4);
checkPalindrome(exampleString5);
checkPalindrome(exampleString6);
