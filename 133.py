chv = input('Input a character value: ')
chv = int(chv)
try:
    ch = chr(chv)
    print('ch val: {} [{}],  ch: {}'.format(chv, hex(chv), ch))
except ValueError:
    print('No charter for value <{}> '.format(chv))