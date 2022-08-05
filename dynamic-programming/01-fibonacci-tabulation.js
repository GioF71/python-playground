// this version creates empty trailing elements on the table
// the return statement has been modified to show this behavior
const fib_alvin = (n) => {
    const table = Array(n + 1).fill(0)
    table[1] = 1
    for (let i = 0; i <= n; i++) {
        table[i + 1] += table[i]
        table[i + 2] += table[i]
    }
    return [/*table, */table.length, table[n]]
}

// this version does not create empty trailing elements on the table
// the return statement has been modified to show this behavior
const fib = (n) => {
    const table = Array(n + 1).fill(0)
    table[1] = 1
    for (let i = 2; i <= n; i++) {
        table[i] = table[i - 2] + table[i - 1]
    }
    return [/*table, */table.length, table[n]]
}

console.log(fib_alvin(6))  //8
//console.log(fib_alvin(7))  //13
//console.log(fib_alvin(8))  //21
//console.log(fib_alvin(50)) //12586269025

console.log(fib(6))  //8
console.log(fib(7))  //13
console.log(fib(8))  //21
console.log(fib(50)) //12586269025