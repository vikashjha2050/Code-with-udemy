
var player1name=prompt("PLayer 1 name :");
var player2name=prompt("PLayer 2 name :");

$('h2').text(player1name + " will play");
$('.t1 tr').on('click',function(){
  var colindex=$('this').index();
  var rowindex=$('this').closest('tr').index();
  alert(rowindex+"hello"+colindex);
})
