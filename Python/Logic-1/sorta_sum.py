#Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

#sorta_sum(3, 4) → 7
#sorta_sum(9, 4) → 20
#sorta_sum(10, 11) → 21


def sorta_sum(a, b):
  arr=[10,11,12,13,14,15,16,17,18,19]
  sum = a + b
  for i in range(len(arr)):
    if sum == arr[i]:
      return 20
  return sum
