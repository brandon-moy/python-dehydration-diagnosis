welcome_prompt = "Hello! What would you like to do today?\n - List all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press q\n"

def main():
  selection = input(welcome_prompt)
  print(selection)
  
main()