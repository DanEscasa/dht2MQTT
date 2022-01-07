# Adapted from https://RandomNerdTutorials.com/micropython-mqtt-publish-bme680-esp32-esp8266/
# for use with the DHT11 in place of the BME680, and broker.emqx.io in place of a local MQTT broker

# One thing I've changed is using tayfunulu's WiFi Manager at # https://github.com/tayfunulu/WiFiManager.
# In the “near future”, I'll add code to allow the user to change the default password

import time
from   umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import wifimgr
import esp
import dht
from   machine import Pin, I2C

esp.osdebug(None)
import gc
gc.collect()

wifimgr.get_connection()
mqtt_server = 'broker.emqx.io'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.106'

client_id = ubinascii.hexlify(machine.unique_id())

topic_pub_temp = b'esp/dht/temperature'
topic_pub_hum  = b'esp/dht/humidity'
# topic_pub_pres = b'esp/dht/pressure'
# topic_pub_gas  = b'esp/dht680/gas'

# last_message     = 0
message_interval = 30

# ESP32 - Pin assignment
#i2c = I2C(scl=Pin(22), sda=Pin(21))
# ESP8266 - Pin assignment
dhtSensor = dht.DHT11(machine.Pin(14))

def connect_mqtt():
  global client_id, mqtt_server
  client = MQTTClient(client_id, mqtt_server, user="emqx", password="public")
  client.connect()
  print('Connected to %s MQTT broker' % (mqtt_server))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

def read_dht_sensor():
  try:
    dhtSensor.measure()
    temp = (b'{:.2f}'.format(dhtSensor.temperature()))
    #temp = (b'{0:.2f}'.format((dhtSensor.temperature) * (9/5) + 32))
    hum = (b'{:.2f}'.format(dhtSensor.humidity()))
#    pres = (b'{:.2f}'.format(dhtSensor.pressure))
#    gas = (b'{:.2f}'.format(dhtSensor.gas/1000))
    
    return temp, hum
    #else:
    #  return('Invalid sensor readings.')
  except OSError as e:
    return('Failed to read sensor.')

try:
  client = connect_mqtt()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
#    if (time.time() - last_message) > message_interval:
    time.sleep(message_interval)
    temp, hum = read_dht_sensor()
    print(temp)
    print(hum)
#      print(pres)
#      print(gas)
    client.publish(topic_pub_temp, temp)
    client.publish(topic_pub_hum, hum)      
#    last_message = time.time()
  except OSError as e:
    restart_and_reconnect()
