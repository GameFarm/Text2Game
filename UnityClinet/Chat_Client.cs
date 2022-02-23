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
    string serverIP = "127.0.0.1";
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
            receivedBuffer = new byte[1024];
            stream.Read(receivedBuffer, 0, receivedBuffer.Length);
            string msg = Encoding.UTF8.GetString(receivedBuffer, 0, receivedBuffer.Length);
            Debug.Log(msg);
            Array.Clear(receivedBuffer, 0, receivedBuffer.Length);
        }

        if (Input.GetKey(KeyCode.S))
        {
            send_message("sentiment, 오늘 너무 기분이 좋아.");
        }
        if (Input.GetKey(KeyCode.E))
        {
            send_message("emotion, 오늘 너무 기분이 좋아.");
        }
        if (Input.GetKey(KeyCode.C))
        {
            send_message("context, 오늘 너무 기분이 좋아.");
        }
        if (Input.GetKey(KeyCode.Q))
        {
            send_message("question, 오늘 너무 기분이 좋아.");
        }
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
