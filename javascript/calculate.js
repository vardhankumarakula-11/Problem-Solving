let btns = document.getElementsByClassName("btns")
let display = document.getElementById("display")
let res = ""

for(let i of btns){
    i.onclick = function(){
        if(i.textContent=="DEL"){
            res = res.substring(0,res.length-1)
        }else if(i.textContent=="C"){
            res = ""
        }else if(i.textContent=="="){
            res = eval(res)
        }else{
            res+=i.textContent
        }
        if(res==""){
            display.textContent = "0"
        }else{
            display.textContent = res
        }
    }
}