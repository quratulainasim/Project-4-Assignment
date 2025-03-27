
prompt:str="What do you want ? "
joke:str="Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
sorry:str="I will only tell joke."
def main():
  user_input= input(prompt).strip().lower()

  if "joke" in user_input:
      print(joke)
  else:
      print(sorry)

if __name__ == '__main__':
    main()
 