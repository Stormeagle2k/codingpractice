"use strict"
//console.log("Hello World");
const PI = 3.1415192
let pie =true
pie =24

function add(a,b){
    return a +b;
}

let result = add(1,5);
console.log(result);
function subtract(a,b){
     let result = a - b;
     return result;

}

console.log(subtract(5, 3));
function multiply(a,b){
    let result = a * b;
    return result;
}

function divide(a,b){
    let result = a/b;
    return result;
}

function exponent(a,b){
    let result = a **b
    return result;
}
console.log(exponent(5, 2),divide(15,3),multiply(3,3),subtract(72,3));

const car = {
    make: "voltswagon", 
    model: "passant",
    honk: function(){
        console.log("the " + this.make + " beep")
    }
};

function test(){car.honk()}

let ranger = (e)=>{
    e.preventDefault()
    console.log(e["number"])
    //const result = confirm('continue?');
    //console.log("result",result)
}

let crazy = "make";
car.honk()
console.log(car[crazy], car.model );