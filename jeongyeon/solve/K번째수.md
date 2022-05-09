# 프로그래머스
- K번째 수
  - [URL](https://programmers.co.kr/learn/courses/30/lessons/42748?language=javascript)   

### 문제 이해하기
배열의 i번째 수부터 j번째 수까지 자르고 정렬 했을 때,

k번째에 있는 수를 구한다. 

array 가 들어오고 [1,5,2,6,3,7,4]

배열이 들어있는 배열 commands가 들어온다

[i,j,k] 라면 i번째부터 j까지 자르고 k번째 수가 결과다. 

그 모든 k들의 집합을 반환한다. 

### 문제 접근 방법
commands배열 순회하면서 i부터 j까지 자르고 sort한 후 k번째 인걸 answer array에 넣는다.



### 구현 배경 지식
sort() 와 forEach() 를 사용했다. 

### 접근 방법을 적용한 코드
```
```
### 해결하지 못한 이유

### 문제를 해결한 코드
```
function solution(array, commands) {
    var answer = [];
    commands.forEach(element => {
        let i=element[0], j=element[1], k=element[2];
        let new_array = array.slice(i-1,j).sort((a, b) => a - b);
        answer.push(new_array[k-1]);
    })
    return answer;
}
```

### 문제를 해결한 방법
블로그에 좀 더 자세히 정리했다
[[프로그래머스]정렬 | K번째 수 JS 풀이](https://developer-jeongyeon.tistory.com/47)