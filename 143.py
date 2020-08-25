bufsize = 1024  # for reading by 1kB. 
f = open('./sources/img_sample.jpg', 'rb')
h = open('./sources/img_sample_copy.jpg', 'wb')

data = f.read(bufsize)
while data:  # '' when done
    h.write(data)
    data = f.read(bufsize)

f.close()
h.close()