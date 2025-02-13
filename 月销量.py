def append_file(file1,file2):
    with open(file1,'a',encoding='utf-8') as f1, open(file2,'r',encoding='utf-8') as f2:
        f1.write('\n')
        f1.write(f2.read())
append_file("wzp1","wzp2")