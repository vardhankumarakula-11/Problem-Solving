let table = document.getElementById("table")
let username = document.getElementById("username")
let age = document.getElementById("age")
let city = document.getElementById("city")
let dlt = document.getElementById("dlt")
let update = document.getElementById("update")
let upd = document.getElementById("upd")

function getData(){
    let data = localStorage.getItem("data")
    if(data==null){
        return []
    }else{
        return JSON.parse(data)
    }
}

let arr = getData();

function tableHead(){
    let tr = document.createElement("tr")
    table.appendChild(tr)

    let th1 = document.createElement("th")
    th1.textContent = "username"
    tr.appendChild(th1)

    let th2 = document.createElement("th")
    th2.textContent = "age"
    tr.appendChild(th2)

    let th3 = document.createElement("th")
    th3.textContent = "city"
    tr.appendChild(th3)

}
tableHead()

for(let i of arr){
    tableData(i["username"],i["age"],i["city"])
}

function tableData(username,age,city){
    let tr = document.createElement("tr")
    table.appendChild(tr)

    let td1 = document.createElement("td")
    td1.textContent = username;
    tr.appendChild(td1)

    let td2 = document.createElement("td")
    td2.textContent = age;
    tr.appendChild(td2)

    let td3 = document.createElement("td")
    td3.textContent = city;
    tr.appendChild(td3)
}

function addBtn(){
    if(username.value=="" || age.value == "" || city.value==""){
        alert("Please Enter all detalis.")
        return
    }
    let obj = {
        "username" : username.value,
        "age" : age.value,
        "city" : city.value
    }
    arr.push(obj)
    localStorage.setItem("data",JSON.stringify(arr))
    tableData(username.value,age.value,city.value)
    username.value = ""
    age.value = ""
    city.value = ""

}

function delBtn(){
    if(dlt.value==""){
        alert("Please enter valid data")
        dlt.value = ""
        return
    }
    let indexValue;
    for(let i of arr){
        if(i["username"]==dlt.value){
            indexValue = arr.indexOf(i)
        }
    }

    if(indexValue==undefined){
        alert("user not found")
        dlt.value = ""
        return
    }

    arr.splice(indexValue,1)
    localStorage.setItem("data",JSON.stringify(arr))
    table.textContent = "";
    tableHead()
    for(let i of arr){
        tableData(i["username"],i["age"],i["city"])
    }
    dlt.value = ""
}

let indexValue;
function updateBtn(){
    if(update.value==""){
        alert("Enter a Valid Data")
        return
    }

    if(upd.textContent == "Save"){
        let new_obj={
            "username" : username.value,
            "age" : age.value,
            "city" : city.value
        }
        arr.splice(indexValue,1,new_obj)
localStorage.setItem("data",JSON.stringify(arr))
    table.textContent=""
    tableHead()
    for(let i of arr){
        tableData(i["username"],i["age"],i["city"])
    }

        username.value = ""
        age.value = ""
        city.value = ""
        update.value = ""
        upd.textContent = "Update"
        return
    }
    for(let i of arr){
        if(i["username"]==update.value){
            indexValue = arr.indexOf(i)
            username.value = i["username"];
            age.value = i["age"];
            city.value = i["city"]
        }
    }
    upd.textContent = "Save"
}