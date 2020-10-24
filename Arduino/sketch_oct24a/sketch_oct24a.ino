# include <dht11.h>
# include <LiquidCrystal.h>
# define DTH11PIN 9

dht11 DHT11;

const int rs=12 , e=11 , d4=5 , d5=4 , d6=3 , d7=2;
LiquidCrystal lcd(rs,e,d4,d5,d6,d7);

const int rx=7 , tx=8;
SoftwareSerial esp(ex , tx)
void setup() {
  esp.begin(115200);
  
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Welcome to **HUB");
  lcd.setCursor(0, 1);
  lcd.print("You have to buy a premium to see");
  delay(2000);

}

void loop() {
  if(esp.available()>0){
    char check = esp.read();
    switch (check) {
      case 9 :
      fan = "OFF";
      break;
      case 8 :
      fan = "ON";
      break;
      case 7 :
      pump = "OFF";
      break;
      case 6 :
      pump = "ON";

    }
  
  
  
  
  
  
  
  
  int temp = getTemp();
  int hum = getHumidity();
  toLCD(temp , hum );
}

int getTemp(){
  int val = DHT11.read(DHT11PIN);
  return DHT11.temprature;
}

int getHumidity(){
  int val = DHT11.read(DHT11PIN);
  return DHT11.humidity;
}

void toLCD(int t ,int h){
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("T:");
  lcd.print(t);
  lcd.clear();
  lcd.setCursor(8, 0);
  lcd.print("FAN:");
  lcd.print(fan);
  lcd.setCursor(0, 1);
  lcd.print("H:");
  lcd.print(h);
  lcd.setCursor(8, 1);
  lcd.print("Pump:");
  lcd.print(pump);
 
}
}
