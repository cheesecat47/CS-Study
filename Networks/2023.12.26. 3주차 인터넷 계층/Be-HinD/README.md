# 3계층 역할

**수신처까지 최적의 경로 탐색 (라우팅 역할)**

2계층 이더넷에서는 주소로 MAC 주소를 사용했지만, 3계층에서는 MAC 주소는 사용하지 않는다. 그 이유는 MAC 주소는 **장소를 특정할 수 없는 주소이기 때문**

---

# IPv4가 하는 일

네트워크 상에서 데이터를 교환하기 위한 프로토콜

데이터가 정확하게 전달될 것을 보장하진 않음

중복된 패킷을 전달하거나 패킷의 순서를 잘못 전달할 가능성도 있음.

(악의적으로 이요되면 DoS 공격이 됨)

데이터의 정확하고 순차적인 전달은 그보다 상위 프로토콜인 TCP에서 보장함.

---

# IPv4 프로토콜 구조

IPv4 프로토콜 ⇒ 다른 네트워크의 특정 대상을 찾는 프로토콜

![Untitled](png1.png)

**Version** : IP 프로토콜의 버전을 명시 (IPv4의 경우만 올 수 있음)

**IHL(Header Length)** : 헤더의 길이 (최소 20BYTE ~ 최대 60BYTE)

- 4bit로 60까지 표현하기 위해서는 4로 나눈 값을 명시

**Type of Service(TOS)** : 아주 과거에 사용했지만 현재는 사용하지 않기 때문에 0으로 초기화

**Total Length** : 헤더의 길이가 아닌 페이로드(상위 캡슐화 포함)까지 합쳐진 전체 길이를 명시

**Identification** : 패킷의 전송과정에서 원래 하나의 데이터를 여러 패킷으로 쪼개서 보내기 때문에 각각의 쪼개진 패킷들이 하나의 데이터를 뜻하는지 체크하기 위한 ID ⇒ 같은 ID면 원래 하나의 데이터

**IP Flags** : 3bit로 이루어져 있음.

첫 bit는 사용하지 않고

두번째 비트는 최대 길이를 넘어선 데이터를 강제적으로 보내기 위한 플래그 값으로 웬만하면 이 경우 전송이 되지 않기 때문에 사용을 잘 하지 않음.

실질적으로 마지막 bit만 사용하는데 이는 최대 길이를 넘어선 데이터를 보낼 시 조각화를 해서 보내게 되는데 해당 bit는 첫 패킷 도착 이후 연속되는 패킷이 있다는걸 알리는 플래그 값.

**Fragment Offset** : 13bit로 이루어져 있음. 조각화된 데이터들의 순서를 보장하기 위해 다음 순서의 패킷까지의 거리를 나타냄.

**Time To Live(TTL)** : 패킷이 살아있을 수 있는 시간을 지정. 네트워크 전송과정에서 실수로 인한 Cycle이 발생할 경우 전송은 되지않고 패킷이 축적되기만 하는 문제를 해결하기 위한 지정값.

**Protocol** : 상위 프로토콜이 무엇인지 알려주는 값.

**Header Checksum** : 헤더가 오류가 있는지 없는지 확인하는 값. 보낼 때 전체 헤더의 값들을 체크하여 값을 지정해서 보내면 수신측은 받고 다시 전체 헤더의 값들을 체크하여 값을 구한 후 해당 Checksum을 확인하여 다르다면 패킷을 버리게 됨.

---

# IPv4의 조각화

### 조각화란 ?

큰 IP 패킷들이 적은 MTU를 갖는 링크를 통하여 전송되려면 여러 개의 작은 패킷으로 쪼개어/조각화 되어 전송돼야 함.

즉, 목적지까지 패킷을 전달하는 과정에 통과하는 각 라우터마다 전송에 적합한 프레임으로 변환이 필요.

일단 조각화되면, 최종 목적지에 도달할 때까지 재조립되지 않는 것이 일반적임

IPv4에서는 발신지 뿐만 아니라 중간 라우터에서도 IP 조각화가 가능

IPv6에서는 IP단편화가 발신지에서만 가능

재조립은 항상 최종 수신지에서만 가능

---

# ICMP 프로토콜

**특정 대상과 내가 통신이 잘되는지 확인하는 프로토콜 (ping 명령어)**

ICMP (Internet Control Message Protocol, 인터넷 제어 메시지 프로토콜)

네트워크 컴퓨터 위에서 돌아가는 운영체제에서 오류 메시지를 전송 받는 데 주로 쓰임.

프로토콜 구조의 Type과 Code를 통해 오류 메시지를 전송 받는다.

## ICMP 프로토콜의 구조

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/bd50b0fd-675b-41a4-9c64-cccbec0fb4a4/cdecf700-8694-499a-824c-c30179822d9c/Untitled.png)

**Type** : 대분류, 종류가 다양함.

아래 표에서 **8번은 요청, 0번은 응답**

3번의 경우 목적지까지 가지 못한 경우 (송신자의 문제)

11번의 경우 목적지까진 도달했지만 문제가 있는 경우(상대방 방화벽에 의해 차단되는 경우) (수신자의 문제)

5번의 경우 원격지에 있는 상대방의 라우팅 테이블을 수정할 때 사용

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/bd50b0fd-675b-41a4-9c64-cccbec0fb4a4/bf6df8b6-8f03-4ed9-9f56-9e6a65996187/Untitled.png)

Code : 소분류

---

# 라우팅 테이블

어디로 보내야 하는지 설정되어 있는 테이블

다른 네트워크 대역을 찾아가는 경로에 대한 지도 느낌임

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/bd50b0fd-675b-41a4-9c64-cccbec0fb4a4/85500fac-47d1-4fee-9705-dbcd6677fa26/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/bd50b0fd-675b-41a4-9c64-cccbec0fb4a4/5db04b80-7dc4-4bab-ac9c-915b48b128b4/Untitled.png)

A → B에게 데이터를 보낼 때 A의 라우팅 테이블에 B의 네트워크 대역이 없다면 보낼 수가 없음.

## 대략적인 전송과정

**추가 예정**

---

# IPv4 주소 체계에 대한 암기사항

IP는 HOST에 대한 식별

IPv4 주소 길이 32bit

IPv6 주소 길이 128bit

IPv4 주소 = NetID + HostID

위에서 NetID의 길이가 얼마인지를 나타내는 것이 NetMask

netmask를 ip와 bit AND연산을 하면 network ID를 얻을 수 있고 나머지가 host id가 되는 것

---

# Reference

[[따라學IT] 06. 멀리 있는 컴퓨터끼리는 이렇게 데이터를 주고받는다 - IP 프로토콜 구조 - YouTube](https://www.youtube.com/watch?v=_i8O_o2ozlE)

[[따라學IT] 06. 멀리 있는 컴퓨터끼리는 이렇게 데이터를 주고받는다 - ICMP 프로토콜 (youtube.com)](https://www.youtube.com/watch?v=JaBCIUsFE74)

[[따라學IT] 06. 멀리 있는 컴퓨터끼리는 이렇게 데이터를 주고받는다 - 라우팅 테이블 및 전송 과정 (youtube.com)](https://www.youtube.com/watch?feature=shared&v=CjnKNIyREHA)

[[따라學IT] 06. 멀리 있는 컴퓨터끼리는 이렇게 데이터를 주고받는다 - 조각화 이론 - YouTube](https://www.youtube.com/watch?v=_AONcID7Sc8)

https://www.youtube.com/watch?feature=shared&v=gOMljj6K2V0
