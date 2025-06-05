def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))

def reverse_words(text):
    l = text.split(' ')
    for i in range(len(l)):
        l[i] = l[i][::-1]
    return ' '.join(l)

def reverse_words(text):
  return ' '.join([ word[::-1] for word in text.split(' ')])

def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split(' '))

def reverse_words(text):
  #go for it
  word = ''
  rev_word = ''
  for i in range(0,len(text)):
      if(text[i] != ' '):
          word = word + text[i]
      else:
              rev_word = rev_word + word[::-1] + text[i]
              word = ''
  return(rev_word + word[::-1])

text = ' Кот шел ! '

all_lng = len(text)
cnt=0
res = ''
while cnt < all_lng:
    spc_pos = str.find(text, ' ', cnt)
    if spc_pos == 0:
        res = ' '
    else:
        sub_str = text[cnt:spc_pos]
        for i in range(spc_pos, cnt, -1):
            res += text[i-1]
        res +=' '
    # res +=' '
    cnt = spc_pos + 1
if spc_pos+1 == all_lng:
    res += ' '
print(res)

def number(bus_stops):
    return sum(on - off for on, off in bus_stops)

def pig_it(text):

    return ' '.join(ss[1:] + ss[0] + 'ay' +' ' if ss.isalnum() else ss for ss in str.split(text))
text = 'O tempora o mores !'

def comp(a1, a2):
    return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2)

def comp(array1, array2):
    if array1 and array2:
        return sorted([x*x for x in array1]) == sorted(array2)
    return array1 == array2 == []

from collections import Counter as c
def comp(a1, a2):
    return a1 != None and a2 != None and c(a2) == c( elt**2 for elt in a1 )

a = 'indivisibility'
dc = {}
for vr in a:
    dc[vr] = a.count(vr)
res = dict(sorted(dc.items(), key=lambda item: item[1], reverse=True))
# dict comprehension
res = {k: v for k, v in sorted(dc.items(), key=lambda item: item[1], reverse=True)}
print(res)
resm = max(res.values())
print(resm)
max_itm = [k for k, v in res.items() if k == resm]
print(max_itm)