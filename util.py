#!C:\Python27\python
a=open('listing20-1.txt').read()

def b():
    print 'ss'

def lines(file):
    for line in file:
        yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
