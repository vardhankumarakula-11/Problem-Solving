let display=document.getElementById("display")
let seconds=0
let minutes=0
let timer;
function startBtn(){
    timer=setInterval(function(){
        seconds++
        console.log(seconds)
        if(seconds==60){
            minutes++
            seconds=0
            
        }
        if(seconds<10){
            display.textContent="0"+minutes+":"+"0"+seconds

        }
        else if(minutes<10){
            display.textContent="0"+minutes+":"+seconds
        }else{
            display.textContent=minutes+":"+seconds
        }
    },1000)
}


function stopBtn(){
    clearInterval(timer)
}

function resetBtn(){
    minutes=0
    seconds=0
    display.textContent="00:00"
    clearInterval(timer)
}
