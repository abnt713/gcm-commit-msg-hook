__author__ = 'alisonbnt'

from subprocess import call

def setup():
    print('-- GCM REPOSITORY SETUP --')
    print('Current directory')
    call(['pwd'])
    print('Make sure this script is running at the repository root')
    answer = raw_input('Running in root dir? (Y/n) ')

    if answer == 'n':
        print('Access the root directory and then run this script from there')
        exit()

    elif answer.lower() != 'y':
        print('Invalid option - Quiting')
        exit()

    print('Running setup')

if __name__ == '__main__':
    setup()
