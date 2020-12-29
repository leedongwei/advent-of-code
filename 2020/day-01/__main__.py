import os
import heapq

def main():
  path = os.path.dirname(os.path.abspath(__file__))
  file = open(f"{path}/input.txt", "r")
  content = file.readlines()

  numbers = []
  for line in content:
    numbers.append(int(line))

  # O(n)
  numbers_set = set(numbers)

  part1(numbers)
  part2(numbers, numbers_set)


def part1(numbers_set, target=2020):
  print("\n\nPart 1:")

  # O(n)
  hasNumber = False
  while len(numbers_set) and not hasNumber:
    num1 = numbers_set.pop()
    num2 = target - num1
    hasNumber = num2 in numbers_set

  if not hasNumber:
    print("Failed")
    return

  print(num1, num2)
  print(num1 * num2)


def part2(numbers, numbers_set):
  print("\n\nPart 2:")

  # O(n^2)
  i_1 = 0
  hasNumber = False
  while not hasNumber and i_1 != len(numbers) - 2:
    i_2 = i_1 + 1
    while not hasNumber and i_2 != len(numbers) - 1:
      num1 = numbers[i_1]
      num2 = numbers[i_2]
      num3 = 2020 - num1 - num2
      hasNumber = num3 in numbers_set
      i_2 += 1
    i_1 += 1

  if not hasNumber:
    print("Failed")
    return

  print(num1, num2, num3)
  print(num1 * num2 * num3)


if __name__ == "__main__":
  main()
