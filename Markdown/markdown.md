# **마크다운 문법**

## **-INDEX-**
1. [Heading](#heading--문서의-제목이나-소제목)
2. [list](#list--목록)
3. [Fencen Code block](#fencen-code-block--코드-블록)
4. [Inline Code block](#inline-code-block--코드-블록)
5. [Link](#link--링크)
6. [image](#6-image--이미지)
7. [Blockquotes](#7-blockquotes--인용문)
8. [table](#8-table--테이블)
9. [Horizontal Rule](#9-horizontal-rule--수평선)

---
<br>

## **1. Heading : 문서의 제목이나 소제목**

* `#`의 개수에 따라 대응되는 수준(Heading level)이 있으며, h1 ~ h6까지 표현 가능하다.

* 문서의 구조를 위해 작성되며 **`글자 크기를 조절하기 위해 사용되어서는 안된다.`**

<br>

## **2. list : 목록**

* 순서가 있는 리스트(ol)와 순서가 없는 리스트(ul)로 구성된다.

* Tab으로 하위 항목으로 구성할 수 있다. (나갈땐 `Shift + tab`)

* `Asterisk(*) Hyphen(-)` 을 통해서도 가능하다.

### **2~3번 적용 예시**

* firstitem
  * first - 1
  * first - 2
* seconditem
  * second - 1

<br>

## **3. Fencen Code block : 코드 블록**

* 코드블록은 `backtick` `(```)` 기호 3개를 활용하여 작성이 가능하다.

* 코드 블록에 특정 언어를 명시하면 Syntax Highlighting 적용할 수 있다.

<br>

### **적용 예시 (python 사용)**
```python
print('hello')
# 주석
```

### **적용 예시 (html 사용)**
```html
<!-- 주석 -->
```

<br>

## **4. Inline Code block : 코드 블록**

* 코드 블록은 `backtick` `(``)` 기호를 인라인에 활용하여 작성이 가능하다.

<br>

## **그 외 텍스트 강조**

* Itaic(기울임) : 양쪽 끝에 `Asterisk(*) 또는 Underscores(_)`를 `한개씩 만` 두어 특정 글자들을 기울게 만들 수 있다.

* Bold(굵게) : 양쪽 끝에 `Asterisk(*) 또는 Underscores(_)`를 `두개씩` 두어 특정 글자들을 굵게 만들 수 있다. 

### **적용 예시**
* *italicized text*
* **bold text**

<br>

## **5. Link : 링크**

* `[문자열](url)`을 통해 링크 작성이 가능하다.
* **url** 자리에 **파일**이나 **폴더**를 입력해 불러올 수도 있다.

### **적용 예시**
[Google](https://google.com)

[NAVER](https://naver.com)

<br>

## **6. image : 이미지**

* `![문자열](url)`을 통해 이미지를 사용할 수 있다.
  * (Link와 유사하되 [ ]앞에 !가 붙는다)
* 특정 파일들 포함하여 연결 시킬 수도 있다. **(위치 중요)**

### **적용 예시**
![이미지](K-001.png)

<br>

## **7. Blockquotes : 인용문**

* `>`으로 인용문을 작성할 수 있다.

### **적용 예시**
> Blockquotes

<br>

## **8. Table : 테이블**

* `Vertical bar(|)` 와 `Hyphen(-)` 를 이용하여 표 작성이 가능하다.

### **적용 예시**
| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text |

<br>

## **9. Horizontal Rule : 수평선**

* 3개 이상의 `Asterisk(*) , Hyphen(---), Underscores(_)`을 사용한다.

### **적용 예시**
---
***
___

<br>

<br>

<br>

### [위로](#마크다운-문법) / [뒤로](/README.md/#)