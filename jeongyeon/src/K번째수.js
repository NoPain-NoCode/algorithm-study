function solution(array, commands) {
    var answer = [];
    commands.forEach(element => {
        let i=element[0], j=element[1], k=element[2];
        let new_array = array.slice(i-1,j).sort((a, b) => a - b);
        answer.push(new_array[k-1]);
    })
    return answer;
}