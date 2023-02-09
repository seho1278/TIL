## Workbench 활용 MySQL 접속 방법
1. MySQL Workbench 8.0 CE 실행

2. MySQL Connections 밑에 있는 Local instance MySQL80 실행(비밀번호 입력)

## Workbench DB 추가
1. Administration -> Data Import/Restore

2. Import from Self-Contained File 체크 -> . 클릭 -> 다운로드 받은 파일 선택 -> Start Import
* 성공시 Import Completed 확인

## 추가된 DB 확인
1. Schemas 클릭 -> 새로고침 버튼 클릭 -> 추가된 데이터베이스 확인

## 실습 데이터베이스에 대한 쿼리(Query)문 작성 및 쿼리문 실행 방법

1. 데이터베이스 선택(더블클릭)

2. Query 에디터 클릭

3. 쿼리문 입력
```
SELECT * FROM customers;
```
4. 쿼리 실행(상단의 번개모양 아이콘 클릭)

5. 출력 확인