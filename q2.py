
# ******************************
# Make your Code
ilist=[]
while True:
  uinput = input('Enter input: ')
  ilist.append(uinput)
  if uinput == 'stop':
    break
  if uinput == 'STOP':
    break
  shortest = ilist[0]
  longest = ilist[0]
  for i in ilist:
    if len(i) < len(shortest):
      shortest = i
    if len(i) > len(longest):
      longest = i
print(longest, shortest)
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
