import sys, time 
indent = 0
ii = True

try: 
    while True:
        print(' ' * indent, end='')
        print('**********')
        time.sleep(0.1)
        
        if ii:
            indent+=1
            if indent == 20:
                ii = False
            else:
                indent-=1
                if indent==0:
                    ii = True
except KeyboardInterrupt:
    sys.exit()