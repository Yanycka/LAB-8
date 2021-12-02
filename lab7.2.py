import pylab
from collections import defaultdict

text=input('Your text:')
chars = defaultdict(int)
for char in text:
    chars[char] += 1


xdata=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ydata=[chars['a'], chars['b'], chars['c'], chars['d'], chars['e'], chars['f'], chars['g'], chars['h'], chars['i'], chars['j'], chars['k'], chars['l'], chars['m'], chars['n'], chars['o'], chars['p'], chars['q'], chars['r'], chars['s'], chars['t'], chars['u'], chars['v'], chars['w'], chars['x'], chars['y'], chars['z']]

pylab.bar(xdata, ydata)
pylab.xlabel('Letters', fontsize=15)
pylab.ylabel('Number', fontsize=15)
pylab.xticks(fontsize=8)
pylab.yticks(fontsize=10)
pylab.title('Bar ex.2')
pylab.savefig('Ex2.png', dpi=200)
pylab.show()