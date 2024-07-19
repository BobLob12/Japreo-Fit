import streamlit as st
import streamlit_space as sy
import sys

import cv2
import mediapipe as mp
import numpy as np
import time

def Squats_Starting_Message(): 


 st.audio('App\pages\AudioCoach\Messages\Starting_Squats_Message.mp3',  autoplay= True)



if __name__ == '__Squats_Starting_Message__':
    Squats_Starting_Message()











def Deadlift_Starting_Message(): 


 st.audio('App\pages\AudioCoach\Messages\Starting_Deadlift_Message.mp3',  autoplay= True)



if __name__ == '__Deadlift_Starting_Message__':
    Deadlift_Starting_Message()

    
   








def Leg_Lunges_Starting_Message(): 


 st.audio('App\pages\AudioCoach\Messages\Starting_Leg_Lunges_Message.mp3',  autoplay= True)



if __name__ == '__Leg_Lunges_Starting_Message__':
    Leg_Lunges_Starting_Message()











def Hamstring_Curls_Starting_Message():
  
  st.audio('App\pages\AudioCoach\Messages\Starting_Hamstring_Curls_Message.mp3',  autoplay= True)

if __name__ == '__Hamstring_Curls_Starting_Message__':
  Hamstring_Curls_Starting_Message()














def Congratulation_Message():
  
  st.audio('App\pages\AudioCoach\Messages\Congratulation_Message.mp3',  autoplay= True)

if __name__ == '__Congratulation_Message__':
  Congratulation_Message()














def Go_Up_Message():
  
  st.audio('App\pages\AudioCoach\Messages\Go Up Message.mp3',  autoplay= True)

if __name__ == '__Go_Up_Message__':
  Go_Up_Message()




def Bicep_Curls_Starting_Message():
  
  st.audio('App\pages\AudioCoach\Messages\Starting_Bicep_Curls_Message.mp3',  autoplay= True)

if __name__ == '__Bicep_Curls_Starting_Message__':
  Bicep_Curls_Starting_Message()


def Drag_Curls_Starting_Message():
  
  st.audio('App\pages\AudioCoach\Messages\Starting_Drag_Curls_Message.mp3',  autoplay= True)

if __name__ == '__Drag_Curls_Starting_Message__':
  Drag_Curls_Starting_Message()


def Hammer_Curls_Starting_Message():
  
  st.audio('App\pages\AudioCoach\Messages\Starting_Hammer_Curls_Message.mp3',  autoplay= True)

if __name__ == '__Hammer_Curls_Starting_Message__':
  Hammer_Curls_Starting_Message()



def Pushups_Starting_Message():
  
  st.audio('App\pages\AudioCoach\Messages\Starting_Pushups_Message.mp3',  autoplay= True)

if __name__ == '__Pushups_Starting_Message__':
  Pushups_Starting_Message()


def Bench_Press_Starting_Message():

  st.audio('App\pages\AudioCoach\Messages\Starting_Bench_Press_Message.mp3',  autoplay= True)

if __name__ == '__Bench_Press_Starting_Message__':
  Bench_Press_Starting_Message()

def Dumbbbell_Chest_Flys_Starting_Message():

  st.audio('App\pages\AudioCoach\Messages\Starting_Dumbbell_Chest_Flys_Message.mp3',  autoplay= True)

if __name__ == '__Dumbbell_Chest_Flys_Starting_Message__':
  Dumbbbell_Chest_Flys_Starting_Message()


def Lat_Pulldown_Starting_Message():

  st.audio('App\pages\AudioCoach\Messages\Starting_Lat_Pulldown_Message.mp3',  autoplay= True)

if __name__ == '__Lat_Pulldown_Starting_Message__':
  Lat_Pulldown_Starting_Message()


def Arnold_Shoulder_Press_Starting_Message():

  st.audio('App\pages\AudioCoach\Messages\Starting_Arnold_Shoulder_Presses_Message.mp3',  autoplay= True)

if __name__ == '__Arnold_Shoulder_Press_Starting_Message__':
  Arnold_Shoulder_Press_Starting_Message()


