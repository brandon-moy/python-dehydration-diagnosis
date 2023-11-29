welcome_prompt = "Hello! What would you like to do today?\n - List all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press q\n"

def list_patients ():
    print("List of patients and diagnoses")
    
def start_diagnosis ():
    print("Starting a new diagnosis")    


def main ():
    selection = input(welcome_prompt)
    if selection == "1":
        list_patients()
    elif selection == "2":
        start_diagnosis()
    elif selection == "q":
        return
  
main()