# dht to MQTT
In this project, an ESP32 takes readings from a DHT11 temperature and humidity sensor and publishes those to EMQX. This project is adapted from [Rui Santos's excellent tutorial](https://RandomNerdTutorials.com/micropython-mqtt-publish-bme680-esp32-esp8266/), using the DHT11 in place of the BME680, and [broker.emqx.io](broker.emqx.io) in place of a local MQTT broker. You'll need to download the MQTT library [umqttsimple.py](https://raw.githubusercontent.com/RuiSantosdotme/ESP-MicroPython/master/code/MQTT/umqttsimple.py) from that tutorial.

I also used [tayfunulu's WiFi Manager](https://github.com/tayfunulu/WiFiManager) instead of hard-coding the WLAN credentials. All you need do is download the .py from his repository. Also in the “near future”, I'll add code to WiFi Manager to allow the user to change the default password.

The other libraries should come with the standard ESP Micropython distribution.

In addition to [Node-RED](https://nodered.org/), I also used the Linux desktop client [MQTT X](https://mqttx.app/) and the Android app [MQTT Dash](https://play.google.com/store/apps/details?id=net.routix.mqttdash&hl=en&gl=US). In the “near future”, I'll try out the [iOS version](https://apps.apple.com/us/app/mqttool/id1085976398). Below are their respective screenshots.

| ![Screenshot NODE-Red](https://user-images.githubusercontent.com/8016816/145812766-30bba930-e1a7-4a7e-9917-fa71f7a379e2.png)|
|:--:| 
| NODE-Red |

The best way to learn to get this output is by following Rui's instructions in his tutorial, omitting the steps for pressure and gas. You can also take the easy way out and import this repository's flows.json.

| ![Screenshot MQTTX](https://user-images.githubusercontent.com/8016816/145812798-cf28e0b0-d2b3-40d1-b2b1-30cc00bbcac4.png) |
|:--:| 
| MQTTX |

| <img src=https://user-images.githubusercontent.com/8016816/145812821-b54d5402-2677-4904-928e-3c2174015eb2.jpg width="300"> |
|:--:| 
| MQTT Dash |

As an aside, those screenshots are more-or-less to scale. Yes, I have a big-screen phone — 6.44".

ACKNOWLEDGEMENTS

Thanks to Michael Polla for his [gist](https://gist.github.com/MichaelPolla/a65ac84286ab523603e64549f9850223) on resizing image files in, among others, a github README.md

I also got the idea of using tables to insert an image caption from a [post in towardsdev.com](https://towardsdev.com/3-ways-to-add-a-caption-to-an-image-using-markdown-f2ca30562be6)
