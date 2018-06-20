from pymouse import PyMouse
import time
m = PyMouse()
time.sleep(5)
a = m.position()
m.click(a[0],a[1])
time.sleep(5)
b = m.position()
m.click(b[0],b[1])
f = open('mouse.txt','a')
f.write(str(a))
f.write('\n')
f.write(str(b))
f.close()


