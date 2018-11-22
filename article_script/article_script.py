long_file = open('long','a')
short_file = open('short','a')

with open('text') as file:
    for line in file:
        if len(line) > 100:
            long_file.write('\n' + line)
        else:
            short_file.write('\n' + line)

long_file.close()
short_file.close()
