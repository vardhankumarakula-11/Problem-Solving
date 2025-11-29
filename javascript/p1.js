let text = document.getElementById("text")
let data = localStorage.getItem("text")
text.value = data
function saveBtn(){
    localStorage.setItem("text",text.value);
}
function clearBtn(){
    localStorage.removeItem("text");
    text.value = ""
}