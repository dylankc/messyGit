#pragma strict
import UnityEngine.UI;


public var textFile : TextAsset;
private var dialogLines : String [];
public var lineNumber : int;

public var uiText : Text;
public var canvas : Canvas;


//This script chooses the word from the assigned text file at 
//random within range (1, 164147) which is currently how many words in the file


function Start () 
{
	if (textFile)
	{
		dialogLines = (textFile.text.Split("\n"[0]));
	}
	
	
	
	
	
	
	
	if (lineNumber == 0)
	{
		lineNumber = Random.Range (0, 100);//164147);
	}
	
	var dialog : String = dialogLines[lineNumber];
	uiText.text = dialog;
	
	
	
}

function Empty ()
{
	
	}