using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class mi : MonoBehaviour
{
    // Start is called before the first frame update
    void Awake()
    {
        
    }
    public void Start()
    {
        Invoke("MakeGuiding", .1f);
    }

    // Update is called once per frame
    void MakeGuiding()
    {
        Application.LoadLevel("guide");
    }
}
