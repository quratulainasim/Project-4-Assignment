def add_number(number)->int:
    num=0
    for i in number:
        num+=i
    return num

def main():
  number:int = [10,20,30,40,50]
  print(add_number(number))
  
if __name__ == "__main__":
    main()
