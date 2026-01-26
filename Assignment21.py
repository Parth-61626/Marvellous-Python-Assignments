import threading

# 1)

def PrimeF(num):
    print("Prime numbers :")
    for n in num:
        count = 0
        for i in range(1,n+1):
            if n % i == 0:
                count = count + 1
        if count == 2:
            print(n)

def NonPrimeF(num):
    print("Non-Prime numbers :")
    for n in num:
        count = 0
        for i in range(1,n+1):
            if n % i == 0:
                count = count + 1
        if count != 2:
            print(n)

def main():

    numbers = [4,2,5,7,9,12]

    Prime = threading.Thread(target = PrimeF,args = (numbers,))

    NonPrime = threading.Thread(target = NonPrimeF,args = (numbers,))

    Prime.start()
    Prime.join()

    NonPrime.start()
    NonPrime.join()

if __name__ == "__main__":
    main()


# 2)

def max(num):

    maximum_number = num[0]

    for i in num:
        if i > maximum_number:
            maximum_number = i
    print(maximum_number)

def min(num):

    minimum_number = num[0]

    for i in num:
        if i < minimum_number:
            minimum_number = i
    print(minimum_number)

def main():

    numbers = []
    size = int(input("Enter size of the list :"))

    for i in range(size):
        value = int(input("Enter value :"))
        numbers.append(value)

    Thread1 = threading.Thread(target = max,args = (numbers,))
    Thread2 = threading.Thread(target = min,args = (numbers,))

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()


# 3)

iCnt = 0
lobj = threading.Lock()

def update():
    global iCnt

    for _ in range(2000000):
        with lobj:
            iCnt = iCnt + 1

def main():
    global iCnt

    t1 = threading.Thread(target = update)
    t2 = threading.Thread(target = update)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Value of iCnt is",iCnt)

if __name__ == "__main__":
    main()


# 4)

ret = {}

def sum(numbers):
    add = 0
    for n in numbers:
        add = add + n
    ret['sum'] = add

def product(numbers):
    product = 1
    for n in numbers:
        product = product * n
    ret['product'] = product

def main():

    numbers = [10,20,30]

    Thread1 = threading.Thread(target=sum, args=(numbers,))
    Thread2 = threading.Thread(target=product, args=(numbers,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print("Sum of elements:", ret['sum'])
    print("Product of elements:", ret['product'])

if __name__ == "__main__":
    main()