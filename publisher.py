import paho.mqtt.client as mqtt
import time
import sys

BROKER = "test.mosquitto.org"
TOPICO_STATUS = "entrega/mensagens"

client = mqtt.Client(client_id="Mensagens_Publisher")

client.will_set(TOPICO_STATUS, payload="Offline (Falha Crítica)", qos=1, retain=True)

print("Conectando ao broker...")
client.connect(BROKER, 1883, 60)
client.loop_start()

print("Enviando status: Online (com retain=True)...")
client.publish(TOPICO_STATUS, payload="Online e Operando", qos=1, retain=True)

print("\nSensor rodando. ")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nSimulando queda de energia! O sensor morreu sem avisar.")
    sys.exit(1)