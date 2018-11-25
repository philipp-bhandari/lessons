import os
import glob
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))
migrations = current_dir + '/Migrations'


def check_file(file, query):
    process = subprocess.Popen('cat "{}" | grep "{}"'.format(file, query), shell=True, stdout=subprocess.PIPE)
    stdout_list = process.communicate()
    return bool(stdout_list[0])
#

def use_search(files):
    print('Введите строку:')
    query = input()
    files_list = []
    for file in files:
        filename = os.path.join(migrations, file)
        result = check_file(filename, query)
        if result == 1:
            files_list.append(file)
            print(file)
    print('Количество подходящих файлов: {}'.format(len(files_list)))
    return files_list


if __name__ == '__main__':

    os.chdir(migrations)
    all_files = glob.glob('*.sql')

    temp_files = use_search(all_files)

    while len(temp_files) > 1:
        temp_files = use_search(temp_files)
