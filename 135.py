add = lambda x, y: x + y
ret = add(1, 3)
print(ret)

func = [lambda x: x + '.pptx', lambda x: x + '.docx']
ret1 = func[0]('intro')
ret2 = func[1]('Report')
print(ret1)
print(ret2)
