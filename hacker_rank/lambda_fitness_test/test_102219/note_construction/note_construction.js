const constructNote = (magazine, note) => {
  // console.log('Magazine =', magazine);
  // console.log('Note =', note);
  let matches = 0;

  for (let i = 0; i < note.length; i++) {
    // console.log(`note[${i}] = ${note[i]}`);
    for (let j = 0; j < magazine.length; j++) {
      // console.log(`magazine[${j}] = ${magazine[j]}`);

      if (note[i] == magazine[j]) {
        // console.log(`We have a match!`);
        matches++;
        // console.log('Matches:', matches);
      }
    }
  }
  // console.log(matches);
  if (matches == note.length) {
    return true;
  } else {
    return false;
  }
};

const magazine_example_1 = ['give', 'me', 'one', 'grand', 'today', 'night'];
const note_example_1 = ['give', 'one', 'grand', 'today'];

const magazine_example_2 = ['dude', 'me', 'where', 'grand', 'today', 'night'];
const note_example_2 = ['dude', 'car', 'where', 'my', 'is'];

console.log(constructNote(magazine_example_1, note_example_1)); // should return true
console.log(constructNote(magazine_example_2, note_example_2)); // should return false
