// function kunal(){
//     console.log("kunal  function")
// }
// kunal()

// ^---------------------------------------------------------------------------------------------------

// function display(name){
//     console.log("JAVASCRIPT")
//     console.log(name)
// }
// console.log("Hello world")
// display("kunal");


// function can take parameter
// function display(n){
//     console.log(`my name is ${n}`)
// }
// display("kunal")


// WAP to take two number  and print its sum
// function sum1(a,b){
//     c=a+b
//     console.log(`sum is ${a} + ${b} =${c}`)

// }
// sum1(5,5)

// 
// function sum2(a,b){
//     console.log(a+b)
    
// }
// sum2(5,6,7)


// 
// function fun(a){
//     console.log(a)

// }
// fun(5,6,7)


// * what i can take all parameter  rest operator ....take all value
//rest operator is used to take multiple values  as array it is denoted by array 

// function fun(a,...b){
//     console.log(a,b)
// }
// fun(5,6,7,8,9)


// spread operator
// function spreadop(a,b){
//     const arr=[12,13,b,14]
//     console.log( a,b,arr)
// }
// spreadop(1,22,34,45,23,1)


// spread operator
// function fruits(a,...b){  //rest op
//     const newarr=[...b,"pineapple","chiku"] //spread op
//     return newarr
// }
// app=fruits("apple","mango","banana")
// console.log(app)

// function fun2(x,y,...z){
//     // console.log(...z,4,"kunal")
//     console.log(x,y,z)
//     let arr=[...z,4,"kunal"]
//     console.log(arr)

// }
// fun2(5,33,4,3,2,6,)

// function call return the value to the function paramater

// function calc(a,b){
//     return a+b

// }
// let x=calc(5,6)
// console.log(x)


// & DAY -2

// function sum(a,b){
//     console.log(a+b)
// }
// sum(4,5) // this give proper output 9
// sum(4) // this give an NAN beacuse b value is not defined 


// function kunal(a,b=5)
// {
//     console.log(a+b)

// }
// kunal(5,1)
// kunal(5)
// kunal(1)


// let a=10
// console.log(a) //
// a=20       // & re-assignment is possible 
// console.log(a)


// function respop(a,b,...z)
// {
//     let newArr=[...z,"kunal"]
//     console.log(newArr)
// }
// respop(2,3,4,5,6)

// interpreted as varibled by js engine

// function fun2(a,b){
//     console.log(a+b)

// }
// var fun3 = function (a,b) //function Expression 
// {
//     console.log(a+b)

// }
// let p=25
// console.log(fun3,p)
// print(p)

//^----------------------------------------------------------------------------------------------------
// Write the function mul which can take two value and print  there multiplication and also the function convert that function   into function Expreeesion 
// function mul(a,b)
// {
//     console.log(a*b)

// }
// mul(5,6)
// // console.log(mul)
// var mul = function (a,b)
// {
//     console.log(a*b)

// }
// mul(5,6)
// // console.log()


// function mul (a,b){
//     return a*b
// }
// mul(5,6)
// var mul= function(a,b)
// {
//     return a*b

// }
// mul(5,6);

//^----------------------------------------------------------------------------------------------------
//Arrow function   
// let fun4 = function(a,b)
// {
//     return a+b
// }
// let res =fun4(2,3)  //^ js madhe prathek value is let var const ne declare kara lagate
// console.log(res)

//Arrow function 
// let fun4 //& we can not redeclre the let varible 
// let fun5 =(a,b)=>{return a*b}
// let res2 = fun5(2,3)
// console.log(res2)

// let mul =(a,b)=>console.log(a,b)
// let res1= fun4(2,5)
// console.log(res1)  


// let sub =(a,b)=>a-b
// let res3=sub(10,5)
// console.log(res3)

// let square = (a)=>a*a
// let res5=square(5)
// console.log(res5)


//* Function with the function 
//^ function inside the function with closore
// function outer()
// {
//     let c=0
//     function inner()
//     {
//             c++;
//             console.log(c)
//     }
//     return inner;

// }
// let z=outer();
// console.log(z); //complete inner function is return 
// z()

// 

// ! Higher order  function 

// ! call back Function

// function x(){
//     console.log("Good")

// }
// function y(a,b){
//     x();
//     console.log(a)
// }
// y("boy",x)



// call back function

// function x()
// {
//     console.log("Good")

// }
// function y(a,b)
// {
//     b();
//     console.log(a)

// }
// y("boy",x)


// const fun6=() =>
// {
//     console.log("i am Fun6")
// }
// function  x(a,b){
//     b();
//     console.log()

// }
// fun6(5,fun6)

// console,log()

//* function is called with function inside the program
// function 

