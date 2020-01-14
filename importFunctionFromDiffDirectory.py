# importing a function from different dirrectory

import sys
sys.path.append('../Desktop')
from rangeFunction import Range


print(Range(4))