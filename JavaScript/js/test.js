/*function addEven(x){
    let tot = 0
    for(i=x;i<100;i++){
        if(i%2==0)
            tot += i
    }
    return tot
}*/
//or

var sumEven = function(x){
    let tot = 0
    for(i=x;i<100;i++){
        if(i%2==0)
            tot += i
    }
    return tot
}

function sum(fun){
    let x = fun(20)
    console.log(x)
    x = fun(30)
    console.log(x)
}

sum(sumEven)
/*let x = "Hello"
    x = 100
console.log(x)
x = addEven(30)
console.log(x)*/