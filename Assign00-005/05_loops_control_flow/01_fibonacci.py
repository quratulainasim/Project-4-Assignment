MAX_TERM_VALUE : int = 10000

def main():
    current_value = 0
    next_value = 1
    while current_value <= MAX_TERM_VALUE:
        print(current_value)
        new_value = current_value + next_value
        current_value = next_value
        next_value =  new_value
if __name__ == '__main__':
   main()
