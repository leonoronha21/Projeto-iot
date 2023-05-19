//Programa: Como fazer um LED piscar no ritmo da musica
//Autor: MakerHero
 
#include <Adafruit_NeoPixel.h>
#ifdef _AVR_
#include <avr/power.h>
#endif
 
 
int nleds = 12; // Numero de LEDs na fita
int pinoLED = 6; // Pino que vai enviar os dados para a fita de LED
int pinosom = A5; // Pino que recebe a entrada analogica do sensor de som
 
Adafruit_NeoPixel pixels=Adafruit_NeoPixel(nleds,pinoLED,NEO_GRB+NEO_KHZ800); // Define com a biblioteca o tipo de fita de LEDs que voce esta usando
 
 
void setup()
{
  pixels.begin();
  pixels.setBrightness(0);  
  pinMode(pinosom, INPUT); // Define o pino de entrada do sensor de somgg
   
}
 
int brilho =5; //define o brilho do led
//int valorsilencio=0;
//int valormusica=255;
 
void loop(){
  int som = analogRead(pinosom); //Lê o valor da porta analógica do sensor de som
   brilho = som/2; // Passa o valor lido pelo som para definir o brilho dos LEDs
    ////brilho = map(som,valorsilencio,valormusica,0,240); // Opção para um ajuste mais fino do brilho
   
  pixels.setBrightness(brilho); // Passa para os LEDs o var da variável brilho
   
  for (int i=0;i<nleds;i++){
    pixels.setPielColor(i,pixels.Color(0,255,0)); // Marca todos os nleds com a cor 
  }
  pixels.show();
 
}