def Bent_Over_BackRows_Starting_Message():

  st.audio('App\pages\AudioCoach\Messages\Starting_Bent_Over_Back_Rows_Message.mp3',  autoplay= True)


if __name__ == '__Bent_Over_BackRows_Starting_Message__':
  Bent_Over_BackRows_Starting_Message()


def Spider_Curls_Starting_Message():

  st.audio('App\pages\AudioCoach\Messages\Starting_Spider_Curls_Message.mp3',  autoplay= True)

if __name__ == '__Spider_Curls_Starting_Message__':
  Spider_Curls_Starting_Message()


def Rep_One():
  
  st.audio('App\pages\Rep_SoundEffects\RepOne.mp3',  autoplay= True)

if __name__ == '__Rep_One__':
    Rep_One()


def Rep_Two():
  
  st.audio('App\pages\Rep_SoundEffects\RepTwo.mp3',  autoplay= True)

if __name__ == '__Rep_Two__':
    Rep_Two()


def Rep_Three():
  
  st.audio('App\pages\Rep_SoundEffects\RepThree.mp3',  autoplay= True)

if __name__ == '__Rep_Three__':
    Rep_Three()


def Rep_Four():
  
  st.audio('App\pages\Rep_SoundEffects\RepFour.mp3',  autoplay= True)

if __name__ == '__Rep_Four__':
    Rep_Four()


def Rep_Five():
  
  st.audio('App\pages\Rep_SoundEffects\RepFive.mp3',  autoplay= True)

if __name__ == '__Rep_Five__':
    Rep_Five()


def Rep_Six():
  
  st.audio('App\pages\Rep_SoundEffects\RepSix.mp3',  autoplay= True)

if __name__ == '__Rep_Six__':
    Rep_Six()


def Rep_Seven():
  
  st.audio('App\pages\Rep_SoundEffects\RepSeven.mp3',  autoplay= True)

if __name__ == '__Rep_Seven__':
    Rep_Seven()


def Rep_Eight():
  
  st.audio('App\pages\Rep_SoundEffects\RepEight.mp3',  autoplay= True)

if __name__ == '__Rep_Eight__':
    Rep_Eight()


def Rep_Nine():
  
  st.audio('App\pages\Rep_SoundEffects\RepNine.mp3',  autoplay= True)

if __name__ == '__Rep_Nine__':
    Rep_Nine()

def Rep_Ten():
  
  st.audio('App\pages\Rep_SoundEffects\RepTen.mp3',  autoplay= True)

if __name__ == '__Rep_Ten__':
    Rep_Ten()

def Rep_Eleven():
  
  st.audio('App\pages\Rep_SoundEffects\RepEleven.mp3',  autoplay= True)

if __name__ == '__Rep_Eleven__':
    Rep_Eleven()

  
def Rep_Twelve():
  
  st.audio('App\pages\Rep_SoundEffects\RepTwelve.mp3',  autoplay= True)

if __name__ == '__Rep_Twelve__':
    Rep_Twelve()


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose



