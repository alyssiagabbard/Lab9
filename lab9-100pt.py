############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

start = True
while(start == True):
    print "What is your temperature?"
    tempAnswer = int(raw_input())
    print "Have you been sick in the last 24 hours?"
    sickAnswer = raw_input()
    print "Have you travelled to West Africa recently?"
    travAnswer = raw_input()
    if tempAnswer >=105 :
        print "You need be amitted into the hospital."
    elif tempAnswer>=102 and sickAnswer == "Yes":
        print "You need be amitted into the hospital."
    elif tempAnswer >= 100 or sickAnswer == "Yes" and travAnswer == "Yes":
        print "You need be amitted into the hospital."
    else:
        print "You are fine, thank you."
    print "-----------------------------------"
    print "Are there any more paitents waiting?"
    finalAnswer = raw_input()
    if finalAnswer == "No":
        start = False
        



# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.
