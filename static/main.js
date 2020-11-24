function getTime() {
    var today = new Date();
    var hours = today.getHours();
    var minutes = today.getMinutes();
    var seconds = today.getSeconds();
    minutes = checkTime(minutes);
    seconds = checkTime(seconds);

    var militaryTime = hours + ":" + minutes + ":" + seconds;
    document.getElementById('time').innerHTML = toStandardTime(militaryTime);

    var timeout = setTimeout(getTime, 500);
}

function checkTime(i){
    if (i < 10) {i = "0" + i}
    return i;
}

function toStandardTime(militaryTime) {
    militaryTime = militaryTime.split(':');
    return (militaryTime[0].charAt(0) == 1 && militaryTime[0].charAt(1) > 2) ? (militaryTime[0] - 12) + ':' + militaryTime[1] + ':' + militaryTime[2] + ' P.M.' : militaryTime.join(':') + ' A.M.';
}