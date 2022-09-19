const int led=7;
const int fan=11;
const int PIR=8;
const int buzz=5;

void setup()
{
  pinMode(led,OUTPUT);
  pinMode(PIR,INPUT);
  pinMode(buzz,OUTPUT);
}

void light(){
  int light=analogRead(A1);
  if(light<500){
  digitalWrite(led, LOW);
  }else{
  digitalWrite(led, HIGH);
  }
}
void fanFunction(){
  int temperature=analogRead(A5);
  int volt=temperature*5.0/1023.0;
  int range=(volt-0.5)*100;
  if(range>25){
    digitalWrite(fan,HIGH);
  }else{
    digitalWrite(fan,LOW);
  }
}

void motionDetector(){
  int state=digitalRead(PIR);
  if(state==HIGH){
    tone(buzz,500,1000);
    delay(1000);
  }else{
    noTone(buzz);
  }  
}

void loop()
{ 
  light();
  fanFunction();
  motionDetector(); 
}