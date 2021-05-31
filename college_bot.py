import random
from datetime import datetime
"""
1. Details about the college like address, contact numbers and location
2. Various courses which are currently offered by this college.
3. Placement information regarding this academic year
4. Regarding various sports encouraged by college as well as their achievements
5. Details about the internships and projects gained by this college
6. Details regarding the hostel facilities and fee structure per each hostel
7. Information about different activities like music club, cultural club etc.
8. Regarding all the latest notifications from the college.
9. Details about the research projects handled currently.
"""
contact_number =  "123467895" 


#List of college bot options

def college_bot_main_options():
    print("------------------------")
    print("1. About our college: ")
    print("2. Placements in our college: ")
    print("3. Sports & NCC: ")
    print("4. Internships and projects: ")
    print("5. Reserch Work: ")
    print("6. Miscelleneous: ")
    print("7. Extracurricuilar Activities: ")
    print("8. Notification: ")
    print("9. what are the eligibility criteria to register for the camps placement?: ")
    print("10 what are stages of the recruitment process?: ")
    print("11. what is Aptitude test?: ")
    print("12. what is personal interview (HR)?: ")
    print("13. For Exit: ")
    print("---------------------")
    try:
        return int(input("enter your choice: "))
    except:
        print("only given choice 1 to 13")
    return 0

# this method gives the information about the college

def about_college():
    address = "Vidyalankar Polytechnic, Vidyalankar Campus, Wadala East, Sangam Nagar, Mumbai, Maharashtra 400037"
    contact_number =  "1234567895" 
    messsage = address + "\n" + " If you have any queries please contact this number "+ contact_number
    return messsage

#This method gives the placements details of our college

def Placement_offered():
    message = "For 2021 passedout students,major companies like TCS,Capgemni,Amazon,Amdocs,SenecaGlobal,Infosys etc.. "
    return message

#This method gives the sports and NCC details of our college

def sports_and_NCC():
    message = "Our students are encouraged to particpate in different tournments for Cricket,volleyball,BasketBall,Throwball,Badminton etc..We have special sports club to maintain all these."
    return message
#This method gives the projects and internships of our college

def internships_and_projects():
    message = "Every year our students are doing interships at different multinational companies"
    return message

#This method gives the Miscellaneous fees and other factors of our college

def Miscellaneous():
    message = "Apart from academic subjects,our college provides various additional courses like Pega,Game Development,Android App Development etc.. for students career development"
    return message

#This method gives the information about Extracurricular activities of our college like music... etc

def Extracurricular_activities():
    message =  "We have Different clubs to support students interests like Music,Dance,Photography,Astronomy,Coding etc.."
    return message

# method is used to greet the user\

def greet_and_introduce():
    #declare some list of responses
    responses = [ "Hi There! I am Bot. I am here to help you. May I know your name please ?", 
    "Hi It is so nice to be in touch with you. Can you tell me your name ? "
    ]
    #pick a responses at random
    print(random.choice(responses))


#this method is used to find the current time 

def get_timeofday_greeting():
    current_time = datetime.today()
    timeofday_greeting = "Good Morning"
    if current_time.hour <= 12 and current_time.hour  < 17:
        timeofday_greeting = "Good Afternoon"
    elif current_time.hour >= 17 and current_time.hour < 22:
        timeofday_greeting = "Good Evening"
    else:
        timeofday_greeting ="Hi, Thats late"
    return timeofday_greeting

# this message used to print the welcome message

def welcome(name):
    messages = ["Nice to meet you", "Glad that you are here"]
    print(get_timeofday_greeting()+ " " + random.choice(messages) +"\n"+ "hiiii "+ name + " welcome to our college")

#this method gives the information about reserch work and conferences of our college

def Reserch_Work():
    return "we have reserch departemt to spouncer the projects and conferences"

#this method gives the information about new notifications of our college

def Notification():
    return "now we don't have any new notifications"

#this method gives the information about new what are the eligibility criteria to register for the camps placement?
 
 def What are the eligibility criteria to register for the camps placement():
    messages = ["Eligibility criteria to participate in the campus placements for the graduating class are as below: "+ 
    "a. 60% throughout. (10th , 12th , UG/PG)/60% in UG/PG"
    "b. No Standing Arrears."
     "c. Students with Standing Arrears (Maximum-02) will be only considered as per the company's discretion."
    "d. Students opting for placements will be given LOR (Letter of Recommendation) for higher studies except 
       "the students gettingplaced in Core / Dream companies."]

