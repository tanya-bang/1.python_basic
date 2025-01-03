from io import BytesIO
from os import path
# 아까 전에는 파일에서 메모리 땡겨오는 거였음.
# 여기는 메모리 내에서 입출력 데이터를 다루어야 할 때 사용
def study_biteIO():
    file_path = path.dirname(path.realpath(__file__))
    with open(f'{file_path}/test.txt', 'rb') as file:
        byte_stream = BytesIO()
        byte_stream.write(file.read())
        byte_stream.write(b'\nfrom bytestream')
        byte_stream.seek(0)
        print(byte_stream.read())
        
study_biteIO()