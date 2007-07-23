import codecs

current_depth = 0
indent_width = 4

def braces_encode(input, errors='strict',
                  filename='<data>', mode=0666):
    return (str(input), len(input))

def braces_decode(input, errors='strict'):
    if not input: return (u'', 0)
    length = len(input)
    # Deal with chunked reading, where we don't get
    # data containing a complete line of source
    if not input.endswith('\n'):
        length = input.rfind('\n') + 1
    input = input[:length]

    acc = []
    global indent_width, current_depth
    lines = input.split('\n')
    for l in [x.strip().replace('++', '+=1') for x in lines]:
        if l.endswith(';'):
            l = l[:-1]

        if l.endswith('{'):
            acc.append(' ' * current_depth + l[:-1].strip() + ':')
            current_depth += indent_width
        elif l.startswith('{'):
            current_depth -= indent_width
            acc.append(' ' * current_depth + l[1:])
        elif l.endswith('}'):
            acc.append(' ' * current_depth + l[:-1].strip())
            current_depth -= indent_width
        else:
            acc.append(' ' * current_depth + l)
    return (u'\n'.join(acc)+'\n', length)

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return braces_encode(input, errors)
    def decode(self, input, errors='strict'):
        return braces_decode(input, errors)

class StreamWriter(Codec, codecs.StreamWriter):
    pass

class StreamReader(Codec, codecs.StreamReader):
    pass

def getregentry():
    return (braces_encode, braces_decode, StreamReader, StreamWriter)

