#pragma strict

var Counter : int = 0;
 
function Update () {
 Counter++;
 GetComponent.<GUIText>().text = "Counter is: "+Counter;
}