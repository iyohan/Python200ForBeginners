ch = input('Input a character: ')
if len(ch) != 0:
    ch = ch[0]
    chv = ord(ch)
    print('char: {},  char val: {} [{} {}]'.format(ch, chv, hex(chv), bin(chv)))