import requests
res = requests.get("http://google.com")
#res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status() #html을 가져오는데 문제가 있으면 오류를 내보내는 기능
#print("응답코드 :", res.status_code) # 200 이면 정상/html을 가져올 수 있는지 확인하는 방법이다.

# if res.status_code == requests.codes.ok:                          #requests.codes.ok = 코드값 200
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)