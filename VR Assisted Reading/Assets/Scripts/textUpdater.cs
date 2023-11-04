using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
public class textUpdater : MonoBehaviour
{
    public TextMeshPro sampleText;
    public Button changeTextButton;
    private int i;
    private string[] newStringArray;

    // Start is called before the first frame update
    void Start()
    {
        i=0;
        List<string> newStringArray = new List<string>();
        var newString = "..And this is some new text";
        var newString2 = "..And this is some new text again!!!";
        newStringArray.Add(newString);
        newStringArray.Add(newString2);
        changeTextButton.onClick.AddListener(ButtonClickHandler);

    }

    // Update is called once per frame
    void Update()
    {

    }
    private void ButtonClickHandler()
    {
        // Handle the button click
        Debug.Log("pressed next button");
        Debug.Log("Text");
        sampleText.text = "New text!";
        i=i+1;
        // panel1.transform.position = Vector3.MoveTowards(panel1.transform.position, inactivePosition, 8);

        // panel2.transform.position = Vector3.MoveTowards(inactivePosition, readingPosition, 8);

    }
}

//code flows like a bath. all students begin to crash. yearning for that cash