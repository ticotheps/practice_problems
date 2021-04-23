function frankenSplice(arr_1, arr_2, n) {
    // Step 1: Store first half of spliced arr_2 in a new var.
    const first_slice = arr_2.slice(0, n);
    console.log({ first_slice });

    // Step 2: Store second half of spliced arr_2 in another var.
    const second_slice = arr_2.slice(n, arr_2.length);
    console.log({ second_slice });

    // Step 3: Create a new var, 'result_arr', to store consolidated array.
    let result_arr = [];

    for (let i = 0; i < first_slice.length; i++) {
        let item = first_slice[i];
        console.log(item);
        result_arr.push(item);
    };

    for (let k = 0; k < arr_1.length; k++) {
        let item = arr_1[k];
        console.log(item);
        result_arr.push(item)
    };

    for (let j = 0; j < second_slice.length; j++) {
        let item = second_slice[j];
        console.log(item);
        result_arr.push(item)
    };

    console.log(result_arr);
    return (result_arr);
};

frankenSplice([1, 2, 3], [4, 5, 6], 1);