function chunkArrayInGroups(arr, size) {
    // console.log({ arr, size });

    // (1) Use slice() to extract a shallow copy of portions
    // of the given 'arr' based on the given 'size'.

    const new_2d_arr = [];

    for (let i = 0; i < arr.length; i += size) {
        let new_group = arr.slice(i, i + size)
        new_2d_arr.push(new_group);
    };
    console.log({ new_2d_arr });
    return new_2d_arr;
};

chunkArrayInGroups(["a", "b", "c", "d"], 2);        // [["a", "b"], ["c", "d"]]
chunkArrayInGroups([0, 1, 2, 3, 4, 5], 3);          // [[0, 1, 2], [3, 4, 5]]
chunkArrayInGroups([0, 1, 2, 3, 4, 5], 2);          // [[0, 1], [2, 3], [4, 5]]
chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6], 3);       // [[0, 1, 2], [3, 4, 5], [6]]