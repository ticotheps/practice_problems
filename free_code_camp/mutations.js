function mutation(arr) {
    const str_1 = arr[0].toLowerCase();
    const str_2 = arr[1].toLowerCase();
    // console.log({ str_1, str_2 });

    let is_a_mutation = true;

    let num_of_matches = 0;

    let str_1_chars_obj = {};

    for (let i = 0; i < str_1.length; i++) {
        str_1_chars_obj[`${str_1[i]}`] = false;
    };

    console.log(str_1_chars_obj);

    for (let j = 0; j < str_2.length; j++) {
        if (str_2[j] in str_1_chars_obj) {
            console.log("We have a match!");
            str_1_chars_obj[str_2[j]] = true;
            num_of_matches += 1;
        }
    };

    if (num_of_matches !== str_2.length) {
        is_a_mutation = false;
    };

    console.log({ str_1_chars_obj });
    console.log({ num_of_matches, is_a_mutation });
    return is_a_mutation;
};

mutation(["hello", "hey"]);         // false
mutation(["hello", "Hello"]);         // true