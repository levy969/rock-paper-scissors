import random
def intro():
    print("welcome to rock paper scissors game")
    print('enter rock paper scissors or q to quit\n')

def evaluate(s,rand,variables):
    check = [['d', 'l', 'w'],
             ['w', 'd', 'l'],
             ['l', 'w', 'd']]
    
    temp = variables.index(s)
    compchoose = variables[rand]
    return compchoose, check[temp][rand]
            
def main():
    random.seed()
    variables=['rock','paper','scissors']
    scores=[0,0]
    intro()
    try:
        while True:
            rand = random.randint(0,2)
            s = input('enter a choice : ').strip().lower()
            if s== 'q':
                print('exiting...')
                break
            if s not in variables:
                print('please enter properly')
                continue
            botpick,ress = evaluate(s,rand,variables)
            print()
            if ress == 'w':
                print(f'bot picked {botpick}, you won')
                scores[0] += 1
            elif ress == 'l':
                print(f'bot picked {botpick}, you lose')
                scores[1] += 1
            else :
                print(f'bot picked {botpick}, draw!!')

            print(f"player : {scores[0]}\nbot : {scores[1]}")
            print()
    except KeyboardInterrupt:
        print("\nexiting...")


if __name__ == "__main__" :
    main()


