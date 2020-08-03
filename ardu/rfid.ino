#include <SPI.h>
//#include <MFRC522.h>

#define SS_PIN 53
#define RST_PIN 5
 
//MFRC522 rfid(SS_PIN, RST_PIN); // Instance of the class


void setup()
{
  Serial.begin(9600);
  SPI.begin(); // Init SPI bus
  //rfid.PCD_Init(); // Init MFRC522

  // inicjalizacja pinów
  pinMode(12, OUTPUT); //Zielone dla pieszych
  pinMode(11, OUTPUT); //Czerwone dla pieszych
  pinMode(10, OUTPUT); //Czerwone dla samochodów
  pinMode(9, OUTPUT); //Żółte dla samochodów
  pinMode(8, OUTPUT); //Zielone dla samochodów
  pinMode(A5, OUTPUT); //sygnał dźwiękowy
  pinMode(7, INPUT_PULLUP); //Przycisk dla pieszych
}

// definicja nazw dla poszczególnych świateł i ich stanów

//piesi
#define P_LAMP_INFO_0 digitalWrite(6, LOW);
#define P_LAMP_ZIEL_0 digitalWrite(12, LOW); // oznacza piesi-lampa zielona-wyłączona itd.
#define P_LAMP_ZIEL_1 digitalWrite(12, HIGH);
#define P_LAMP_CZER_0 digitalWrite(11, LOW);
#define P_LAMP_CZER_1 digitalWrite(11, HIGH);
//samochody
#define S_LAMP_CZER_0 digitalWrite(10, LOW);
#define S_LAMP_CZER_1 digitalWrite(10, HIGH);
#define S_LAMP_ZOLT_0 digitalWrite(9, LOW);
#define S_LAMP_ZOLT_1 digitalWrite(9, HIGH);
#define S_LAMP_ZIEL_0 digitalWrite(8, LOW);
#define S_LAMP_ZIEL_1 digitalWrite(8, HIGH);
//sygnał dźwiękowy
#define SYGNAL_DZWIEKOWY_0 digitalWrite(A5, LOW);
#define SYGNAL_DZWIEKOWY_1 digitalWrite(A5, HIGH);

void stan_swiatel_01()
{
    P_LAMP_CZER_1; //Czerwone dla pieszych
    S_LAMP_CZER_0; //Czerwone
    S_LAMP_ZOLT_0; //Żółte
    S_LAMP_ZIEL_1; //Zielone
    P_LAMP_INFO_0; //Informacyjne dla pieszych
}

void stan_swiatel_02()
{
    P_LAMP_CZER_1; //Czerwone dla pieszych
    S_LAMP_CZER_0; //Czerwone
    S_LAMP_ZOLT_0; //Żółte
    S_LAMP_ZIEL_1; //Zielone
    P_LAMP_INFO_0; //Informacyjne dla pieszych
}

void stan_swiatel_03()
{
    P_LAMP_CZER_1; //Czerwone dla pieszych
    S_LAMP_CZER_0; //Czerwone
    S_LAMP_ZOLT_0; //Żółte
    S_LAMP_ZIEL_1; //Zielone
    P_LAMP_ZIEL_0; //Zielone dla pieszych
    SYGNAL_DZWIEKOWY_1; // sygnał dźwiękowy
}

void stan_swiatel_04()
{
    P_LAMP_CZER_1; //Czerwone dla pieszych
    S_LAMP_CZER_0; //Czerwone
    S_LAMP_ZOLT_1; //Żółte
    S_LAMP_ZIEL_0; //Zielone
    P_LAMP_ZIEL_0; //Zielone dla pieszych
    SYGNAL_DZWIEKOWY_1;// sygnał dzwiękowy
}

void stan_swiatel_05()
{
    P_LAMP_ZIEL_0; //Zielone dla pieszych
    P_LAMP_CZER_1; //Czerwone dla pieszych
    S_LAMP_CZER_1; //Czerwone
    S_LAMP_ZOLT_0; //Pomarańczowa
    S_LAMP_ZIEL_0; //Zielone
    SYGNAL_DZWIEKOWY_1;
}

