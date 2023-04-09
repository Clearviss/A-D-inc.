import sys, time 
indent = 1
ii = True

try: 
    while True:
        print(' ' * indent, end='')
        print("████  █████ █████ █████ █  █  █   █ █████ █████")
        print(' ' * indent, end='')
        print("█   █    █    █   █     █ █   █   █   █   █")     
        print(' ' * indent, end='')
        print("█   █   █     █   ████  ██ █  █   █   █   ████ ") 
        print(' ' * indent, end='')
        print("█   █  █      █   █     █  █  █   █ █ █   █     ")
        print(' ' * indent, end='')
        print("████  █████ █████ █████ █   █ █████ ███   █████ ")
        time.sleep(0.01)
        
        if ii:
            indent+=1
            if indent == 50:
                ii = False
        else:
            indent-=1
            if indent==0:
                ii = True
except KeyboardInterrupt:
    sys.exit()