using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class panelSlider : MonoBehaviour
{
    public Button changeTextButton;
    public GameObject panel1;
    public float moveSpeed = 0.0f;    // Speed of movement
    // Start is called before the first frame update
    void Start()
    {
        changeTextButton.onClick.AddListener(ButtonClickHandler);
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    private void ButtonClickHandler()
    {
        Vector3 targetPosition = panel1.transform.position;

        // Move towards the target position
        StartCoroutine(MoveToTargetPosition(targetPosition));
    }
    private IEnumerator MoveToTargetPosition(Vector3 targetPosition)
    {
        var originalPosition = transform.position;
        while (transform.position != targetPosition )
        {
            Debug.Log(transform.position);
            Debug.Log(targetPosition);
            transform.position = Vector3.MoveTowards(transform.position, targetPosition, 10);
            panel1.transform.position = Vector3.MoveTowards(panel1.transform.position, originalPosition, 10);
            yield return null;
        }
    }
}
