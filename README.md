# how to add video

## youtube에서 video_id 를 확인 

`cur-list.yml` 에서 
- vid는 youtube의 video_id에 해당한다.
- uid는 md파일의 이름에 해당한다. 적당한 구분할 수 있는 이름으로 지정한다. 
- default: true이면 앱 첫 화면의 리스트에 나온다  

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


