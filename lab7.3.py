import pylab
from collections import defaultdict

text=input('Your text:')
chars = defaultdict(int)
for char in text:
    chars[char] += 1

xdata=['.', '?', '!', '...']
ydata=[chars['.'], chars['?'], chars['!']]

pylab.bar(xdata, ydata)
pylab.xlabel('Sentences', fontsize=15)
pylab.ylabel('Number', fontsize=15)
pylab.xticks(fontsize=10)
pylab.yticks(fontsize=10)
pylab.title('Bar ex.3')
pylab.savefig('Ex3.png', dpi=200)
pylab.show()