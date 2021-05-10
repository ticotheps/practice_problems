function getIndexToIns(arr, num) {
    let index_to_insert = 0;

    // // (1) determine if the array is empty. If it is, return 0.
    // if (!arr.length) {
    //     console.log('\n');
    //     console.log({ arr, num });
    //     console.log({ index_to_insert });
    //     return index_to_insert;
    // };
    
    // (2) if the array is NOT empty...
    if (arr.length >= 1) {
        // (3) sort the array...
        const sorted_arr = arr.sort((a, b) => a - b);

        // (4) ...and iterate through the sorted array to determine where to
        // insert 'num'.
        for (let i = 0; i < sorted_arr.length; i++) {
            // (a) ...if 'num' is LESS THAN the first item in the array,
            // insert it at index 0.
            if (num < sorted_arr[0]) {
                index_to_insert = 0;
            }
            
            // (b) ...if 'num' is GREATER THAN OR EQUAL TO the first item in
            // the array...
            if (num >= sorted_arr[0]) {
                // (i) ...and is ALSO equal to another item in the array, insert
                // it at the index of that item which it is equivalent to.
                if (num === sorted_arr[i]) {
                    index_to_insert = i;
                };

                // (ii) ...and is GREATER THAN the item at index 'i' BUT LESS
                // THAN the item at index 'i+1', insert it at the index of the
                // item at index 'i+1'.
                if (num > sorted_arr[i] && num < sorted_arr[i + 1]) {
                    index_to_insert = i + 1;
                };

                // (iii) ...and is GREATER THAN the item at the index
                // 'sorted_arr.length - 1', insert it at the index of the item
                // at index 'sorted_arr.length - 1'.
                if (num > sorted_arr[sorted_arr.length - 1]) {
                    index_to_insert = sorted_arr.length;
                };
            };
        }
    };
    console.log({ index_to_insert });
    return index_to_insert;
};

getIndexToIns([50, 20, 40, 30, 10], 30);        // 2
getIndexToIns([5, 3, 20, 3], 5);                // 2
getIndexToIns([2, 5, 10], 15)                   // 3
getIndexToIns([], 1);                           // 0
getIndexToIns([3, 10, 5], 3);                   // 0