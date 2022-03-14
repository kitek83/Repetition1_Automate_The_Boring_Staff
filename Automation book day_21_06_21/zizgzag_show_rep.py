import sys
import time

indent = 0
indentIncreasing = True
while True:
    print(' ' * indent, end='')
    print('***********')
    time.sleep(0.1)
    try:
      if indentIncreasing:
        indent += 1
        if indent == 20:
            indentIncreasing = False
      else:
        indent -= 1
        if indent == 0:
            indentIncreasing = True
    
    except KeyboardInterrupt:
        sys.exit()