## 📌 Retain Flag

O **Retain Flag** avisa ao Broker MQTT para **salvar a última mensagem** publicada em um tópico. 

* **Como funciona:** Se o seu sensor publica "Ligado" com `retain=True`, o Broker guarda essa informação.
* **Para que serve:** Quando um novo cliente (como um app de celular) se conecta *depois* da publicação, ele recebe esse status guardado imediatamente. Ele não precisa esperar o sensor enviar uma nova atualização para saber como as coisas estão.

---

## 📜 LWT - Last Will and Testament

O **LWT** é uma mensagem de emergência que o dispositivo deixa engatilhada no Broker **no exato momento em que se conecta**.

* **Como funciona:** O dispositivo diz ao Broker: *"Se a minha conexão cair do nada, publique a mensagem 'Offline'"*.
* **Para que serve:** É a melhor forma de detectar quedas de energia, falta de internet ou travamentos. Como o dispositivo morre e não consegue avisar que caiu, o próprio Broker dispara o alerta pré-configurado.
