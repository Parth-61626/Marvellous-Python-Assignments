# 1)

import threading

def EvenF():
    for i in range(2,21,2):
        print(i)

def OddF():
    for i in range(1,20,2):
        print(i)

def main():
    
    Even = threading.Thread(target = EvenF)
    Odd = threading.Thread(target = OddF)

    Even.start()
    Even.join()

    Odd.start()
    Odd.join()

if __name__ == "__main__":
    main()


# 2)

def EvenFactorF(no):
    
    sum = 0

    for i in range(1,no):
        if no % i == 0:
            if i % 2 == 0:
                sum = sum + i 
    print("Sum of even factors is :",sum)

def OddFactorF(no):
    sum = 0

    for i in range(1,no):
        if no % i == 0:
            if i % 2 != 0:
                sum = sum + i
    print("Sum of odd factors is :",sum)

def main():
    
    EvenFactor = threading.Thread(target = EvenFactorF,args = (30,))
    OddFactor = threading.Thread(target = OddFactorF,args = (30,))

    EvenFactor.start()
    EvenFactor.join()

    OddFactor.start()
    OddFactor.join()

    print("exit from main")

if __name__ == "__main__":
    main()


# 3)

def EvenListF(no):
    
    sum = 0

    for i in no:
        if i % 2 == 0:
            sum = sum + i
    print("sum of even elements :",sum)

def OddListF(no):
    
    sum = 0

    for i in no:
        if i % 2 != 0:
            sum = sum + i
    print("sum of odd elements :",sum)

def main():

    Numbers = [10,20,11,21]
    
    EvenList = threading.Thread(target = EvenListF,args = (Numbers,))
    OddList = threading.Thread(target = OddListF,args = (Numbers,))

    EvenList.start()
    EvenList.join()

    OddList.start()
    OddList.join()

    print("exit from main")

if __name__ == "__main__":
    main()


# 4)

def smallF(text):
    count = sum(1 for ch in text if ch.islower())
    print("number of lowercase characters :",count)

    print("Thread name :",threading.current_thread().name)
    print("Thread id :",threading.get_ident())

def capitalF(text):
    count = sum(1 for ch in text if ch.isupper())
    print("number of uppercase characters :",count)

    print("Thread name :",threading.current_thread().name)
    print("Thread id :",threading.get_ident())

def digitsF(text):
    count = sum(1 for ch in text if ch.isdigit())
    print("number of numeric digits :",count)

    print("Thread name :",threading.current_thread().name)
    print("Thread id :",threading.get_ident())

def main():

    Small = threading.Thread(target = smallF,args = ("Parth616",),name = "small")

    Capital = threading.Thread(target = capitalF,args = ("Parth616",),name = "Capital")

    Digits = threading.Thread(target = digitsF,args = ("Parth616",),name = "Digits")

    Small.start()
    Small.join()

    Capital.start()
    Capital.join()

    Digits.start()
    Digits.join()

if __name__ == "__main__":
    main()


# 5)

def Thread1F():
    for i in range(1,51):
        print(i)

def Thread2F():
    for i in range(50,0,-1):
        print(i)

def main():

    Thread1 = threading.Thread(target = Thread1F)
    Thread2 = threading.Thread(target = Thread2F)

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()