# TCP 3-way handshake

## TCP 3-Way Handshake란?
TCP 3-Way Handshake는 TCP/IP 프로토콜에서 클라이언트와 서버 간에 신뢰성 있는 연결을 성립하기 위한 절차이다. 데이터 전송 전 세션을 수립하여, 양쪽이 데이터 송수신 준비가 되었음을 확인하고 초기 순서 번호를 교환한다.

TCP/IP 네트워크에서 안정적이고 연결 지향적인 통신을 설정하기 위해 사용되는 절차이다.
이 절차는 클라이언트와 서버 간에 신뢰할 수 있는 연결을 설정하기 위해 세 개의 메시지(세그먼트)를 교환하는 과정을 포함한다.

우선 클라이언트는 서버에 연결을 요청하는 SYN 세그먼트를 보낸다.
이 세그먼트에는 초기 순서 번호(Sequence Number)와 윈도우 크기(Window Size) 정보가 포함된다.

이후 서버는 클라이언트의 요청을 수락하고, SYN과 ACK 플래그가 설정된 세그먼트를 클라이언트에 보낸다.
이 세그먼트는 서버의 초기 순서 번호와 클라이언트의 초기 순서 번호에 대한 응답(ACK=클라이언트의 초기 순서 번호 + 1)을 포함한다.

클라이언트는 서버의 응답을 확인하고, ACK 플래그가 설정된 세그먼트를 서버에 보낸다.
이 세그먼트는 서버의 순서 번호에 대한 응답(ACK=서버의 초기 순서 번호 + 1)을 포함한다.
이 절차가 완료되면 클라이언트와 서버 간에 신뢰할 수 있는 연결이 설정되고, 데이터 전송이 시작될 수 있다.

### 📌 Handshake 과정에서 사용되는 데이터 단위: 세그먼트(Segment)

- TCP는 **전송 계층(Transport Layer)** 프로토콜이며, 이 계층의 데이터 단위는 **세그먼트(Segment)** 이다.
- 따라서 3-Way Handshake의 **SYN**, **SYN+ACK**, **ACK** 그리고 4-Way Handshake의 **FIN**, **ACK** 등은 모두 **TCP 세그먼트**로 주고받는다.
- 이러한 제어 플래그들은 모두 TCP 세그먼트의 **헤더 영역**에 포함된다.
- 연결 설정, 데이터 송수신, 연결 종료까지 TCP 통신의 모든 단계는 항상 세그먼트 단위로 이루어진다.

| Handshake 종류 | 사용 데이터 단위 |
|---------------|------------------|
| 3-Way Handshake | TCP 세그먼트 (SYN, SYN+ACK, ACK) |
| 4-Way Handshake | TCP 세그먼트 (FIN, ACK 등) |

- 즉, Handshake 과정은 **세그먼트 교환 과정**이라고 볼 수 있다.

### TCP 3-Way Handshake 절차 요약
1️⃣ 클라이언트 → 서버 : SYN 전송 (연결 요청)  
2️⃣ 서버 → 클라이언트 : SYN + ACK 전송 (요청 수락)  
3️⃣ 클라이언트 → 서버 : ACK 전송 (연결 성립)  

이후 데이터 송수신 가능 (연결 상태: ESTABLISHED)

> SYN -> Synchronize sequence numbers
> 말 그대로 “순서 번호(Sequence Number)를 동기화한다”는 의미로, TCP 연결의 시작 신호 역할을 한다.

### TCP 3-Way Handshake의 역할
- 양쪽 모두 데이터 전송 준비 완료 상태 확인  
- 양쪽 모두 상대의 초기 순서 번호 확보  
- 신뢰성 있는 연결 성립 보장  

### 보안적 측면에서 알아둘 점
- **SYN Flooding 공격**: 악의적인 클라이언트가 SYN 패킷만 보내고 응답하지 않음으로써 서버 자원을 고갈시키는 공격  
    - SYN = TCP 연결을 초기화할 때 “나 데이터 주고받을 준비됐어” 라는 의미로 보내는 패킷.
	- SYN Flooding = 이 패킷만 엄청나게 보내서 상대 서버 자원을 고갈시키는 공격.
- 이를 막기 위한 대책으로 **SYN Cookies** 기법이나, **방화벽 설정** 등이 사용됨  
- 또한 TCP 연결 단계에서 인증, 암호화는 보장되지 않기 때문에 **TLS/SSL**과 같은 추가적인 보안 계층이 필수적임



---

## TCP 4-Way Handshake

TCP 4-Way Handshake는 연결 종료 시 사용되는 절차이다. 3-Way Handshake는 연결을 성립하기 위한 과정이라면, 4-Way Handshake는 세션을 정상적으로 종료하기 위한 과정이다.

### 📌 Handshake 과정에서 사용되는 데이터 단위: 세그먼트(Segment)

- TCP는 **전송 계층(Transport Layer)** 프로토콜이며, 이 계층의 데이터 단위는 **세그먼트(Segment)** 이다.
- 따라서 3-Way Handshake의 **SYN**, **SYN+ACK**, **ACK** 그리고 4-Way Handshake의 **FIN**, **ACK** 등은 모두 **TCP 세그먼트**로 주고받는다.
- 이러한 제어 플래그들은 모두 TCP 세그먼트의 **헤더 영역**에 포함된다.
- 연결 설정, 데이터 송수신, 연결 종료까지 TCP 통신의 모든 단계는 항상 세그먼트 단위로 이루어진다.

| Handshake 종류 | 사용 데이터 단위 |
|---------------|------------------|
| 3-Way Handshake | TCP 세그먼트 (SYN, SYN+ACK, ACK) |
| 4-Way Handshake | TCP 세그먼트 (FIN, ACK 등) |

- 즉, Handshake 과정은 **세그먼트 교환 과정**이라고 볼 수 있다.

### 절차

1. 클라이언트 → 서버: FIN
    - 클라이언트는 연결 종료를 요청하는 FIN 플래그를 서버로 전송한다.

2. 서버 → 클라이언트: ACK
    - 서버는 FIN 요청을 수신하고, ACK 플래그로 응답하여 종료 요청을 수락한다.
    - 서버는 자신의 남은 작업(데이터 전송)을 모두 끝낼 때까지 대기한다.

3. 서버 → 클라이언트: FIN
    - 서버의 작업이 완료되면 클라이언트에게 FIN 플래그를 전송한다.

4. 클라이언트 → 서버: ACK
    - 클라이언트는 FIN을 수신한 후 ACK로 응답한다.
    - 이 시점 이후 연결이 종료된다.

### TIME_WAIT

- 클라이언트는 마지막 ACK를 전송한 뒤에도 일정 시간동안 연결 정보를 유지한다. 이를 TIME_WAIT 상태라고 한다.
- 이는 네트워크 지연, 패킷 유실로 인해 늦게 도착할 수 있는 패킷을 수신하기 위함이다.
- 일반적으로 기본 2배의 MSL(Maximum Segment Lifetime), 약 240초 정도 유지된다.

### 보안 고려

- TIME_WAIT 상태의 연결 정보는 자원 소모를 유발할 수 있다. 대량의 연결 해제 시 자원 고갈(포트 고갈) 문제가 발생할 수 있다.
- 이러한 문제를 방지하기 위해 서버 측에서는 TIME_WAIT 대신 클라이언트에게 종료 책임을 넘기는 경우도 있다.