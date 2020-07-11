## Messenger
Simple messenger with using Flask and Qt. First experiense.


### Some pictures
![Start and login](https://github.com/alina-andreevna/simple_messenger/blob/master/screenshoots/im1.jpg)
![Wrong password](https://github.com/alina-andreevna/simple_messenger/blob/master/screenshoots/im2.jpg)

### Inside
- server.py - server side of the application with sending history, and authorization requests
- sender.py - sending messages to the server through the console, authorization check
- receiver.py - show last messages in console
- messenger.py - algorithm of GUI client 
- client_ui.py - GUI client on Qt
- client.py - server request template

### How to use
- launch server.py
- **to use console:** launch sender.py and receiver.py
- **to use GUI:** launch messenger.py

### About
You can exchange messages inside one PC or inside the local network.
To do this, you need to run the server.py on one of the devices and the messenger.py on all devices from which communication will be conducted.

For authorization, you need to come up with a username and password that will be stored on the server. To reconnect, use the existing pair of username and password.
The names Jack and Mary are reserved to simulate chatting with the first connected person.
