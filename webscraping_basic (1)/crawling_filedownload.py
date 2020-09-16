import urllib.request as req
import re

rep = req.urlopen('https://daum.net')

data = rep.read().decode('utf8')

result = re.findall('https://[./-_\w]+.jpg',data) 
# '\w' : 문자가 포함된 것을 찾는다.(특수기호는 해당 안됨)
# '+' : 하나 이상의 문자열을 찾는다.
# '.','/','-','_' : 특수기호는 각각 입력해서 넣어야함

#찾은 파일 다운받기
for link in result:
    idx = link.rfind('/') #오른쪽부터 처음으로 나오는 '/'왼쪽에 커서위치
    with open( link[idx+1:], "wb") as f: #'/'를 파일제목에 포함시키지 않기 위해 +1 해줌
        pic = req.urlopen(link)
        f.write(pic.read())     


# print(rep.read())
# print(rep.read().decode(utf8)) 바이트로 깨진 정보가 한글로 해독되어 출력됨
# print(rep.getheaders()) #중요한 정보만 모아놓은 리스트를 불러옴
# print(rep.getheader("Connection")) #중요한 정보 중 특정한 값만 불러옴
# print(rep.status) #현재 요청이 어떠한 상태로 반환되었는가? '200'이면 정상적으로 반환했다는 뜻