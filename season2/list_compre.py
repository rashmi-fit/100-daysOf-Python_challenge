# list comprehension

negative= []
for i in range (1,11):
      negative.append(-i)
print(negative)


new_negative = [ -i for i in range(1,11)]
print(new_negative)

names =['rashmi', 'liti', 'abhi']
# new_list =['r', 'l', 'a'] expected

new_list = []
for name in names:
      new_list.append(name[0])
print(f'new_list: {new_list}')

# using list comprehension
# append karne ki jarurat hi ni hai
new_list2 = [i[0] for i in names]
print(f'new_list2: {new_list2}')


# exercise using list compre
# l = ['abcd','efgh','ijkl']
# write a function to reverse the strings in a list
#  ['dcba','hgfe','lkji']

l = ['abcd','efgh','ijkl']
def reverse_strings(l):
      return[name[::-1] for name in l]

print(f'reverse_strings(l): {reverse_strings(l)}')

def reverse_str(l):
      new_list = []
      for name in l:
            new_list.append(name[::-1])
      return new_list

print(f'reverse_str(l): {reverse_str(l)}')
