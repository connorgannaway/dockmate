const months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
const weekdays = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];

function getTime() {
    var today = new Date();
    var hours = today.getHours();
    var minutes = today.getMinutes();
    var seconds = today.getSeconds();
    var date = today.getDate();
    var day = weekdays[today.getDay()];
    var month = months[today.getMonth()];
    var year = today.getFullYear();
    minutes = checkTime(minutes);
    seconds = checkTime(seconds);

    var militaryTime = hours + ":" + minutes + ":" + seconds;
    document.getElementById('time').innerHTML = toStandardTime(militaryTime);
    document.getElementById('date').innerHTML = day + ", " + month + " " + date + " " + year;

    let timeout = setTimeout(getTime, 500);
}

function checkTime(i){
    if (i < 10) {i = "0" + i}
    return i;
}

function toStandardTime(militaryTime) {
    militaryTime = militaryTime.split(':');
    return (militaryTime[0].charAt(0) == 1 && militaryTime[0].charAt(1) > 2) ? (militaryTime[0] - 12) + ':' + militaryTime[1] + ':' + militaryTime[2] + ' P.M.' : militaryTime.join(':') + ' A.M.';
}