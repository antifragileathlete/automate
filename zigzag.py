import time, sys
indent = 0
indentIncreasing = True

try:
    while True: # The main programm loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 second

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreasing = False

        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
