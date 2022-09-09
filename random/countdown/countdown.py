def countdown(n):
  if n < 1: return []
  if n == 1: return [1]
  result = [n] 
  for v in countdown(n - 1):
    result.append(v)
  return result

print(countdown(2))
print(countdown(3))