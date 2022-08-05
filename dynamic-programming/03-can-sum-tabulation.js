// Tabulation

// this version creates empty trailing elements on the table
// the return statement has been modified to show this behavior
const canSum_alvin = (targetSum, numbers) => {
    const table = Array(targetSum + 1).fill(false)
    table[0] = true
    for (let i = 0; i <= targetSum; i++) {
        if (table[i] === true) {
            for (let num of numbers) {
                table[i + num] = true;
            }
        }
    }
    return [table[targetSum], targetSum, table.length]
}
  
// this version does not create empty trailing elements on the table
// the return statement has been modified to show this behavior
const canSum = (targetSum, numbers) => {
    const table = Array(targetSum + 1).fill(false)
    table[0] = true
    for (let i = 0; i <= targetSum; i++) {
        if (table[i] === true) {
            for (let num of numbers) {
                if (i + num <= targetSum) {
                    table[i + num] = true;
                }
            }
        }
    }
    return [table[targetSum], targetSum, table.length]
}
    
console.log(canSum_alvin(7, [2, 3]))  // True
console.log(canSum(7, [2, 3]))  // True

//console.log(canSum(7, [5, 3, 4, 7]))  // True
//console.log(canSum(7, [2, 4]))  // False
//console.log(canSum(8, [2, 3, 5]))  // True
//console.log(canSum(300, [7, 14]))  // False