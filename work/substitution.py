headers_list = []
counter = 0

with open('headings') as headers:
    for header in headers:
        headers_list.append(header.strip())

with open('keys') as keys:
    for key in keys:
        key = key.strip()

        for header in headers_list:
            with open('phrases', 'a') as file:

                phrase = header.replace('|', key)
                phrase = phrase.strip() + '\n'
                file.write(phrase)
                counter += 1
                print('Выполняется: ', counter)
