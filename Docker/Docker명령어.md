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
