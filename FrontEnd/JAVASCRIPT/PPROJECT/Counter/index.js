// console.log()
const countvalue = document.getElementById("count")
console.log(countvalue.textContent)
let c=0;    
function incre()
{
    c++;
    countvalue.textContent = c
}
function decre()
{
    c--;
    countvalue.textContent = c 
}
function reset(){
    c=0
    countvalue.textContent = c   
}



