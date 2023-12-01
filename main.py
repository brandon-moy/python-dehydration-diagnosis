welcome_prompt = "Hello! What would you like to do today?\n - List all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press q\n"
name_prompt = "What is the patient's name?\n"
appearance_prompt = "How is the patient's general appearance?\n - 1: Normal appearance \n -2: Irritable or lethargic\n"

def list_patients ():
    print("List of patients and diagnoses")
    
def start_diagnosis ():
    name = input(name_prompt)
    appearance = input(appearance_prompt)

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