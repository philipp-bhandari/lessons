headers_list = []
counter = 0

with open('zagolovki_copywr.txt') as headers:
    for header in headers:
        headers_list.append(header.strip())

with open('keys_copywr.txt') as keys:
    for key in keys:
        key = key.strip()

        for header in headers_list:
            with open('phrases.txt', 'a') as file:

                phrase = header.replace('|', key)
                phrase = phrase.strip() + '\n'
                file.write(phrase)
                counter += 1
                print('Выполняется: ', counter)
