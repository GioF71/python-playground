// this version creates unnecessary trailing elements on the table
// the function has been modified to show this behavior
const howSum_alvin = (targetSum, numbers) => {
    const table = Array(targetSum + 1).fill(null)
    table[0] = []

    for (let i = 0; i <= targetSum; ++i) {
        if (table[i] !== null) {
            for (let num of numbers) {
                if (i + num > targetSum) {
                    console.log("Out of bounds, writing at position", i + num, "while array size is", targetSum + 1)
                }
                table[i + num] = [...table[i], num]
            }
        }
    }
    return [table.length, table[targetSum]]
}

// this version does not create unnecessary trailing elements on the table
const howSum = (targetSum, numbers) => {
    const table = Array(targetSum + 1).fill(null)
    table[0] = []

    for (let i = 0; i <= targetSum; ++i) {
        if (table[i] !== null) {
            for (let num of numbers) {
                if (i + num <= targetSum) {
                    table[i + num] = [...table[i], num]
                }
            }
        }
    }
    return [table.length, table[targetSum]]
}

console.log(howSum_alvin(7, [2,3]))        // 3,2,2
console.log(howSum(7, [2,3]))        // 3,2,2


// console.log(howSum(7, [5,3,4,7]))    // 4,3
// console.log(howSum(7, [2,4]))        // Null
// console.log(howSum(8, [2,3,5]))      // 2,2,2,2
// console.log(howSum(300, [7,14]))     // Null