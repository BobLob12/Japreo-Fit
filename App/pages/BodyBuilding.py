import streamlit as st
import streamlit_space as sy
import cv2
import mediapipe as mp
from AudioCoach.Messages.Message_Player import Squats_Starting_Message, Deadlift_Starting_Message, Hamstring_Curls_Starting_Message, Leg_Lunges_Starting_Message
from AudioCoach.Messages.Message_Player import Bicep_Curls_Starting_Message, Drag_Curls_Starting_Message, Hammer_Curls_Starting_Message, Spider_Curls_Starting_Message
from AudioCoach.Messages.Message_Player import Pushups_Starting_Message, Bench_Press_Starting_Message, Dumbbbell_Chest_Flys_Starting_Message
from AudioCoach.Messages.Message_Player import Bent_Over_BackRows_Starting_Message, Lat_Pulldown_Starting_Message
from AudioCoach.Messages.Message_Player import Arnold_Shoulder_Press_Starting_Message


from Exercises.Biceps.Bicep_Curls import BicepCurls
from Exercises.Biceps.Hammer_Curls import HammerCurls
from Exercises.Biceps.Spider_Curls import SpiderCurls
from Exercises.Biceps.Drag_Curls import DragCurls

from Exercises.Chest.Pushups import Pushups
from Exercises.Chest.Bench_Press import BenchPress
from Exercises.Chest.Dumbbell_Chest_Flys import Dumbbell_Chest_Flys

from Exercises.Back.LatPulldown import LatPulldown
from Exercises.Back.BentOver_BackRows import BentOver_Backrows_OverHandGrip

from Exercises.Legs.Squats import Squats
from Exercises.Legs.Hamstring_Curls import HamstringCurls
from Exercises.Legs.Deadlift import Deadlift
from Exercises.Legs.LegLunges import LegLunges

from Exercises.Shoulders.Arnold_ShoulderPress import ArnoldShoulderPress


import time




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
     
    st.audio('App/AudioCoach/Messages/Starting_Squats_Message.mp3',  autoplay= True)
     
    time.sleep(10)
     
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose



    used = True

    def Squats():

 
    
 

     cap = cv2.VideoCapture(0)
 



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
            Left_Hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            Left_Knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            Left_Ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

            Right_Hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            Right_Knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
            Right_Ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

           
            


            def calculate_angle(a,b,c):
             a = np.array(a) # First
             b = np.array(b) # Mid
             c = np.array(c) # End
    
             radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
             angle = np.abs(radians*180.0/np.pi)
             round_angle = round(angle)
    
             if round_angle > 180.0:
              round_angle = 360-round_angle
        
             return round_angle
            
            def calculate_angle2(a,b,c):
             a = np.array(a) # First
             b = np.array(b) # Mid
             c = np.array(c) # End
    
             radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
             angle2 = np.abs(radians*180.0/np.pi)
             round_angle2 = round(angle2)
    
             if round_angle2 > 180.0:
              round_angle2 = 360-round_angle2
        
             return round_angle2
          

            # Calculate angle
            round_angle = calculate_angle(Left_Hip, Left_Knee, Left_Ankle)
            round_angle2 = calculate_angle(Right_Hip, Right_Knee, Right_Ankle)
            
            """
            # Visualize angle
            cv2.putText(image, str(round_angle), 
                           tuple(np.multiply(Left_Knee, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 4, cv2.LINE_AA
                                )
            
             # Visualize angle
            cv2.putText(image, str(round_angle2), 
                           tuple(np.multiply(Right_Knee, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 4, cv2.LINE_AA
                                )
            """
            # Curl counter logic
            if round_angle >= 160:
                stage = "up"
            if round_angle <= 70 and stage =='up':
                
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
                
                  
              

              
               
             
            """


            if Rep_Amount_Selector == counter:
               
               st.write("You've reached your goal!")
               Congratulation_Message()
               cap.release()
               cv2.destroyAllWindows()
               
            """ 
      

            if round_angle2 >= 160:
                stage = "up"
            if round_angle2 <= 70 and stage =='up':
                
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


