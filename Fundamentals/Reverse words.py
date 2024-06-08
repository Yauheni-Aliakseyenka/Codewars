'''
Complete the function that accepts a string parameter,
and reverses each word in the string. All spaces in the string should be retained.
'''

def reverse_words(text):
    new_row = []
    if len(text.split()) > 1:
        space = ' ' * (text.count(' ') // (len(text.split()) - 1))
    else:
        space = ' '
    for i in text.split():
        new_row.append(i[::-1])
    return space.join(new_row)

def reverse_words1(str):
    return ' '.join(s[::-1] for s in str.split(' '))

def reverse_words2(str):
  newStr = []
  for i in str.split(' '):
      newStr.append(i[::-1])
  return ' '.join(newStr)

a = "double  spaced  words"
a1 = 'This is an example!'
print(reverse_words1(a))
b = a.split(' ')
print(b)




