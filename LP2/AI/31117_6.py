'''
31117 - Udayan Chavan - K1
Assignment 6 - Implement any one of the following expert systems:
    1. Information management
    2. Hospitals and medical facilities
    3. Help desks management
    4. Employee performance evaluation
    5. Stock market trading
    6. Airline scheduling and cargo schedules
'''
# --------------------------------------------------------------------------

commonSymptoms=["Does the patient experience fever? ", 
                "Does the patient experience cold? ", 
                "Does the patient experience tiredness? ",
                "Does the patient experience loss of taste or smell? "]

mildSymptoms=["Does the patient experience a sore throat? ",
              "Does the patient experience a headache? ",
              "Does the patient experience rashes on the body? ",
              "Does the patient experience diarrhoea? "]

# --------------------------------------------------------------------------

print("\n===== Covid detection expert system =====")
print("\nPress 'Y' if you experience the following symptoms and 'N' if you don't.")

score=0

# Check for common symptoms
for i in range(len(commonSymptoms)):
    x = input(commonSymptoms[i])
    if(x=="Y"):
        score+=2
    elif(x=="N"):
        continue
    else:
        print("Invalid Input")  
        
# Check for mild symptoms
for i in range(len(mildSymptoms)):
    x = input(mildSymptoms[i])
    if(x=="Y"):
        score+=1
    elif(x=="N"):
        continue
    else:
        print("Invalid Input")

if(score>7):
    print("\nThe patient has covid.")
else:
    print("\nThe patient does not have covid.")
    
# --------------------------------------------------------------------------

'''
========== OUTPUT ==========
---------- TEST 1 ----------

===== Covid detection expert system =====

Press 'Y' if you experience the following symptoms and 'N' if you don't.
Does the patient experience fever? Y
Does the patient experience cold? N
Does the patient experience tiredness? N
Does the patient experience loss of taste or smell? Y
Does the patient experience a sore throat? Y
Does the patient experience a headache? Y
Does the patient experience rashes on the body? Y
Does the patient experience diarrhoea? Y

The patient has covid.

---------- TEST 2 ----------

===== Covid detection expert system =====

Press 'Y' if you experience the following symptoms and 'N' if you don't.
Does the patient experience fever? N
Does the patient experience cold? N
Does the patient experience tiredness? N
Does the patient experience loss of taste or smell? N
Does the patient experience a sore throat? Y
Does the patient experience a headache? Y
Does the patient experience rashes on the body? N
Does the patient experience diarrhoea? Y

The patient does not have covid.
'''