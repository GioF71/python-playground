// this version creates unnecessary trailing elements on the table
// the function has been modified to show this behavior
// the out of bounds operations are logged, logging can be disabled using the last argument 
// the return statement has been modified to show this behavior
const bestSum_alvin = (targetSum, numbers, logging = false) => {
    const table = Array(targetSum + 1).fill(null)
    table[0] = []
    for (let i = 0; i <= targetSum; ++i) {
        if (table[i] !== null) {
            for (let num of numbers) {
                if (i + num > targetSum) {
                    if (logging) {
                        console.log("Out of bounds, writing at position", i + num, "while array size is", targetSum + 1)
                    }
                }
                const combination = [...table[i], num]
                if (!table[i + num] || table[i + num].length > combination.length) {
                    table[i + num] = combination
                }
            }
        }
    }
    return [targetSum/*, table*/, table.length, table[targetSum]]
}

const bestSum = (targetSum, numbers) => {
    const table = Array(targetSum + 1).fill(null)
    table[0] = []
    for (let i = 0; i <= targetSum; ++i) {
        if (table[i] !== null) {
            for (let num of numbers) {
                if (i + num <= targetSum) {
                    const combination = [...table[i], num]
                    if (!table[i + num] || table[i + num].length > combination.length) {
                        table[i + num] = combination
                    }
                }
            }
        }
    }
    return [targetSum/*, table*/, table.length, table[targetSum]]
}

console.log(bestSum_alvin(7, [5,3,4,7], false))  //7
console.log(bestSum_alvin(8, [2,3,5]))          //3,5
console.log(bestSum_alvin(8, [1,4,5]))          //4,4
console.log(bestSum_alvin(100, [1,2,5,25]))     //25,25,25,25

console.log(bestSum(7, [5,3,4,7]))        //7
console.log(bestSum(8, [2,3,5]))          //3,5
console.log(bestSum(8, [1,4,5]))          //4,4
console.log(bestSum(100, [1,2,5,25]))     //25,25,25,25
