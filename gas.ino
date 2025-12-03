#include <ESP8266WiFi.h>

String apiKey = "MR4AJKG0UZCDQ867";      // your ThingSpeak WRITE API key
const char* ssid = "A7";
const char* password = "00000000";

const char* server = "api.thingspeak.com";

int gasPin = A0;   // Analog pin for MQ sensor
WiFiClient client;

void setup() {
  Serial.begin(9600);

  pinMode(gasPin, INPUT);

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi connected");
}

void loop() {
  int gasValue = analogRead(gasPin);  // Read MQ sensor

  Serial.print("Gas Value: ");
  Serial.println(gasValue);

  if (client.connect(server, 80)) {
    String postStr = apiKey;
    postStr += "&field1=";
    postStr += String(gasValue);

    client.print("POST /update HTTP/1.1\n");
    client.print("Host: api.thingspeak.com\n");
    client.print("Connection: close\n");
    client.print("X-THINGSPEAKAPIKEY: " + apiKey + "\n");
    client.print("Content-Type: application/x-www-form-urlencoded\n");
    client.print("Content-Length: ");
    client.print(postStr.length());
    client.print("\n\n");
    client.print(postStr);

    Serial.println("Data sent to ThingSpeak");
  }

  client.stop();

  // ThingSpeak free account limit: 15 seconds
  delay(2000);
}
