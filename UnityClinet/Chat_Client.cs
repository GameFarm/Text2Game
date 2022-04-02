using System.Collections;
using System.Collections.Generic;
using System.Net.Sockets;
using UnityEngine;
using System.Text;
using System;
using System.IO;
using System.Runtime.InteropServices;

public class Chat_Client : MonoBehaviour
{
    TcpClient client;
    StreamReader reader;
    NetworkStream stream;
    string serverIP = "ip-172-31-23-109.us-east-3.compute.internal";
    int port = 8000;
    byte[] receivedBuffer;
    bool socketReady = false;


    void Start()
    {
        init_CheckReceive();
    }

    void Update()
    {
        if (stream.DataAvailable)
        {
            receivedBuffer = new byte[32];
            stream.Read(receivedBuffer, 0, receivedBuffer.Length);
            string msg = Encoding.UTF8.GetString(receivedBuffer, 0, receivedBuffer.Length);
            Debug.Log(msg);
            //Array.Clear(receivedBuffer, 0, receivedBuffer.Length);
        }

        if (Input.GetKey(KeyCode.S))
        {
            Delay(1000);
            send_message("sentiment,sentiment data");
        }
        if (Input.GetKey(KeyCode.E))
        {
            Delay(1000);
            send_message("emotion,emotion data");
        }
        if (Input.GetKey(KeyCode.C))
        {
            Delay(1000);
            send_message("context,context data");
        }
        if (Input.GetKey(KeyCode.Q))
        {
            Delay(1000);
            send_message("question,question data");
        }
    }
    private static DateTime Delay(int MS)
    {
        DateTime ThisMoment = DateTime.Now;
        TimeSpan duration = new TimeSpan(0, 0, 0, 0, MS);
        DateTime AfterWards = ThisMoment.Add(duration);

        while (AfterWards >= ThisMoment)
        {
            ThisMoment = DateTime.Now;
        }

        return DateTime.Now;
    }


    void init_CheckReceive()
    {
        if (socketReady) return;

        try
        {
            client = new TcpClient(serverIP, port);

            if (client.Connected)
            {
                stream = client.GetStream();
                Debug.Log("서버 연결 성공");
                socketReady = true;
            }
        }
        catch (Exception e)
        {
            Debug.Log("클라이언트 연결 에러 " + e);
        }
    }

    void send_message(string msg)
    {
        byte[] buff = Encoding.UTF8.GetBytes(msg);
        stream.Write(buff, 0, buff.Length);
        buff = new byte[32];
    }

    void CloseSocket() // Scene 종료시 호출
    {
        if (!socketReady) return;

        reader.Close();
        stream.Close();
        client.Close();
        socketReady = false;
    }
}
