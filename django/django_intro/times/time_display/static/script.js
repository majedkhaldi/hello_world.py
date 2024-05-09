let hrs = document.querySelector(".hrs")
let min = document.querySelector(".mins")
let sec = document.querySelector(".sec")



setInterval(()=>{
    var currenttime = new Date();
    // console.log(currenttime);
    hrs.innerHTML = currenttime.getHours();
    min.innerHTML = currenttime.getMinutes();
    sec.innerHTML = currenttime.getSeconds();
}, 1000)