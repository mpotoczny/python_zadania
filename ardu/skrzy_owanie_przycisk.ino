#include <SoftwareSerial.h>
#include <Wire.h>
#include <RTClib.h>
RTC_DS1307 RTC;
#include <LiquidCrystal_I2C.h>
#define DS1307_I2C_ADDRESS 0x68
LiquidCrystal_I2C lcd(0x27,16,2);
char daysOfTheWeek[7][10] = {"NIEDZIELA", "PONIEDZIALEK", "WTOREK", "SRODA", "CZWARTEK", "PIATEK", "SOBOTA"};
char bufferRX[50];
void setup()
{
 
  Serial.begin(9600);
  Serial.println("Aby zaktualizować datę i godzinę, wyślij następujące polecenie: ");
  Serial.println("\"setDateTime rok, miesiac, dzien, godzina, minuta, sekunda\"");
  Serial.println("17:30 del 8 sett 2018");
  Serial.println("Przykład: setDateTime, 2018, 9, 8, 17, 30, 00");
  lcd.init();
  lcd.backlight();
  pinMode(12, OUTPUT); //Zielone dla pieszych
  pinMode(11, OUTPUT); //Czerwone dla pieszych
  pinMode(10, OUTPUT); //Czerwone dla samochodów
  pinMode(9, OUTPUT); //Żółte dla samochodów
  pinMode(8, OUTPUT); //Zielone dla samochodów
  pinMode(A5, OUTPUT); //sygnał dźwiękowy
  pinMode(7, INPUT_PULLUP); //Przycisk dla pieszych 
}

int i = 0;
void loop()

