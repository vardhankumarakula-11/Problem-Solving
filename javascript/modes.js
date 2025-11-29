
let text = document.getElementById("text")
let all = document.getElementById("all")
let btn = document.getElementById("btn")
let bd = document.getElementById("bd")
let mode = true;

function modeBtn(){
    if(mode==true){
    all.style.backgroundColor="Black"
    text.style.color = "white"
    text.textContent = "This is Dark Mode"
    btn.textContent = "Light"
    btn.style.backgroundColor = "white"
    btn.style.color = "black"
    bd.style.backgroundColor = "rgba(45, 47, 48, 1)"
    mode=false
    }else{
        all.style.backgroundColor = "White"
        text.style.color = "black"
        text.textContent = "This is Light Mode"
        btn.textContent = "Dark"
        btn.style.backgroundColor = "black"
        btn.style.color = "white"
        bd.style.backgroundColor = "rgba(232, 243, 245, 1)"
        mode = true
    }
}
