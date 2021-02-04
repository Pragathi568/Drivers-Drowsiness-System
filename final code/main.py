from blink_detection import count_blinks
from detect_drowsiness import detect_drowsiness
import playsound
l = []
#EYE_AR_CONSEC_FRAMES=3
#EYE_AR_CONSEC_FRAMES=0.3
while True:
    if count_blinks() < 15:
        print('*'*5 + ' ALERT '+'*'*5)
        playsound.playsound('C:/Users/MY PC/Desktop/final code/alarm.wav')
        if detect_drowsiness() > 3:
            print('*'*5 + ' ALERT '+'*'*5)
            playsound.playsound('C:/Users/MY PC/Desktop/final code/alarm.wav')
            break
            
    
 #EYE_AR_CONSEC_FRAMES   