def BentOver_Backrows_OverHandGrip():


 cap = cv2.VideoCapture(0)
 # Exercise must done on the sides



 # Curl counter variables
 counter = 0 
 stage = None

 ## Setup mediapipe instance
 with mp_pose.Pose(min_detection_confidence=0.8, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark
            
            # Get coordinates
            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            shoulder_1 = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            elbow_1 = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            wrist_1 = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

           
            


            def calculate_angle(a,b,c):
             a = np.array(a) # First
             b = np.array(b) # Mid
             c = np.array(c) # End
    
             radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
             angle = np.abs(radians*180.0/np.pi)
             round_angle = np.round(angle)
    
             if round_angle > 180.0:
              round_angle = 360-round_angle
        
             return round_angle 
            
            def calculate_angle2(a,b,c):
             a = np.array(a) # First
             b = np.array(b) # Mid
             c = np.array(c) # End
    
             radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
             angle2 = np.abs(radians*180.0/np.pi)
             round_angle2 = np.round(angle2)
    
             if round_angle2 > 180.0:
              round_angle2 = 360-round_angle2
        
             return round_angle2 
          

            # Calculate angle
            round_angle = calculate_angle(shoulder, elbow, wrist)
            round_angle2 = calculate_angle(shoulder_1,elbow_1,wrist_1)
            
            """
            # Visualize angle
            cv2.putText(image, str(round_angle), 
                           tuple(np.multiply(elbow, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4, cv2.LINE_AA
                                )
            
             # Visualize angle
            cv2.putText(image, str(round_angle2), 
                           tuple(np.multiply(elbow_1, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4, cv2.LINE_AA
                                )
           
                                
                                """
            # Curl counter logic
            if round_angle >= 170:
                stage = "up"
                
            if round_angle <= 150 and stage =='up':
                
                stage="down"
                
                counter +=1
                print(counter)


                if counter == 1:
               
                 Rep_One()
             

                if counter == 2:
               
                  Rep_Two()
 

                if counter == 3:
               
                   Rep_Three()
             

                if counter == 4:
               
                  Rep_Four()
              

                if counter == 5:
               
                  Rep_Five()


                if counter == 6:
               
                  Rep_Six()

                
                if counter == 7:
               
                 Rep_Seven()
             

                if counter == 8:
               
                  Rep_Eight()
 

                if counter == 9:
               
                   Rep_Nine()
             

                if counter == 10:
               
                  Rep_Ten()

                if counter == 11:
               
                  Rep_Eleven()

                if counter == 12:
               
                  Rep_Twelve()
                  cap.release()
                  cv2.destroyAllWindows()
                  time.sleep(2)
                  Congratulation_Message()
                   
                
            
        
                       

            if round_angle2 >= 170:
                stage = "up"

            
                
            if round_angle2 <= 150 and stage =='up':
                
                stage="down"
                
                counter +=1
                print(counter)

                if counter == 1:
               
                 Rep_One()
             

                if counter == 2:
               
                  Rep_Two()
 

                if counter == 3:
               
                   Rep_Three()
             

                if counter == 4:
               
                  Rep_Four()
              

                if counter == 5:
               
                  Rep_Five()


                if counter == 6:
               
                  Rep_Six()

                
                if counter == 7:
               
                 Rep_Seven()
             

                if counter == 8:
               
                  Rep_Eight()
 

                if counter == 9:
               
                   Rep_Nine()
             

                if counter == 10:
               
                  Rep_Ten()

                if counter == 11:
               
                  Rep_Eleven()

                if counter == 12:
               
                  Rep_Twelve()


                  cap.release()
                  cv2.destroyAllWindows()
                  time.sleep(2)
                  Congratulation_Message()
            
               
        except:
            pass
        
        # Render curl counter
        # Setup status box
        """
        cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)
        
        # Rep data
        cv2.putText(image, 'REPS', (15,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, str(counter), 
                    (10,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        cv2.putText(image, str('Pushups' ), 
                    (10,120), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 2, cv2.LINE_AA)
        
        # Stage data
        cv2.putText(image, 'STAGE', (65,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, stage, 
                    (60,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )               
        """
        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__BentOver_Backrows_OverHandGrip__':
 BentOver_Backrows_OverHandGrip()


def LatPulldown():


 cap = cv2.VideoCapture(0)
 #  # Exercise must done with legs facing the direction of the camera



 # Curl counter variables
 counter = 0 
 stage = None

 ## Setup mediapipe instance
 with mp_pose.Pose(min_detection_confidence=0.8, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark
            
            # Get coordinates
            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            shoulder_1 = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            elbow_1 = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            wrist_1 = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

           
            


            def calculate_angle(a,b,c):
             a = np.array(a) # First
             b = np.array(b) # Mid
             c = np.array(c) # End
    
             radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
             angle = np.abs(radians*180.0/np.pi)
             round_angle = np.round(angle)
    
             if round_angle > 180.0:
              round_angle = 360-round_angle
        
             return round_angle 
            
            def calculate_angle2(a,b,c):
             a = np.array(a) # First
             b = np.array(b) # Mid
             c = np.array(c) # End
    
             radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
             angle2 = np.abs(radians*180.0/np.pi)
             round_angle2 = np.round(angle2)
    
             if round_angle2 > 180.0:
              round_angle2 = 360-round_angle2
        
             return round_angle2 
          

            # Calculate angle
            round_angle = calculate_angle(shoulder, elbow, wrist)
            round_angle2 = calculate_angle(shoulder_1,elbow_1,wrist_1)
            
        
            # Visualize angle
            cv2.putText(image, str(round_angle), 
                           tuple(np.multiply(elbow, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4, cv2.LINE_AA
                                )
            
             # Visualize angle
            cv2.putText(image, str(round_angle2), 
                           tuple(np.multiply(elbow_1, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4, cv2.LINE_AA
                                )
           
            # Curl counter logic
            if round_angle >= 160:
                stage = "up"
                
            if round_angle <= 80 and stage =='up':

                stage="down"
                
                counter +=1
                print(counter)

                if counter == 1:
               
                 Rep_One()
             

                if counter == 2:
               
                  Rep_Two()
 

                if counter == 3:
               
                   Rep_Three()
             

                if counter == 4:
               
                  Rep_Four()
              

                if counter == 5:
               
                  Rep_Five()


                if counter == 6:
               
                  Rep_Six()

                
                if counter == 7:
               
                 Rep_Seven()
             

                if counter == 8:
               
                  Rep_Eight()
 

                if counter == 9:
               
                   Rep_Nine()
             

                if counter == 10:
               
                  Rep_Ten()
                  cap.release()
                  cv2.destroyAllWindows()
                  time.sleep(2)
                  Congratulation_Message()
                   
                
            
        
                       

            if round_angle2 >= 160:
                stage = "up"

            
                
            if round_angle2 <= 80 and stage =='up':
                stage="down"
                
                counter +=1
                print(counter)

                if counter == 1:
               
                 Rep_One()
             

                if counter == 2:
               
                  Rep_Two()
 

                if counter == 3:
               
                   Rep_Three()
             

                if counter == 4:
               
                  Rep_Four()
              

                if counter == 5:
               
                  Rep_Five()


                if counter == 6:
               
                  Rep_Six()

                
                if counter == 7:
               
                 Rep_Seven()
             

                if counter == 8:
               
                  Rep_Eight()
 

                if counter == 9:
               
                   Rep_Nine()
             

                if counter == 10:
               
                  Rep_Ten()
                  cap.release()
                  cv2.destroyAllWindows()
                  time.sleep(2)
                  Congratulation_Message()
            
               
        except:
            pass
        
        # Render curl counter
        # Setup status box
        cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)
        
        # Rep data
        cv2.putText(image, 'REPS', (15,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, str(counter), 
                    (10,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        cv2.putText(image, str('Pushups' ), 
                    (10,120), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 2, cv2.LINE_AA)
        
        # Stage data
        cv2.putText(image, 'STAGE', (65,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, stage, 
                    (60,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        """
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )               
        """
        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__LatPulldown__':
  LatPulldown()




clicked = True

# Define All Exercises

Select_Pushups = 'Pushups'
Select_Bicep_Curls = 'Bicep Curls'
Select_Drag_Curls = 'Drag Curls'
Select_Squats = 'Squats'
Select_Bench_Press = 'Bench Press'
Select_Arnorld_Shoulder_Press = 'Arnold Shoulder Press'
Select_BOBR = 'Bent Over Backrows'
Select_Lat_Pulldown = 'Lat Pulldown'
Select_Hammer_Curls = 'Hammer Curls'
Select_Spider_Curls = 'Spider Curls'
Select_Dumbbell_Chest_Flys = 'Dumbbell Chest Flys'
Select_Deadlift = 'Deadlift'
Select_Leg_Lunges = 'Leg Lunges'
Select_Hamstring_Culrs = 'Hamstring Curls'




st.title('BodyBuilding')


st.divider()

UpperBody = 'Upper Body Workout'
LowerBody = 'Lower Body Workout'
Unselected = 'Workout Type'

# Define All Exercises






Workout_Selector = st.selectbox(label= 'Select the type of workout you want to do', options= [UpperBody, LowerBody, Unselected], index= 2)


if Workout_Selector == Unselected:

  print()



if Workout_Selector == UpperBody:
 
  clicked = True

  st.header('Upper Body Workout')

  st.subheader('Parameters')

  sy.space(lines=2)
 

  Exercise_Selector = st.selectbox(label= 'Select Exercises' , options= ['Pushups', 'Lat Pulldown', 'Bicep Curls', 'Drag Curls',
                                                            'Hammer Curls', 'Bench Press', Select_Dumbbell_Chest_Flys, Select_BOBR,
                                                            'Arnold Shoulder Press'],)

  sy.space(lines=2)
  Start_Button = st.button('Start')
  


  if Start_Button is clicked and Exercise_Selector == Select_Bicep_Curls :
     
    Bicep_Curls_Starting_Message()

    time.sleep(10)
     
    BicepCurls()


  if Start_Button is clicked and Exercise_Selector == Select_Drag_Curls:
    
    Drag_Curls_Starting_Message()

    time.sleep(10)

    DragCurls()

  
  if Start_Button is clicked and Exercise_Selector == Select_Hammer_Curls:

    Hammer_Curls_Starting_Message()

    time.sleep(10)

    HammerCurls()


  if Start_Button is clicked and Exercise_Selector == Select_Pushups:

    Pushups_Starting_Message()

    time.sleep(10)

    Pushups()

  if Start_Button is clicked and Exercise_Selector == Select_Bench_Press:

    Bench_Press_Starting_Message()

    time.sleep(10)

    BenchPress()

  if Start_Button is clicked and Exercise_Selector == Select_Dumbbell_Chest_Flys:

    Dumbbbell_Chest_Flys_Starting_Message()

    time.sleep(10)

    Dumbbell_Chest_Flys()

  if Start_Button is clicked and Exercise_Selector == Select_Lat_Pulldown:

    Lat_Pulldown_Starting_Message()

    time.sleep(10)

    LatPulldown()


  if Start_Button is clicked and Exercise_Selector == Select_Arnorld_Shoulder_Press:

    Arnold_Shoulder_Press_Starting_Message()

    time.sleep(10)

    ArnoldShoulderPress()

  
  if Start_Button is clicked and Exercise_Selector == Select_BOBR:

    Bent_Over_BackRows_Starting_Message()

    time.sleep(10)

    BentOver_Backrows_OverHandGrip()

  
  if Start_Button is clicked and Exercise_Selector == Select_Spider_Curls:

    Spider_Curls_Starting_Message()

    time.sleep(10)

    SpiderCurls()


 



















        
if Workout_Selector == LowerBody:
 
  clicked = True

  st.header('Lower Body Workout')

  st.subheader('Parameters')
  
  #Exercise_Amount_Selector = st.selectbox(label= 'How many exercises do you want to do?',  options=['1', '2', '3', '4'], index= 1,)


  sy.space(lines=2)
  Exercise_Selector = st.selectbox(label= 'Select Exercises' , options= [Select_Deadlift, Select_Squats, Select_Hamstring_Culrs, Select_Leg_Lunges
                                                            ],)

  sy.space(lines=2)
  Start_Button = st.button('Start')
 

  if Start_Button is clicked and Exercise_Selector == Select_Squats :
     
    Squats_Starting_Message()
     
    time.sleep(10)
     
    Squats()

  if Start_Button is clicked and Exercise_Selector == Select_Hamstring_Culrs :
     
    Hamstring_Curls_Starting_Message()
     
    time.sleep(10)
     
    HamstringCurls()

  if Start_Button is clicked and Exercise_Selector == Select_Leg_Lunges :
     
    Leg_Lunges_Starting_Message()
     
    time.sleep(10)
     
    LegLunges()

  
  if Start_Button is clicked and Exercise_Selector == Select_Deadlift :
     
    Deadlift_Starting_Message()
     
     
    time.sleep(10)
     
    Deadlift()


