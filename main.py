welcome_prompt = "Hello! What would you like to do today?\n - List all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press q\n"
name_prompt = "What is the patient's name?\n"
appearance_prompt = "How is the patient's general appearance?\n - 1: Normal appearance \n -2: Irritable or lethargic\n"

eye_prompt = "How are the patient's eyes?\n - 1: Eyes normal or slightly sunken\n - 2: Eyes very sunken\n"
severe_dehydration = "Severe dehydration"
some_dehydration = "Some dehydration"
no_dehydration = "No dehydration"

def list_patients ():
    print("List of patients and diagnoses")

def assess_eyes():
    eyes = input(eye_prompt)
    if eyes == "1":
        return no_dehydration
    elif eyes == "2":
        return severe_dehydration
    
def assess_skin():
    print("Assessing skin appearance")    
    
def assess_appearance():
    appearance = input(appearance_prompt)
    if appearance == "1":
        diagnosis = assess_eyes()
        print(diagnosis)
    elif appearance == "2":
        assess_skin()
    
def start_diagnosis ():
    name = input(name_prompt)
    assess_appearance()

def main ():
    while(True):
        selection = input(welcome_prompt)
        if selection == "1":
            list_patients()
        elif selection == "2":
            start_diagnosis()
        elif selection == "q":
            return
    
main()