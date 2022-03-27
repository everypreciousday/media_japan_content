# how to add video

## youtube에서 video_id 를 확인 

`cur-list.yml` 에서 
- vid는 youtube의 video_id에 해당한다.
- uid는 md파일의 이름에 해당한다. 적당한 구분할 수 있는 이름으로 지정한다. 그리고 유일해야 한다. 즉, 같은 노래에 대해 여러 아이템이 참조할 수 없다. ㅠㅠ(디비 설계상의 문제)
- default: true이면 앱 첫 화면의 리스트에 나온다  
- t1, t2는 쌍따옴표로 감싸줄 것. 

```
    dir: JPop
    uid: chara_i_miss_you
    vid: nBONQ1g7PZs
    ver: 1
    enabled: false
    default: false
    t1: "Chara I miss you"
    t2: "독특하고 몽환적인 목소리 Chara"
```

## 컨텐츠 준비 



먼저 다음과 같이 일본어와 한글을 준비한다. 
하나의 페이지는 `---`로 구분한다. 
```
あの<ruby>交差点<rt>こうさてん</rt></ruby>で
그 교차로에서
みんながもしスキップをして
만약 모두가 스킵을 하고
---
もしあの<ruby>街<rt>まち</rt></ruby>の<ruby>真<rt>ま</rt></ruby>ん<ruby>中<rt>なか</rt></ruby>で
만약 그 거리의 한가운데에서
<ruby>手<rt>て</rt></ruby>をつないで<ruby>空<rt>そら</rt></ruby>を<ruby>見上<rt>みあ</rt></ruby>げたら
손을 마주잡고 하늘을 올려다본다면
```

페이지의 상단에 

```
<h1>kyary_ponponpon.md</h1>
<h2>content</h2>
```

페이지 하단에 

```
<h2>end</h2>
```

모든 줄 끝에 `<br>`을 추가 

### 주의 

싱글쿼트(')는 쓰지 말것. 

That's -> That is 

## 폴더 관리 

`dir: JPop, dir:  JMedia` 같은 폴더는 동적으로 늘어난다. 

즉, github에서 추가하면 자동으로 앱에 반영된다. 

