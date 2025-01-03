import socket
from QRGenerator import QRGenerator


class Sever:
    def __init__(self):
        self.__port = 9898
        self.__buffersize = 1024 # 버퍼: 한번에 읽어들어올 메모리

    # 소켓에는 두 종류가 있다.
    """
    1. sever socket : 서버가 상시로 열어두는 소켓
    2. client socket : 클라이언트와 통신을 위해서 1:1로 열어두는 소켓.
    """
    # 우리가 서버를 만들면 클라이언트가 찾아오잖아. 그럼 찾아온지는 알아야될 거 아냐.
    # 클라이언트가 서버소켓에다가 나 너네랑 통신할래! 하면 client socket을 열어줌
    # 그리고 볼일 끝나면 client socket을 닫을 수 있다. -> 컴 부담 줄이기
    # 겜 서버가 터지는 이유는 client socket을 닫을 수가 없어서 ㅋㅋ ㅠ
    # 근데 웹서버는 죽었다는 얘기가 없는게 c.s를 무조건 닫을수 있으니까 서버안정성 굿.
    
    # 공식문서 소켓 만들기 ㄱㄱ
        
    def start_sever(self):
        sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 공식문서에 나와있는 소켓만들기 내용
        sever_socket.bind(('localhost', self.__port)) #IP 넣어도 되는데 오류나서 localhost입력
        sever_socket.listen(5) # 대기할 수 있는 클라이언트의 숫자
        
        while(True):
            client_socket, address = sever_socket.accept() # 클라이언트 소켓 열기
            request = client_socket.recv(self.__buffersize)
            req_txt = str(request, encoding = 'utf-8') #http message str 타입으로 변경

            statusline = req_txt.splitlines()[0] # 첫 줄 추출!
            status_token = statusline.split(' ')
            
            http_method = status_token[0]
            req_url = status_token[1]
            
            # 요청 URL에 대한 검증을 실행해야함.
            # 우리서버는 qr로 시작하는 것만 요청을 받고 다른 모든 요청은 거절하자.
            if('/qr' not in req_url):
                client_socket.close() # 요청한 path가 아닌 (/qr이 없는) path로 요청했으니 너랑은 통신안해~
                continue # 소켓 닫고 while문으로 돌아간다.
            
            # 데이터가 이런 이름으로 넘어왔을거야
            # '/qr?data=www.naver.com
            # 그 중에 우리는 도메인을 잘라서 뒤에 네이버 주소를 꺼낼거잖아.
            # = 기준으로 잘라도 되긴 하는데 쿼리스트링의 규칙이 &로 여러가지가 넘어올 수 있는 규칙이다.
            # like '/qr?query1=a&query2=b&query3=c 이런식으로
            # 그래서 일단 ?로 잘라서 url과 쿼리스트링을 나눠주고, & 기준으로 한번 더 나누어줌.
            
            url_tokens = req_url.split('?')
            path = url_tokens[0]
            
            if(len(url_tokens) >= 2):
                #쿼리스트링 잘라서 하는 작업을 쭉 하면 되겠고.
            
                query_string = url_tokens[1]

                param_dict ={}
                params = query_string.split('&') # parameters 줄여서 params
                for e in params:
                    token = e.split('=')
                    param_dict[token[0]] = token[1]
                print(param_dict)

                client_socket.send(b'HTTP/1.1 200 OK\n') # 이게 양식 1) 200이 ㅇㅋ라는 뜻이라 이걸 넣어줌
                client_socket.send(b'Content-Disposition: attachment; filename="qr.png"\n\n')#다운로드 가능하게 해주는 헤더
                qr = QRGenerator()
                client_socket.send(qr.generate(param_dict[token[0]]))
                print(param_dict[token[0]])
                client_socket.close()
                continue
                # 토큰의 0번 인덱스 값을 바이트 형식으로 전달하겠다.라는 뜻
                # 근데 이거 해도 브라우저에서는 뭐가 안보임.
                # 왜그러냐면 양식을 안지켜서. =그 이미지파일에서 본 약속 ㅇㅇ (start-line, HTTP headers, empty line, body 요 양식)
                # 이제 양식을 지켜볼 것이다.
                
            client_socket.send(b'HTTP/1.1 200 OK\n\n')
            client_socket.send(b'hello world, there is no query')
            client_socket.close()
