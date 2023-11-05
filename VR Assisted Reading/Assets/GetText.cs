using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;
using System.Linq;

public class GetText : MonoBehaviour
{
    public Transform contentWindow;
    public GameObject recallTextObject;

    public GameObject content;

   
    void Start()
    {
        string readFromFilePath = Application.streamingAssetsPath + "/RecallChat/loremipsum.txt";
        string[] fileLines = File.ReadAllLines(readFromFilePath);
        Debug.Log("Tester");
        //Debug.Log(fileLines);

        foreach (string line in fileLines)
        {
            Debug.Log(line);
            GameObject newTextObject = new GameObject("RecallObject");
            newTextObject.transform.SetParent(content.transform);
            Text textComponent = newTextObject.AddComponent<Text>();
            textComponent.text = line;

            Font ArialFont = (Font)Resources.GetBuiltinResource(typeof(Font), "Arial.ttf");
            textComponent.font = ArialFont;
            textComponent.material = ArialFont.material;
            
            /* if (textComponent != null)
            {
                textComponent.text = line;
            }
            else
            {
                Debug.LogError("Text component not found on the instantiated object.");
            }*/
            
        }
    }
}