void stan_swiatel_06()
{
    P_LAMP_ZIEL_1; //Zielone dla pieszych
    P_LAMP_CZER_0; //Czerwone dla pieszych
    S_LAMP_CZER_1; //Czerwone
    S_LAMP_ZOLT_0; //Żółte
    S_LAMP_ZIEL_0; //Zielone
    SYGNAL_DZWIEKOWY_1;// sygnał dzwiękowy
}

void stan_swiatel_07()
{
    P_LAMP_ZIEL_0; //Zielone dla pieszych
    P_LAMP_CZER_0; //Czerwone dla pieszych
    S_LAMP_CZER_1; //Czerwone
    S_LAMP_ZOLT_0; //Żółte
    S_LAMP_ZIEL_0; //Zielone
    SYGNAL_DZWIEKOWY_1; // sygnał dźwiekowy
}

void stan_swiatel_08()
{
    P_LAMP_ZIEL_1; //Zielone dla pieszych
    P_LAMP_CZER_0; //Czerwone dla pieszych
    S_LAMP_CZER_1; //Czerwone
    S_LAMP_ZOLT_0; //Żółte
    S_LAMP_ZIEL_0; //Zielone
    SYGNAL_DZWIEKOWY_1;//sygnał dźwiękowy
}

void stan_swiatel_09()
{
    P_LAMP_ZIEL_0; //Zielone dla pieszych
    P_LAMP_CZER_1; //Czerwone dla pieszych
    S_LAMP_CZER_1; //Czerwone
    S_LAMP_ZOLT_0; //Pomarańczowa
    S_LAMP_ZIEL_0; //Zielone
    SYGNAL_DZWIEKOWY_0;//sygnał dźwiękowy
}

void stan_swiatel_10()
{
    P_LAMP_ZIEL_0; //Zielone dla pieszych
    P_LAMP_CZER_1; //Czerwone dla pieszych
    S_LAMP_CZER_1; //Czerwone
    S_LAMP_ZOLT_1; //Pomarańczowa
    S_LAMP_ZIEL_0; //Zielone
}

void stan_swiatel_11()
{
    P_LAMP_ZIEL_0; //Zielone dla pieszych
    P_LAMP_CZER_1; //Czerwone dla pieszych
    S_LAMP_CZER_0; //Czerwone
    S_LAMP_ZOLT_0; //Żółte
    S_LAMP_ZIEL_1; //Zielone
}


void loop()
{
    stan_swiatel_01();

    //if ( ! rfid.PICC_IsNewCardPresent())
    // return; // przyłożenie karty

    delay(5000);

    stan_swiatel_02();

    stan_swiatel_03();
    delay(10000); //Czekamy na reakcję 10 sekund po naciśnięciu przycisku dla pieszych

    stan_swiatel_04();
    delay(2000); //Czekamy 2 sekundy po zapaleniu się żółtego dla pojazdów

    stan_swiatel_05();
    delay(2000); //Czekamy 2 sekundy po zapaleniu się czerwonego dla pojazdów i czerwonego dla przechodniów, zabezpieczenie przeciwwypadkowe

    stan_swiatel_06();
    delay(5000); //Czekamy 5 sekund, zielone dla przechodniów

    //MIGANIE ŚWIATEŁ (po 0.4 sekundy)
    stan_swiatel_07();
    delay(400);
    stan_swiatel_08();
    delay(400);
    stan_swiatel_07();
    delay(400);
    stan_swiatel_08();
    delay(400);
    stan_swiatel_07();
    delay(400);
    stan_swiatel_08();
    delay(400);
    stan_swiatel_07();
    delay(400);
    stan_swiatel_08();
    delay(400); 
    stan_swiatel_07();
    delay(400);

    stan_swiatel_09();
    delay(2000); //Czekamy 2 sekundy, czerwone dla wszystkich, zabezpieczenie przeciwwypadkowe, dla spóźnialskich pieszych

    stan_swiatel_10();
    delay(2000); //Czekamy 2 sekundy, światło czerwone i żółte dla pojazdów ruszających

    stan_swiatel_11();
    delay(500); //Pół sekundy - Określamy czas po którym przycisk dla pieszych znów jest aktywny

}

  
