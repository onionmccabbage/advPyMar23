
def writeBytes():
    '''convert a string to byte data then persist in a byte file'''
    b = bytes( range(0, 256) ) # 0, 1, 2, ...255 i.e. 256 values
    # print(b) # print will ALWAYS convert bytes back into string data
    fout = open('bfile', 'wb') # 'w' means (over)write 'b' means bytes
    fout.write(b)
    fout.close()

def readbytes():
    '''read byte data in from a byte file'''
    fin = open('bfile', 'rb') # 'rb' will read bytes
    retrieved = fin.read()
    fin.close()
    print(retrieved)

if __name__ == '__main__':
    writeBytes()
    readbytes()