{

  
   for( i = 0; i < 10; i++ )
  {
    lcd.scrollDisplayLeft( );// pętla przesuwania się napisów na wyświetlaczu 
    delay( 500 );
  }
  delay( 1000 );
  for( i = 0; i < 12; i++ )
  {
    lcd.scrollDisplayRight( );
    delay( 500 );
  }
  
  delay( 1000 );
  static unsigned long updateTime;  
  if(millis() - updateTime > 1000){
    updateTime = millis();
    DateTime now = RTC.now();
    lcd.clear();
    lcd.setCursor(0, 0);
    LCDPrintNum(now.hour());
    lcd.print(":");
    LCDPrintNum(now.minute());
    lcd.print(":");
    LCDPrintNum(now.second());
    lcd.print(" ");  
    lcd.print(daysOfTheWeek[now.dayOfTheWeek()]);
    lcd.setCursor(0, 1);
    LCDPrintNum(now.day());
    lcd.print("/");
    LCDPrintNum(now.month());
    lcd.print("/");
    lcd.print(now.year(), DEC);
  }
  readSerial();  
}
void LCDPrintNum(int num){
  if(num <10)
    lcd.print("0");
  lcd.print(num);
}
void readSerial(){
  while (Serial.available() > 0) {  
    Serial.readBytesUntil('\n', bufferRX, sizeof(bufferRX) - 1);    
    if(strstr(bufferRX, "setDateTime,")){          
      int tdArray[6];  
      char * pch = strtok (bufferRX, " ,");
      unsigned int i = 0;
      while (pch != NULL){          
        if(i > 0)
          tdArray[i-1] = atoi(pch);
        pch = strtok (NULL, " ,");
        i++;
      }
      DateTime newTime = DateTime(tdArray[0], tdArray[1], tdArray[2], tdArray[3], tdArray[4], tdArray[5]);
      RTC.adjust(newTime);      
      Serial.println("Ustawiony nowy czas.");     
    
    
    }

    
  }








    

  
  digitalWrite(11, HIGH); //Czerwone dla pieszych
  digitalWrite(10, LOW); //Czerwone
  digitalWrite(9, LOW); //Żółte
  digitalWrite(8, HIGH); //Zielone
  digitalWrite(6, LOW); //Informacyjne dla pieszych

       
    if (digitalRead(7) == LOW) { //Jeśli przycisk dla pieszych zostanie wciśnięty
  
    digitalWrite(11, HIGH); //Czerwone dla pieszych
    digitalWrite(10, LOW); //Czerwone
    digitalWrite(9, LOW); //Żółte
    digitalWrite(8, HIGH); //Zielone
    digitalWrite(12, LOW); //Zielone dla pieszych
    digitalWrite(A5, HIGH);// sygnał dźwiękowy 
    delay(1000); //Czekamy na reakcję 10 sekund po naciśnięciu przycisku dla pieszych
      
      
      
      
      digitalWrite(11, HIGH); //Czerwone dla pieszych
    digitalWrite(10, LOW); //Czerwone
    digitalWrite(9, HIGH); //Żółte
    digitalWrite(8, LOW); //Zielone
    digitalWrite(12, LOW); //Zielone dla pieszych
    digitalWrite(A5, HIGH);// sygnał dzwiękowy 
    
    delay(2000); //Czekamy 2 sekundy po zapaleniu się żółtego dla pojazdów
      
      
      digitalWrite(12, LOW); //Zielone dla pieszych
    digitalWrite(11, HIGH); //Czerwone dla pieszych
    digitalWrite(10, HIGH); //Czerwone
    digitalWrite(9, LOW); //Pomarańczowa
    digitalWrite(8, LOW); //Zielone
             digitalWrite(A5, HIGH);

      
    delay(2000); //Czekamy 2 sekundy po zapaleniu się czerwonego dla pojazdów i czerwonego dla przechodniów, zabezpieczenie przeciwwypadkowe
      
      
    
    digitalWrite(12, HIGH); //Zielone dla pieszych
    digitalWrite(11, LOW); //Czerwone dla pieszych
    digitalWrite(10, HIGH); //Czerwone
    digitalWrite(9, LOW); //Żółte
    digitalWrite(8, LOW); //Zielone
             digitalWrite(A5, HIGH);// sygnał dzwiękowy 

    delay(5000); //Czekamy 5 sekund, zielone dla przechodniów
      
      
      
      
    digitalWrite(12, LOW); //Zielone dla pieszych
    digitalWrite(11, LOW); //Czerwone dla pieszych
    digitalWrite(10, HIGH); //Czerwone
    digitalWrite(9, LOW); //Żółte
    digitalWrite(8, LOW); //Zielone
    digitalWrite(A5, HIGH); // sygnał dźwiekowy 
    delay(400); //Czekamy 0,4 milisekund, zielone dla przechodniów zaczyna migać
      
        digitalWrite(12, HIGH); //Zielone dla pieszych
    digitalWrite(11, LOW); //Czerwone dla pieszych
    digitalWrite(10, HIGH); //Czerwone
    digitalWrite(9, LOW); //Żółte
    digitalWrite(8, LOW); //Zielone
    digitalWrite(A5, HIGH);//sygnał dźwiękowy 
    delay(400); //Czekamy 0,4 milisekund, zielone dla przechodniów zaczyna migać
      
        digitalWrite(12, LOW); //Zielone dla pieszych
    digitalWrite(11, LOW); //Czerwone dla pieszych
    digitalWrite(10, HIGH); //Czerwone
    digitalWrite(9, LOW); //Żółte
    digitalWrite(8, LOW); //Zielone
    digitalWrite(A5, HIGH);//sygnał dźwiękowy 
    delay(400); //Czekamy 0,4 milisekund, zielone dla przechodniów zaczyna migać
      
        digitalWrite(12, HIGH); //Zielone dla pieszych
    digitalWrite(11, LOW); //Czerwone dla pieszych
    digitalWrite(10, HIGH); //Czerwone
    digitalWrite(9, LOW); //Żółte
    digitalWrite(8, LOW); //Zielone
    digitalWrite(A5, HIGH);//sygnał dźwiękowy
    delay(400); //Czekamy 0,4 milisekund, zielone dla przechodniów zaczyna migać
      
        digitalWrite(12, LOW); //Zielone dla pieszych
    digitalWrite(11, LOW); //Czerwone dla pieszych
    digitalWrite(10, HIGH); //Czerwone
    digitalWrite(9, LOW); //Żółte
    digitalWrite(8, LOW); //Zielone
    digitalWrite(A5, HIGH);//sygnał dźwiękowy
    delay(400); //Czekamy 0,4 milisekund, zielone dla przechodniów zaczyna migać
      
        digitalWrite(12, HIGH); //Zielone dla pieszych
    digitalWrite(11, LOW); //Czerwone dla pieszych
    digitalWrite(10, HIGH); //Czerwone
    digitalWrite(9, LOW); //Żółte
    digitalWrite(8, LOW); //Zielone
    digitalWrite(A5, HIGH);//sygnał dźwiękowy
    delay(400); //Czekamy 0,4 milisekund, zielone dla przechodniów zaczyna migać
      
        digitalWrite(12, LOW); //Zielone dla pieszych
    digitalWrite(11, LOW); //Czerwone dla pieszych
    digitalWrite(10, HIGH); //Czerwone
    digitalWrite(9, LOW); //Żółte
    digitalWrite(8, LOW); //Zielone
    digitalWrite(A5, HIGH);//sygnał dźwiękowy
    delay(400); //Czekamy 0,4 milisekund, zielone dla przechodniów zaczyna migać
      
        digitalWrite(12, HIGH); //Zielone dla pieszych
    digitalWrite(11, LOW); //Czerwone dla pieszych
    digitalWrite(10, HIGH); //Czerwone
    digitalWrite(9, LOW); //Żółte
    digitalWrite(8, LOW); //Zielone
    digitalWrite(A5, HIGH);//sygnał dźwiękowy
    delay(400); //Czekamy 0,4 milisekund, zielone dla przechodniów zaczyna migać
      
        digitalWrite(12, LOW); //Zielone dla pieszych
    digitalWrite(11, LOW); //Czerwone dla pieszych
    digitalWrite(10, HIGH); //Czerwone
    digitalWrite(9, LOW); //Żółte
    digitalWrite(8, LOW); //Zielone
    digitalWrite(A5, HIGH);//sygnał dźwiękowy
    delay(400); //Czekamy 0,4 milisekund, zielone dla przechodniów zaczyna migać
      
      
      
      digitalWrite(12, LOW); //Zielone dla pieszych
    digitalWrite(11, HIGH); //Czerwone dla pieszych
    digitalWrite(10, HIGH); //Czerwone
    digitalWrite(9, LOW); //Pomarańczowa
    digitalWrite(8, LOW); //Zielone
    digitalWrite(A5, LOW);//sygnał dźwiękowy
      
    delay(2000); //Czekamy 2 sekundy, czerwone dla wszystkich, zabezpieczenie przeciwwypadkowe, dla spóźnialskich pieszych
      

    digitalWrite(12, LOW); //Zielone dla pieszych
    digitalWrite(11, HIGH); //Czerwone dla pieszych
    digitalWrite(10, HIGH); //Czerwone
    digitalWrite(9, HIGH); //Pomarańczowa
    digitalWrite(8, LOW); //Zielone
      
    delay(2000); //Czekamy 2 sekundy, światło czerwone i żółte dla pojazdów ruszających

    digitalWrite(12, LOW); //Zielone dla pieszych
    digitalWrite(11, HIGH); //Czerwone dla pieszych
    digitalWrite(10, LOW); //Czerwone
    digitalWrite(9, LOW); //Żółte
    digitalWrite(8, HIGH); //Zielone
    delay(500); //Pół sekundy - Określamy czas po którym przycisk dla pieszych znów jest aktywny
 
      
  
    }  }
