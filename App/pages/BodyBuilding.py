import streamlit as st
import streamlit_space as sy
import sys
sys.path.append('Japreo-Fit/App/AudioCoach/Messages/Message_Player')
sys.path.append('Japreo-Fit/App/Exercises/Biceps')
sys.path.append('Japreo-Fit/App/Exercises/Chest')
sys.path.append('Japreo-Fit/App/Exercises/Back')
sys.path.append('Japreo-Fit/App/Exercises/Legs')
sys.path.append('Japreo-Fit/App/Exercises/Shoulders')
from Message_Player import Squats_Starting_Message, Deadlift_Starting_Message, Hamstring_Curls_Starting_Message, Leg_Lunges_Starting_Message
from Messgae_Player import Bicep_Curls_Starting_Message, Drag_Curls_Starting_Message, Hammer_Curls_Starting_Message, Spider_Curls_Starting_Message
from Message_Player import Pushups_Starting_Message, Bench_Press_Starting_Message, Dumbbbell_Chest_Flys_Starting_Message
from Message_Player import Bent_Over_BackRows_Starting_Message, Lat_Pulldown_Starting_Message
from Message_Player import Arnold_Shoulder_Press_Starting_Message


from Bicep_Curls import BicepCurls
from Hammer_Curls import HammerCurls
from Spider_Curls import SpiderCurls
from Drag_Curls import DragCurls



from Pushups import Pushups
from Bench_Press import BenchPress
from Dumbbell_Chest_Flys import Dumbbell_Chest_Flys



from LatPulldown import LatPulldown
from BentOver_BackRows import BentOver_Backrows_OverHandGrip



from Squats import Squats
from Hamstring_Curls import HamstringCurls
from Deadlift import Deadlift
from LegLunges import LegLunges


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


