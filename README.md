# dht to MQTT
This project is adapted from [Rui Santos's excellent tutorial](https://RandomNerdTutorials.com/micropython-mqtt-publish-bme680-esp32-esp8266/), using the DHT11 in place of the BME680, and broker.emqx.io in place of a local MQTT broker

Also, in contrast to the post at RandomNerdTutorials.com, I've combined all the code into one file. At RNT, Rui separates these into boot.py and main.py. In the “near future”, I'll do the same.

One other thing I've changed is using [tayfunulu's WiFi Manager](https://github.com/tayfunulu/WiFiManager) instead of hard-coding the WLAN credentials. Also in the “near future”, I'll add code to allow the user to change the default password
