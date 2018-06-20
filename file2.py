def reduce(fromName):
    f = open('no.txt','r')
    lines = f.readlines()

    f_w = open('no.txt','w')
    for line in lines:
        if fromName in line:
            
            continue
        
        f_w.write(line)



    f.close()

    f_w.close()
def add(fromName):
    f = open('no.txt','a')
    f.write(fromName)
    f.write('\n')
    f.close()
def read(fromName):
    f = open('no.txt','r')
    lines = f.readlines()
    if fromName+'\n' in lines:
        return True
    else:
        return False
    
