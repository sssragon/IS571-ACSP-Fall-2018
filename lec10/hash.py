def ROL(data, shift, size=32):
    shift %= size
    remains = data >> (size - shift)
    body = (data << shift) - (remains << size )
    return (body + remains)


def ROR(data, shift, size=32):
    shift %= size
    body = data >> shift
    remains = (data << (size - shift)) - (body << size)
    return (body + remains)

hash = 0;
#api = ['G', 'e', 't', 'P', 'r', 'o', 'c', 'A', 'd', 'd', 'r', 'e', 's', 's'];
api = ['C', 'l', 'o', 's', 'e', 'P', 'r', 'i', 'v', 'a', 't', 'e', 'N', 'a', 'm', 'e', 's', 'p', 'a', 'c', 'e'];

for c in range(0, len(api)):
    hash = ROR(hash, 5);
    hash = hash + ord(api[c])
    print api[c], hash, hex(hash)
