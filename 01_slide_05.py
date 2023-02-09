# dis - Disassembler of Python byte code into mnemonics.
import dis

def myfunc(alist):
    print("hello")
    print(alist)
    return len(alist)
print(dis.dis(myfunc))