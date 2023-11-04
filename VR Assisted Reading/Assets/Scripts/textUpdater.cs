using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
public class textUpdater : MonoBehaviour
{
    public TextMeshProUGUI sampleText;
    public Button changeTextButton;
    public string newString;
    // Start is called before the first frame update
    void Start()
    {
        changeTextButton.onClick.AddListener(ButtonClickHandler);
        newString = "..And this is some new text";
    }

    // Update is called once per frame
    void Update()
    {

    }
    private void ButtonClickHandler()
    {
        // Handle the button click
        Debug.Log("Button Clicked!");
        sampleText.text = newString;

    }
}

//code flows like a bath. all students begin to crash. yearning for that cash