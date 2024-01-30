console.log("hello world");
// single line commment ur mom // 
/* 
multi line comment 
*/ 
var avariable = 'hello world';


console.log(avariable);
console.log(2*(3+2));
// arethmitic



var greeting = function() {
    var number1 = 6;
    var number2 = 7;
    var total = (number1 + number2);
    console.log("total: " + total);
    // any functions
}

greeting();

var foo =  "hello";
var bar = 'worlds';
 
console.log( foo + " " + bar + "!");

console.log(2 * 5);
console.log(2/3);

var i = 1;
var j = ++i;
var k = i++;
// increment and decrememt 


console.log("i:", i, "\n","j:", j,"\n", "k:", k);
//  introduced \n for new lines and used, to seperatethe print

var aNumber = 1;
var anotherNumber = '2'; 

console.log(aNumber + anotherNumber);// error message because it is reading both numbers as a string because console.log() reads as a string if both not shown as int

console.log(aNumber + Number(anotherNumber));

var a = 1; 
var b = 0;
var c = 2;

console.log(a || b);// '||' = OR
console.log(c && b);//  '&&' = AND
//! is NOT 
// boolean values 

/*  
== represents eqaul to
!= represents NOT equal to
>= greater than or equal to
<= Less than or equal to
*/ 

var jeffery;
jeffery = 5;
if(jeffery < 5) {
    console.log("jeff is less than five ");
} else if(jeffery > 5)  {
    console.log("jeff is greater than 5");
}else {
    console.log("JEFF IS 5!!!!!");
}


var anArray = [];
// initialize and empty array 
var anObject = {};
// initialize and empty object 


achoice = "choice ";

switch(achoice) {
    case 'choice 2':
        console.log("Choice 2 was selected");
    break;

    case 'choice 1':
        console.log("Choice 1 was selected");
    break;
    
    default:
        console.log("Default alert was executed");
    break;
}
