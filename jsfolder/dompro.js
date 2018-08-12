var button12=document.getElementById('b1');
var sq=document.getElementsByTagName('td');

function Restart()
{
  for (var i = 0; i < sq.length; i++) {
    sq[i].textContent=" ";
  }
}
button12.addEventListener('click',Restart);

function sinfun(){
  this.textContent="x";
}

function dbfun(){
  this.textContent="0";
}

for (var i = 0; i < sq.length; i++) {
    sq[i].addEventListener('click',sinfun);
    sq[i].addEventListener('dblclick',dbfun);
  }
