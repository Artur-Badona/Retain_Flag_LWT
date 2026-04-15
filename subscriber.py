import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
TOPICO_STATUS = "entrega/mensagens"

def on_message(client, userdata, msg):
    print(f"\n[ALERTA] Mensagem recebida no tópico '{msg.topic}':")
    print(f"STATUS ATUAL: {msg.payload.decode()}")

def on_connect(client, userdata, flags, rc):
    print("Monitor conectado ao Broker!")
    client.subscribe(TOPICO_STATUS)
    print(f"Assinando o tópico: {TOPICO_STATUS}")

client = mqtt.Client(client_id="Mensagens_Subscriber")
client.on_connect = on_connect
client.on_message = on_message

print("Iniciando o Monitor...")
client.connect(BROKER, 1883, 60)

client.loop_forever()