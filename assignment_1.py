f_input = int(input('enter a number'))
op = input('enter the operator')
s_input = int(input('enter another nmber'))

match op:
    case "+":
        print(f_input + s_input)
    case "-":
        print(f_input - s_input)    
    case "/":
        print(f_input / s_input)    
    case "*":
        print(f_input * s_input)    

