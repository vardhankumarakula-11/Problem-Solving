let fruits = ["apple","banana","mango","Orange","pineapple","goa","grepes"]
let ul = document.getElementById("ul");
let text = document.getElementById("text");
for(let i of fruits){
    let li = document.createElement("li");
    li.textContent = i;
    ul.appendChild(li)
}

function addBtn(){
    if(text.value==""){
        alert("Invalid input.")
        return
    }
    let li = document.createElement("li");
    li.textContent = text.value
    ul.appendChild(li);
    text.value = "";
}