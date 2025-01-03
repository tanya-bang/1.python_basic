from os import path

def study_write():
    file_path = path.dirname(path.realpath(__file__))
    file = open(f'{file_path}/text.txt', 'w')
    file.write('hello io')
    file.close()
    
def study_read():
    file_path = path.dirname(path.realpath(__file__))
    file = open(f'{file_path}/text.txt', 'w')
    txt = file.read()
    print(txt)
    file.close() 
    
study_read()