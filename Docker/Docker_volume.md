# Docker volume

### 1. 도커 볼륨이란
- 도커 이미지로 컨테이너를 생성하면 이미지는 읽기 전용이 되며 컨테이너의 변경 사항만 별도로 저장해서 각 컨테이너를 보존하는 기능이다.

- 도커 컨테이너의 경우 생성과 삭제가 매우 쉬워 실수로 컨테이너를 삭제하게될 경우 데이터를 복구할 수 없게 되는데, 이를 방지하기 위해 컨테이너의 데이터를 영속적 데이터로 활용할 수 있는 방법이 몇 가지 있다. 그중 하나가 볼륨을 활용하는 것이다.

- 볼륨을 활용하는 방법은 여러가지가 있으며, 호스트와 볼륨을 공유할 수도 있고, 볼륨 컨테이너를 활용할 수도 있으며, 도커가 관리하는 볼륨을 생성할 수도 있다.

<br>

### 2-1 호스트 볼륨 공유
```bash
# 명령어
docker run -d --name wordpressdb_hostvolume -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=wordpress -v /home/wordpress_db:/var/lib/mysql mysql:5.7

docker run -d -e WORDPRESS_DB_PASSWORD=password --name wordpress_hostvolume --link wordpressdb_hostvolume:mysql -p 80 wordpress
```
- 위의 경우 -v 옵션을 /home/wordpress_db:/var/lib/mysql로 추가한 경우 이는 호스트의 /home/wordpress_db 디렉터리와 컨테이너 /var/lib/mysql 디렉터리를 공유한다는 뜻이다.
  * [호스트의 공유 디렉터리]:[컨테이너의 공유 디렉터리] 형태이다.
  * 컨테이너의 /var/lib/mysql 디렉터리는 MySQL의 데이터베이스의 데이터를 저장하는 기본 디렉터리이다.

- 이 경우 미리 /home/wordpress_db 디렉터리를 호스트에 생성하지 않았어도 도커가 자동으로 이를 생성한다.

<br>

<br>

<br>

### [위로](#) / [뒤로](/README.md/#)