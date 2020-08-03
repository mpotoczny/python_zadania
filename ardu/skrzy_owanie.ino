//deklaracje zmiennych i stanow w pliku decl.c
//#include "decl.c"
#include <SoftwareSerial.h>
//Create software serial object to communicate with SIM800L
SoftwareSerial mySerial(3, 2); //SIM800L Tx & Rx is connected to Arduino #3 & #2
void setup_GSM();
//RFID

#include <SPI.h>
#include <MFRC522.h>
#define RST_PIN A0 // Pin do resetowania RC522
#define SS_PIN  A1 // Pin dla SS (SDA) RC522
MFRC522 mfrc522(SS_PIN, RST_PIN);


//program sterujacy przejsciem dla pieszych 
//deklaracje wejsc
#define s_KL digitalRead(11)   //fizyczny aktualny stan klawisza dostępnego dla pieszych
char KL=0;                      //flaga klawisz KL był/nie byl nacisniety
#define s_KPB digitalRead(12)    //fizyczny aktualny stan klawisza wejscia w tryb programowania kart (brelokow)
char KPB=0;                      //flaga breloczek odczytany
char SMS=0;                       //flaga odbioru komendy SMS

//deklaracje wyjsc (sterowanie)
#define S_LC_1   digitalWrite(4,HIGH) //wlacz lampe czerwona dla samochodu        
#define S_LC_0   digitalWrite(4,LOW) //wylacz lampe czerwona dla samochodu  

#define S_LP_1   digitalWrite(5,HIGH) //wlacz lampe zolta/pomaranczowa dla samochodu        
#define S_LP_0   digitalWrite(5,LOW) //wylacz lampe zolta/pomaranczowa dla samochodu  

#define S_LZ_1   digitalWrite(6,HIGH) //wlacz lampe zielona dla samochodu        
#define S_LZ_0   digitalWrite(6,LOW) //wylacz lampe zielona dla samochodu  

#define P_LC_1   digitalWrite(7,HIGH) //wlacz lampe czerwona dla pieszego        
#define P_LC_0   digitalWrite(7,LOW) //wylacz lampe czerwona dla pieszego  

#define P_LZ_1   digitalWrite(8,HIGH) //wlacz lampe zielona dla pieszego        
#define P_LZ_0   digitalWrite(8,LOW) //wylacz lampe zielona dla pieszego  

#define BUZ_1   digitalWrite(9,HIGH) //wlacz piszczyk trybu programowania        
#define BUZ_0   digitalWrite(9,LOW) //wylacz piszczyk trybu programowania  

#define SPK_1   digitalWrite(10,HIGH) //wlacz dzwiek dla pieszego niewidomego        
#define SPK_0   digitalWrite(10,LOW) //wylacz dzwiek dla pieszego niewidomego

//stany automatu stanu

#define S    0   //samochody jada
#define KN   1   //klawisz nacisniety byl


#define S1  1   //samochody jada (wymuszenie SMS)
#define SP1 2   //cykl zalaczenia zielonego dla pieszych
#define SP2 3   //cykl zalaczenia zielonego dla samochodow
#define P   4   //piesi ida



char STAN = S;
//zmienne licznikowe czasu (cykl 500ms) 16 bitow max. 
#define T_LIM 1800 //15min
unsigned int volatile t_S;     

unsigned int volatile t_KN;
          
unsigned int volatile t_S1;
unsigned int volatile t_SP1;
unsigned int volatile t_SP2;
unsigned int volatile t_P;
unsigned int volatile t_GSM; //do odpytywania karty GSM


//GSM polaczenie  ARDUINO MEGA
//Rx2 Tx2 


void set_T1()
{ //ustaw przerwanie zegara T1 na 2Hz  https://www.instructables.com/id/Arduino-Timer-Interrupts/
cli();//stop interrupts
  TCCR1A = 0;// set entire TCCR1A register to 0
  TCCR1B = 0;// same for TCCR1B
  TCNT1  = 0;//initialize counter value to 0
  // set compare match register for 1hz increments
  //OCR1A = 15624;// = (16*10^6) / (1*1024) - 1 (must be <65536)
  OCR1A = 7812;// = 2Hz
  
  // turn on CTC mode
  TCCR1B |= (1 << WGM12);
  // Set CS10 and CS12 bits for 1024 prescaler
  TCCR1B |= (1 << CS12) | (1 << CS10);  
  // enable timer compare interrupt
  TIMSK1 |= (1 << OCIE1A);
sei();//allow interrupts
STAN=0;
}

ISR(TIMER1_COMPA_vect)
{//timer1 interrupt 2Hz odliczanie czasu 500ms
switch(STAN) {
  case S: if (t_S<T_LIM) t_S++; break;
  case S1: if (t_S<T_LIM) t_S++; break;
  case SP1: if (t_S<T_LIM) t_S++; break;
  case SP2: if (t_S<T_LIM) t_S++; break;
  case P: if (t_S<T_LIM) t_S++; break;


  case KN:  if (t_KN) t_KN--;
             }
t_GSM++; 
}

void setup() {

SPI.begin(); //inicjacja magistrali SPI
mfrc522.PCD_Init(); // inicjacja RC522
  setup_GSM(); //start karty GSM
  // put your setup code here, to run once:
t_S = 0;   //poczatek stanu samochody jada
set_T1();
}

void loop() {
  while(1)
  {
    if(s_KL) KL=0; else KL=1;
    if(SMS()        SMS_byl
    if(VIP)
  
  switch(STAN) {
  case S:  //samochody_jada 
           if(KL) { STAN=KN; t_KN= 15*2;}
           break;
  case KN://samochody_jada
          if(t_KN==0) STAN = sam pom piesi czerw ;
           break; 
  
  
  KL=0;  break;
  case SP1:                      KL=0;  break;
  case SP2:  break;
  case P:  break;
             }
 
 
 } //end while(1)
}

//https://lastminuteengineers.com/sim800l-gsm-module-arduino-tutorial/
//GSM 
void setup_GSM() //wyslanie testowego smsa 
{
  //Begin serial communication with Arduino and SIM800L
  mySerial.begin(9600);
  mySerial.println("AT"); //Once the handshake test is successful, it will back to OK
  delay(500);
  updateSerial();
  mySerial.println("AT+CMGF=1"); // Configuring TEXT mode
  delay(500);
  mySerial.println("AT+CMGS=\"+ZZxxxxxxxxxx\"");//change ZZ with country code and xxxxxxxxxxx with phone number to sms
  delay(500);
  updateSerial();
  mySerial.print("Last Minute Engineers | lastminuteengineers.com"); //text content
  delay(500);
  updateSerial();
  mySerial.write(26);
}
#if 0
void loop()
{
  updateSerial();
}
#endif

void updateSerial()
{
   while (Serial.available()) 
  {
    mySerial.write(Serial.read());//Forward what Serial received to Software Serial Port
  }
  while(mySerial.available()) 
  {
    Serial.write(mySerial.read());//Forward what Software Serial received to Serial Port
  }
}


void read_522() 
{
// Sprawdzamy, czy są nowe karty
   if ( mfrc522.PICC_IsNewCardPresent())
      {
      //odczyt karty
       if ( mfrc522.PICC_ReadCardSerial())
         {
          for (byte i = 0; i < mfrc522.uid.size; i++) {
           //Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? ” 0″ : ” „);
          //Serial.print(mfrc522.uid.uidByte[i], HEX);
          }
       //Serial.println();
       mfrc522.PICC_HaltA();
        }
     }
}
