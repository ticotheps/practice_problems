function titleCase(str) {
    // console.log({ str });
    
    // Step 1: Convert 'str' into an array of words & store in new var.
    let str_arr = str.split(' ');
    // console.log({str_arr});

    // Step 2: Create a new var to store the modified items from 'str_arr'.
    let new_str_arr = [];

    // Step 3: Iterate thru the array of words...
    for (let i = 0; i < str_arr.length; i++) {
        let word = str_arr[i];
        // console.log({ word });

        let new_word = '';

        for (let j = 0; j < str_arr[i].length; j++) {
            let char = str_arr[i][j];
            // console.log(char);

            let new_char;
            
            // Step 3a: Capitalize the first letter of each word...
            if (j === 0) {
                new_char = char.toUpperCase();
            // Step 3b: Lowercase all other letters in the word...
            } else {
                new_char = char.toLowerCase();
            };

            new_word += new_char;
            // console.log({ new_word});
        };
        new_str_arr.push(new_word);
    };
    // console.log({ new_str_arr });
    
    // Step 4: Join all of the words in the array into a new string.
    let final_str = new_str_arr.join(' ');
    // console.log({ final_str });

    return final_str;
};

titleCase("I'm a little tea pot")