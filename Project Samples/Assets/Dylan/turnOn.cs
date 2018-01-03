using UnityEngine;
using System.Collections;
using UnityEngine.UI;


public class turnOn : MonoBehaviour 
{

	public GameObject object1;

	void Start ()
	{
		GameObject.Find ("resumeOne").SetActive(false);
	}

	void OnMouseDown()
	{
		object1.SetActive(!object1.activeSelf);
	}
}


