#pragma strict

function Start () {

}

function Update () {

}

function OnTriggerEnter() {
	Debug.LogWarning("Enter area where key is taken");
	}
function OnTriggerExit() {
	Debug.LogWarning("Left area where key is taken");
	}