#this method gives the information about new What are the stages of the recruitment process?
 
 def What are the stages of the recruitment process():
    messages = ["The following are the typical stages of recruitment – elimination happens at every stage"
   "a. Pre-placement Talk (PPT)
    "b. Aptitude Test / Technical Test (Online/Pen and Paper)
    "c. Group Discussion(GD)
    "d. Personal Interview (PI)
     "e. Technical & HR Interview (TI) The above mentioned stages may vary as per each company recruitment pattern.
     ]

#this method gives the information about new What is Aptitude Test?
 
 def What is Aptitude Test():
    messages = ["a. Consists of Verbal Reasoning, Logical Reasoning and Numerical / Analytical sections.
                "b. Duration of the test varies from Company to Company.
                 "c. Every company has minimum cut-off marks. (Section-wise and Overall)
                "d. Some companies may have negative marking also.
                 "e. Those who clear the Aptitude test will go to the next round of the selection process."]

#this method gives the information about new What is personal interview (HR)?
 
 def What is personal interview (HR)():
    messages = ["HR interviews are conducted to assess Attitude, Communication, Confidence level, Flexibility and
    " Fitment of the candidate into the respective company culture"]


def What is the schedule of Placements Interview ():
    messages = [" Infosys 02/05/2021 , Wipro  06/05/2021 , HP 08/06/2021
    " Other details will be shared shortly" ]
    
def What is the shortlisted students in L&T campus interview (SC)():
    messages = [" Parag IF5I-B, Vinay CO5I-A, Arti IF5I-B
    " Congratulations students!!" ] 
    
#this method for good bye message at the time of exit

def good_bye_message():
    print("Thank You for visiting our site")

#this method is for bot functionality

def bot():
    greet_and_introduce()
    name = input("May I know your good name:")
    welcome(name)
    choice = college_bot_main_options()
    while choice != 0:

        #if you choose choice one then it will about_college() method
        if choice == 1:
            print()
            print("-----------About College--------------")
            print(about_college(),end="\n")


        elif choice == 2:
            print()
            print("----------Plcaments--------------")
            print(Placement_offered(),end="\n")


        elif choice == 3:
            print()
            print("----------Sports And NCC--------------")
            print(sports_and_NCC(),end="\n")

        elif choice == 4:
            print()
            print("----------Internships and Projects--------------")
            print(internships_and_projects(),end="\n")

        elif choice == 5:
            print()
            print("----------Research Work--------------")
            print(Reserch_Work(),end="\n")

        elif choice == 6:
            print()
            print("----------Miscelaneous--------------")
            print(Miscellaneous(),end="\n")

        elif choice == 7:
            print()
            print("----------Extracurricular_activities--------------")
            print(Extracurricular_activities(),end="\n")

        elif choice == 8:
            print()
            print("----------Notification--------------")
            print(Notification(),end="\n")

         elif choice == 9:
            print()
            print("-----What are the eligibility criteria to register for the campus placements------")
            print(What are the eligibility criteria to register for the campus placements(),end="\n")   
        
         elif choice == 10:
            print()
            print("-----What are the stages of the recruitment process------")
            print(What are the stages of the recruitment process(),end="\n")  

         elif choice == 11:
            print()
            print("-----What is Aptitude Test------")
            print(What is Aptitude Test(),end="\n") 

         elif choice == 12:
            print()
            print("-----What is personal interview (HR)------")
            print(What is personal interview (HR)(),end="\n")            
         
         elif choice == 13:
            print()
            print("-----What is the schedule of Placements Interviews(PL)------")
            print(What is the schedule of Placements Interviews(PL),end="\n") 
        
          elif choice == 14:
            print()
            print("-----What is the shortlisted students in L&T campus interview (SC)------")
            print(What is the shortlisted students in L&T campus interview (SC),end="\n") 
        
        choice = college_bot_main_options()
    
    good_bye_message()
        
bot()
college_bot.py
Displaying college_bot.py.