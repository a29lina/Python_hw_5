def rle_encode(data):
    encode_data = ''
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else :
            if count == 1:
                encode_data += data[i-1]
            else:
                encode_data += str(count) + data[i-1]
                count = 1
    else:
        if count == 1:
            encode_data += str(count) + data[i]
        else:
            encode_data += str(count) + data[i]
    return encode_data

print(rle_encode('aaaaaaaaaaaaannnnnnnnnnnnj'))


def rle_decode(data):
    decode_data = ''
    count = ''
    for char in data:
        if char.isnumeric():
            count += char
        else :
            decode_data += int(count) * char
            count = ''
    return decode_data

print(rle_decode('13a12n1j'))
