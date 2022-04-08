#include "18F1330.h"
void RobotControl();
int black_threshold = 512 ;
int an[1];

void main (void)
{

Setup_18F1330();
while(true) 
 {
an [0] = Sample_ADC_Channel(0, 4);
RobotControl() ; 
delay(10); 
} 
} 

void RobotControl()
{ if (an[0] > black_threshold) {
    LED0 = 1; 
    LED1 = 0; 
    Set_PWM(0, 2000);
    Set_PWM(1, 500);
} else {
    LED0 = 0; 
    LED1 = 1; 
    Set_PWM(0, 500);
    Set_PWM(1, 2000);
}
}
