var myArray =["hello","world"];
console.log(myArray[0]);
// arrays with info 

for (var i = 1;  i<6; i++) {
    console.log(i)
}
// for loop


var j = 1;
while(j<10){
    console.log("currently at: " + j)
    j++;
}
// while loops

var k = 0;
do {
    k--;
    console.log("K:"+k);
    if(k== -15){
        break;
    } 
}while(true);
// do while 

var myObject = {
    sayHello : function() {
        console.log("Hello has been said");
    },
    addNumber : function(number1, number2) {
        total = number1 + number2;
        return total;
    },
    myName : "Joaquin", 
    myLastName : "Camaran"
}

console.log(myObject.addNumber(1,2))

console.log(myObject.sayHello())

console.log(myObject.myLastName)