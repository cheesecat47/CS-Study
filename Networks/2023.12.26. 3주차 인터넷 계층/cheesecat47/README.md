* [IPv4 프로토콜](#ipv4-프로토콜)
    * [IPv6](#ipv6)
* [ICMP 프로토콜](#icmp-프로토콜)
* [Routing Table](#routing-table)
    * [통신 과정](#통신-과정)
* [Fragmentation](#fragmentation)
* [IP 주소와 Net-mask](#ip-주소와-net-mask)

# IPv4 프로토콜

- 네트워크 상에서 데이터를 교환하기 위한 프로토콜.
- 데이터가 정확하게 전달될 것을 보장하지는 않음.
    - 패킷이 중복 전달되거나, 순서가 바뀔 수 있음.
    - 이를 보장하는건 상위 프로토콜인 TCP에서 수행.
      ![](Pasted%20image%2020231226140509.png)
- 마지막 IP Option은 일반적으로는 잘 안 붙으므로 IPv4는 20bytes라고 생각해도 될 듯.
- Src Addr, Dest Addr은 IP주소니 각 4bytes.
- 헤더 길이는 2진수 4개로 표현하는데, 나누기 4를 한 값이 들어감.
    - 그러므로 옵션이 없는 기본 IPv4 헤더 길이는 20bytes이니 IHL에는 5(1001<sub>(2)</sub>)가 들어가고, 옵션이 하나 추가될 때마다 4bytes 늘어나니 IHL에는 1씩 늘어남.
- TOS는 지금은 사용하지 않는 값이라 0으로 채움.
- Total Length는 전체(Header + Payload) 길이.
- Identification, IP Flags, Fragment Offset은 한 세트로 취급.
    - 큰 데이터를 MTU 크기에 맞춰서 잘라서 전송할 때 사용하는 값.
    - IP Flags
        - D: Don't fragment: 이 패킷을 더 나누지 말 것. 그런데 이 옵션을 지정해서 전송하면 MTU보다 크기 때문에 전송이 안됨. 그래서 잘 안 씀.
        - M: More fragments: 이 패킷 뒤에 나누어진 패킷이 더 있음. 조각들을 다시 붙여 원본을 만들기 위해 더 기다려야 함.
    - Fragmentation Offset
        - 이 잘려진 패킷이 원래 데이터의 몇 번째인지? IP는 순서를 보장하지 않기 때문.
- Time To Live (TTL)
    - 라우팅 과정에서 패킷이 루프로 잘못 빠졌을 때 무한히 살아서 누적되어 네트워크 혼잡을 유발할 수 있음.
    - Hop마다 TTL 값을 -1씩 줄여 0이 되면 패킷 폐기.
        - Windows는 기본값이 128, Linux는 64.
- Protocol
    - 상위 프로토콜. ICMP, TCP, UDP 중 하나.
- Header Checksum

## IPv6

- IPv4는 32bit 주소 체계, v6는 128bit.
- 잘 사용되지는 않음.

---

# ICMP 프로토콜

- 오류 메시지 전송 받는 데 주로 사용. 상대방과 통신이 잘 되는지 확인.
  ![](Pasted%20image%2020231226144953.png)
- Type: 대분류.
    - 8 Echo: 요청 -> 0 Echo Reply: 응답.
    - 3 Destination Unreachable: 목적지에 도달할 수 없음. 경로상 문제.
    - 11 Time Exceded: 시간 초과. 목적지까지 갔으나 응답을 받지 못함. 상대방 문제. 대표적으로는 상대방이 방화벽을 켜둬서 내 패킷을 무시한 경우.
    - 5 Redirect: 상대방 라우팅 테이블을 수정할 때 쓸 수 있음. 그래서 보안상 중요.
- Code: 소분류.

---

# Routing Table

![](Pasted%20image%2020231226145232.png)

- 라우팅 테이블에 적혀있는 네트워크 대역만 찾아갈 수 있음.
    - 그래서 기본 게이트웨이 값을 하나 추가해 줌. 내가 모르는 네트워크 대역이면 게이트웨이 밖으로 나가서 찾도록.

## 통신 과정

![](Pasted%20image%2020231226145332.png)

- A가 B와 통신하려 할 때 B의 네트워크 대역이 A의 라우팅 테이블에 있어야 찾아갈 수 있음.
- `192.168.20.20`은 `192.168.20.0/24`대역에 매칭되고, 이 곳을 찾아가려면 우선 `192.168.10.1`로 가야된다고 함.
  ![](Pasted%20image%2020231226145555.png)
- 일단 통신이 되는지 확인하기 위해 ICMP 요청 프로토콜 (Type:08) 작성.
  ![](Pasted%20image%2020231226145920.png)
- 이 때 MAC Address는 최종 목적지 주소가 아니라 가장 가까운 게이트웨이(여기서는 공유기)의 MAC 주소.
    - 이 때 중간 과정에 있는 장비들의 MAC 주소는 어떻게 알아내나? ARP.
      ![](Pasted%20image%2020231226150102.png)
- 공유기가 2계층 패킷을 열어보고 자신에게 온 게 맞으니 3계층 패킷을 열어봄. 그러면 목적지 IP가 자신이 아님.
- 그러면 공유기는 자신의 라우팅 테이블을 확인해 해당 패킷을 어디로 보내야되는지 찾음.
- 라우터로 전송할 때는 이더넷 프로토콜을 다시 만듦.
- 이렇게 네트워크를 타고 타고 B까지 도달.
  ![](Pasted%20image%2020231226150401.png)
- 결과적으로 B에 도달해서 B가 패킷을 다 열어봤을 때 자신이 맞다면 반대로 ICMP 응답 패킷을 만들고 A로 보낼 때 동일한 과정으로 반복.

---

# Fragmentation

![](Pasted%20image%2020231226153922.png)

- MTU는 일반적으로 1500bytes. 매우 큰 패킷은 MTU에 맞게 나눠서 전송해야 함.
- 이 그림에서는 MTU가 3300bytes로 설정되어 있다고 가정.
- IPv4 프로토콜 헤더 20bytes가 붙어야 하므로 Payload의 최대 길이는 3,280bytes.
- 여기서는 Offset을 8로 나눈 값으로 사용. 그래서 2번째 패킷은 MoreFragment가 1, Offset이 410.
  ![](Pasted%20image%2020231226154728.png)
- 전송하려는 원래 데이터가 2000bytes인 경우.
    - Encapsulation을 하다 보면 헤더 크기만큼 더 붙음.
- MTU보다 패킷 크기가 크기 때문에 그냥은 못 보냄.
  ![](Pasted%20image%2020231226154822.png)
- MTU가 1500이므로 IPv4 헤더 크기를 제외한 크기만큼 데이터를 나눔.
- ICMP 요청은 나눠진 두 패킷 모두가 아니라 뒤쪽 패킷에 한 번만 붙음. 그래야 다시 복원했을 때 원래 패킷과 동일해짐.
- 이제는 MTU 크기에 맞으니 전송 가능하고, 그 다음 전송을 위해 Ethernet Encapsulation하여 14바이트 더 붙음.
    - 그래서 프레임(2계층 PDU)은 최대 1,514바이트.

---

# IP 주소와 Net-mask

![](Pasted%20image%2020231226161709.png)

- IP 주소는 Host에 대한 식별자.
- IPv4는 32bit 주소 체계 -> 최대 약 43억 개. 주소 개수 부족함.
  ![](Pasted%20image%2020231226162149.png)
- IPv4 주소는 8bit씩 끊어서 표기.
- IPv4 주소는 Network ID, Host ID 두 부분으로 나눠서 볼 수도 있음.
    - Network ID의 길이를 나타내는 것이 Subnet Mask.
      ![](Pasted%20image%2020231226162416.png)
- IP 주소와 Subnet Mask를 `&`(bitwise AND) 연산을 하게 되면 Network ID를 얻을 수 있음.
- `/` 기호를 사용해 짧게 표기하기도 함.

---

> 사진 캡처 출처
> - [따라하면서 배우는 IT. "06. 멀리 있는 컴퓨터끼리는 이렇게 데이터를 주고받는다 - IP 프로토콜 구조"](https://youtu.be/_i8O_o2ozlE?feature=shared)
> - [따라하면서 배우는 IT. "06. 멀리 있는 컴퓨터끼리는 이렇게 데이터를 주고받는다 - ICMP 프로토콜"](https://youtu.be/JaBCIUsFE74?feature=shared)
> - [따라하면서 배우는 IT. "06. 멀리 있는 컴퓨터끼리는 이렇게 데이터를 주고받는다 - 라우팅 테이블 및 전송 과정"](https://youtu.be/CjnKNIyREHA?feature=shared)
> - [따라하면서 배우는 IT. "06. 멀리 있는 컴퓨터끼리는 이렇게 데이터를 주고받는다 - 조각화 이론"](https://youtu.be/_AONcID7Sc8?feature=shared)
> - [널널한 개발자 TV. "IPv4주소 체계에 대한 암기사항"](https://youtu.be/gOMljj6K2V0?feature=shared)
