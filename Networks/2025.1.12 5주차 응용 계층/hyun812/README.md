# 5주차 - 응용 계층 - HTTP/HTTPS, DHCP, DNS, SSH, TLS/SSL

</br>

## 7계층 프로토콜

## HTTP (**H**yper**T**ext **T**ransfer **P**rotocol)

- 클라이언트와 웹 서버 간에 정보를 주고받기 위해 사용되는 네트워크 프로토콜
- www에서 쓰이는 핵심 프로토콜
- 문서의 전송을 위해 쓰임
- 모든 웹 애플리케이션에서 사용되고 있음
- Request / Response ( 요청/응답) 동작에 기반하여 서비스 제공

</br>

### HTTP 1.0

**특징**

- 연결 수립, 동작, 연결 해제의 단순함이 특징 → 하나의 URL은 하나의 TCP 연결
- HTML 문서를 전송 받은 뒤 `연결을 끊고` `다시 연결`하여 데이터를 전송

**문제점**

단순 동작이 반복되어 `통신 부하` 문제 발생

</br>

### HTTP 1.1

**특징**

- `연결을 유지`
- HTTP 1.0과는 달리 Server가 갖는 하나의 IP Address와 다수의 Web Site 연결 가능
- 빠른 속도와 Internet Protocol 설계에 최적화될 수 있도록 Cache 사용
- Data를 압축해서 전달이 가능하도록 하여 전달하는 Data 양이 감소

![Untitled](image.png)

<aside>
💡 Port 번호는 Process에 대한 식별자 ( 1 ~ 65534 )
</aside>

</br>
</br>

# 웹 브라우저에 URL을 입력하면 일어나는 일

![Untitled](image1.png)

1. `hosts` 파일을 확인 ( IP와 도메인의 매핑이 입력되어 있음 )
2. OS에서 제공하는 `DNS Cache`를 확인 ( 최근에 수행된 DNS 조회 결과를 저장하는 메모리 영역 )
3. 기록에 없다면 `DNS 서버`에 `직접 질의`하여 IP 매핑을 얻음
   1. `공유기` 사용 시 공유기가 `DNS 포워딩`하여 직접 질의
   2. ISP ( Internet Service Provider ) 의 DNS에 요청
4. IP주소를 얻은 후 네이버에 http 통신을 위해 `TCP 연결`
5. `HTTP Request`로 질의
6. 그에 따른 `Response`를 받음
7. 이후 받은 데이터를 화면에 렌더링

**GSLB ( 전역 서버 부하 분산 )**

인터넷 트래픽을 전 세계에 걸쳐 분산된 수많은 연결된 서버에 배포하는 방식

**CDN ( Content Delivery Network )**

지리적으로 분산된 서버들을 연결한 네트워크

1. 사용자가 접속
2. 접속자의 IP주소를 보고 CDN이 위치를 파악
3. 가장 원활하게 접속할 수 있는 IP주소를 알려줌

**Health check**

서버의 상태를 주기적으로 확인하여 서버의 정상 작동 여부를 판단하는 과정

</br>
</br>

# DNS ( D**omain Name System )**

- 사람이 이해하기 쉬운 `도메인` 이름을 실제 네트워크상에서 사용하는 `IP 주소로` `변환`하는 역할을 수행하는 `분산형` `데이터베이스` 시스템
- 도메인 수가 너무 많기 때문에 DNS 서버 종류를 계층화해서 단계적으로 처리
- Root DNS는 전세계에 13대

![Untitled](image2.png)

</br>

### 동작과정

1. 웹 브라우저는 Local DNS 서버에 해당 도메인의 IP주소를 요청
2. 접속정보가 캐싱되어 있으면 바로 IP주소를 알려줌
3. 접속정보가 없을 경우 Root DNS 서버에 요청 + com 주소 알려줌
4. Local DNS 서버는 com 도메인을 관리하는 TLD DNS 서버에 요청 + naver.com 주소 알려줌
5. Local DNS 서버는 naver.com 도메인을 관리하는 Authoritative DNS 서버에 요청
6. Local DNS 서버는 해당 도메인의 IP주소를 응답 및 캐싱
7. 웹 브라우저에게 응답받은 IP주소 전달

![Untitled](image3.png)
