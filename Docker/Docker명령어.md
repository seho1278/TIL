# Docker 명령어 정리

### 도움말
- docker run --help

### 버전 확인
- docker -v

### 컨테이너 생성 명령어
- docker run -i -t [이미지 이름]:태그
- docker create -i -t --name [컨테이너 이름] [이미지 이름]:태그
  * run 명령어는 pull, create, start 명령어를 일괄적으로 실행 한 후 attach가 가능한 컨테이너라면 내부로 들어가게 하는 반면 create는 pull, create 명령어만 실행한다.

### 이미지 목록 확인
- docker images

### 컨테이너 시작
- docker start [컨테이너 이름]

### 컨테이너 정지
- docker stop [컨테이너 이름]

### 컨테이너 내부로 이동
- docker attach [컨테이너 이름]

### 컨테이너 빠져나오기
- exit
  * exit 명령어는 실행중인 컨테이너를 정지시키고 빠져나온다.
- Ctrl + P, Q
  * 위 단축키를 사용하면 실행중인 상태에서 컨테이너를 빠져나온다.

### 컨테이너 목록 확인
- docker ps
- docker ps -a
  * 정지상태의 컨테이너 포함 모든 컨테이너를 조회
- docker ps -a --format {{.ID}}\t{{.Status}}
  * 원하는 정보만 입력할 경우(\t는 줄바꿈을 의미)

### 컨테이너 삭제
- docker rm [컨테이너 이름]
  * 실행중인 컨테이너를 삭제 시도할 경우 에러가 발생할 수 있다.
- docker rm -f
  * 실행중인 컨테이너 삭제
- docker container prune
  * 모든 컨테이너 삭제
- docker rm $(docker pa -a -q)
  * 모든 컨테이너 삭제 -q는 id값만 출력

### 컨테이너 이름 수정
- docker rename [컨테이너 이름] [변경할 컨테이너 이름]

### 호스트와 바인딩된 포트만 확인하는 명령어
- docker port [컨테이너 이름]

### Detached 모드 실행
- docker run -d ...
  * 컨테이너를 백그라운드에서 동작하는 애플리케이션으로 실행하도록 설정

### 컨테이너 내부 환경변수 설정
- docker run ... -e MYSQL_ROOT_PASSWORD=password ...
  * 예시로 mysql 컨테이너를 생성할 때 설정한 -e 옵션의 값을 살펴보면 mysql 컨테이너의 환경변수로 어떤 것이 설정됐는지 알 수 있다.

### 컨테이너 내부 셸 확인
- docker exec [컨테이너 이름] /bin/bash
  * Detached 모드로 생성한 경우 attach 명령어를 쓰는 것은 의미가 없기 때문에 exec 명령어를 이용하면 컨테이너 내부의 셸을 사용할 수 있다.
  * 컨테이너 내부 확인 명령어 : docker exec [컨테이너 이름] ls