import paho.mqtt.client as mqttClient
import time
 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
        print("Connect to client1")
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection Error!")
 
def on_message(client, userdata, message):
    print (&quot;Message received: &quot;  + message.payload)
 
Connected = False   #global variable for the state of the connection
 
broker_address= "localhost"  #Broker address
port = 1883                     #Broker port
user = "client1"                   #Connection username
password = "123456"            #Connection password
 
client = mqttClient.Client(&quot;Python&quot;)               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
 
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
client.subscribe(&quot;python/test&quot;)
 
try:
    while True:
        time.sleep(1)
 
except KeyboardInterrupt:
    print &quot;exiting&quot;
    client.disconnect()
    client.loop_stop()