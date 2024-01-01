import random
import string

def main():
    start = input('enter whether you want to code or decode the message:')
    def random_char(y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y)).lower()

    if start.lower() == 'code':
        msg = input('enter the message you want to code:')
        msg_spl = msg.split()
        for i in msg_spl:
            if len(i) < 3:
                def reverse(i):
                    i = list(i)
                    i.reverse()
                    x = ''.join(i)
                    return x
                print(reverse(i), end= ' ')
            else:
                def encode(i):
                    first = i[0]
                    new_msg = str(random_char(3)+ i[1:len(i)+1] + first + random_char(3))
                    return new_msg
                print(encode(i), end=' ')

    if start.lower() == 'decode':
        code = input('enter message you want to decode:')
        code_spl = code.split()
        for i in code_spl:
            if len(i) < 3:
                def reverse(i):
                    i = list(i)
                    i.reverse()
                    x = ''.join(i)
                    return x
                print(reverse(i), end= ' ')
            else:
                def decode(i):
                    msg_coded = i[3:-3]
                    last = msg_coded[-1]
                    final_msg = last + msg_coded[:-1]
                    return final_msg
                print(decode(i), end = ' ')

main()
cont = input('\n enter whether you want to continue or not:')
while True:
    if cont.lower() == 'continue':
        main()
    else:
        break