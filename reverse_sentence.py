'''
Sentence Reverse
You are given an array of characters arr that consists of sequences of characters separated by space characters. Each space-delimited sequence of characters defines a word.

Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.

Explain your solution and analyze its time and space complexities.

Example:

input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]
Constraints:

[time limit] 5000ms

[input] array.character arr

0 ≤ arr.length ≤ 100
[output] array.character

'''
import unittest

def reverse_words(arr):
  reversed_result = []
  left = len(arr) - 1
  right = len(arr) 
  print(left, right)
  while(right >= 0):
    while( left >=0 and  arr[left] != ' '):
      left -= 1
    i = left +1
    while i < len(arr) and i <= right:
      reversed_result.append(arr[i])  
      i+=1
    if left >= 0and arr[left] == ' ':
      reversed_result.append(' ')  
    
    left = left - 1
    right = left 
  print(left,right)
  return reversed_result 

class MyFunctionTests(unittest.TestCase):
    def test_multi_words(self):
        result = reverse_words([ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ])
        self.assertEqual(result, [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ])

    def test_all_spaces(self):
        result = reverse_words([" "," "])
        self.assertEqual(result, [" "," "])

    def test_all_spaces(self):
        result = reverse_words( ["h","e","l","l","o"] )
        self.assertEqual(result,  ["h","e","l","l","o"] )
       

if __name__ == '__main__':
    unittest.main()
