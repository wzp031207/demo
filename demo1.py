try:
    f=open('gushi.txt','r')
    e=open('copy.txt','w')
finally:
    try:
        def read():
            f.readlines()
        a=f.readlines()
        print(a)
    finally:
        try:
            import os
            def copy():
                os.copy('gushi.txt','copy.txt')
                os.move('gushi.txt','copy.txt')
            print('复制完毕')
        except Exception as result:
            print(result)