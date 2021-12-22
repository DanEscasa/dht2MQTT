# dht to MQTT
This project is adapted from [Rui Santos's excellent tutorial](https://RandomNerdTutorials.com/micropython-mqtt-publish-bme680-esp32-esp8266/), using the DHT11 in place of the BME680, and [broker.emqx.io](broker.emqx.io) in place of a local MQTT broker. An ESP32 takes temperature and humidity readings from the DHT11 and publishes those to EMQX.

Speaking of Rui's tutorial, you'll still download [umqttsimple.py](https://raw.githubusercontent.com/RuiSantosdotme/ESP-MicroPython/master/code/MQTT/umqttsimple.py). The other libraries should come with the standard ESP Micropython distribution. The other exception is wifimgr.py — refer to two paragraphs below for the source.

One thing I've changed is using [tayfunulu's WiFi Manager](https://github.com/tayfunulu/WiFiManager) instead of hard-coding the WLAN credentials. You'll have to download the .py from his repository. Also in the “near future”, I'll add code to WiFi Manager to allow the user to change the default password.

In addition to [Node-RED](https://nodered.org/), I also used the  MQTT desktop client [MQTT X](https://mqttx.app/) and the Android app [MQTT Dash](https://play.google.com/store/apps/details?id=net.routix.mqttdash&hl=en&gl=US). In the “near future”, I'll install the [iOS version](https://apps.apple.com/us/app/mqttool/id1085976398). Below are their respective screenshots.

| ![Screenshot NODE-Red](https://user-images.githubusercontent.com/8016816/145812766-30bba930-e1a7-4a7e-9917-fa71f7a379e2.png)|
|:--:| 
| NODE-Red |

| ![Screenshot MQTTX](https://user-images.githubusercontent.com/8016816/145812798-cf28e0b0-d2b3-40d1-b2b1-30cc00bbcac4.png) |
|:--:| 
| MQTTX |

|![Screenshot MQTT Dash](https://user-images.githubusercontent.com/8016816/145812821-b54d5402-2677-4904-928e-3c2174015eb2.jpg) |
|:--:| 
| MQTT Dash |

