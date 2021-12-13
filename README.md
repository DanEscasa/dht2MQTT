# dht to MQTT
This project is adapted from [Rui Santos's excellent tutorial](https://RandomNerdTutorials.com/micropython-mqtt-publish-bme680-esp32-esp8266/), using the DHT11 in place of the BME680, and [broker.emqx.io](broker.emqx.io) in place of a local MQTT broker.

Also, in contrast to the post at RandomNerdTutorials.com, I've combined all the code into one file. At RNT, Rui separates these into boot.py and main.py. In the “near future”, I'll probably do the same.

One other thing I've changed is using [tayfunulu's WiFi Manager](https://github.com/tayfunulu/WiFiManager) instead of hard-coding the WLAN credentials. Also in the “near future”, I'll add code to WiFi Manager to allow the user to change the default password.

In addition to [Node-RED](https://nodered.org/), I also used [MQTT X](https://mqttx.app/), an MQTT desktop client, and the Android app [MQTT Dash](https://play.google.com/store/apps/details?id=net.routix.mqttdash&hl=en&gl=US). In the “near future”, I'll install the [iOS version](https://apps.apple.com/us/app/mqttool/id1085976398). Below are their respective screenshots.

| ![Screenshot NODE-Red](https://user-images.githubusercontent.com/8016816/145812766-30bba930-e1a7-4a7e-9917-fa71f7a379e2.png)|
|:--:| 
| NODE-Red |

| ![Screenshot MQTTX](https://user-images.githubusercontent.com/8016816/145812798-cf28e0b0-d2b3-40d1-b2b1-30cc00bbcac4.png) |
|:--:| 
| MQTTX |

|![Screenshot MQTT Dash](https://user-images.githubusercontent.com/8016816/145812821-b54d5402-2677-4904-928e-3c2174015eb2.jpg) |
|:--:| 
| MQTT Dash |

