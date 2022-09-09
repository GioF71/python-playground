def rangeOfNumbers(startNum, endNum):
    if startNum == endNum: return [startNum]
    vArr = rangeOfNumbers(startNum, endNum - 1)
    result = []
    for v in vArr:
        result.append(v)
    result.append(endNum)
    return result

print(rangeOfNumbers(2, 3))
print(rangeOfNumbers(2, 5))