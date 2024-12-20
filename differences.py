# Get Name
# Write a method that accepts a name from the user and then returns it. Here’s the javascript:
'''
const getName = () => {
  let name = prompt("what is your name?");
  return name;
};
'''
getName = input('What is your name? ')
print(getName)

# Reverse It
# Write a method that reverses a string. Here’s the javascript:
'''
const reverseIt = () => {
  let string = "a man, a plan, a canal, frenemies!";

  let reverse = "";

  for (let i=0; i < string.length; i++) {
    reverse += string[string.length - (i+1)];
  };

  alert(reverse);
};
'''

def reverseString():
    reverse = ''
    string = "a man, a plan, a canal, frenemies!"
    for i in string:
        reverse = i + reverse

        print(reverse)
    # this is really weird..... so it always adds the front of the string when it loops through
reverseString()

# Swap Em
# Write a method that swaps the values of two variables around. Here’s the javascript:
'''
const swapEm = () => {
  let a = 10;
  let b = 30;
  let temp;

  temp = b;
  b = a;
  a = temp;

  alert("a is now " + a + ", and b is now " + b);
};
'''

def swapEm():
    a = 10
    b = 30
    
    temp = b
    b = a
    a = temp
    print( a, b)
swapEm()

def swapEm2():
    a = 10
    b = 30

    a, b = b, a
    print(a, b)
swapEm2()

# Multiply Array/List
# Write a method that multiplies all numbers in a given array/list and returns the final product. Here’s the javascript:
'''
const multiplyArray = (ary) => {
  if (ary.length == 0) { return 1; };

  let total = 1;
  // let total = ary[0];

  for (let i=0; i < ary.length; i++) {
    total = total * ary[i];
  };

  return total;
};
'''
nums = [2, 5, 6, 44 ,10]
total = 1

def multiply(int):
    for num in nums:
        total = num * int
        print(total)

multiply(2)

# Fizz Buzzer
# Write a method that takes a number argument and returns “fizz” if the number is divisible by three, “buzz” if the number is divisible by five, and “fizzbuzz” if it’s divisible by both. Here’s the javascript:
'''
const fizzbuzzer = (x) => {
  if( x%(3*5) == 0 ) {
    return 'fizzbuzz'
  } else if( x%3 == 0 ) {
    return 'fizz'
  } else if ( x%5 == 0 ) {
    return 'buzz'
  } else {
    return 'archer'
  }
}
'''
# need to use % to check for divisability

def fizzbuzz(x):
    if x % (3*5) == 0:
        print('fizzbuzz')
    elif x % 5 == 0:
        print('buzz')
    elif x% 3 == 0:
        print('fizz')
    else:
        print('archer')
        
fizzbuzz(12)

# Nth Fibonacci
# Write a method that finds the fibonacci number at the nth position and returns it. Here is the javascript:
'''
const nthFibonacciNumber = () => {
  let fibs = [1, 1];
  let num = prompt("which fibonacci number do you want?");

  while (fibs.length < parseInt(num)) {
    let length = fibs.length;
    let nextFib = fibs[length - 2] + fibs[length - 1];
    fibs.push(nextFib);
  }

  alert(fibs[fibs.length - 1] + " is the fibonacci number at position " + num);
};
'''

def nthFibonacciNumber():
    #inital Fibonacci sequence
    fibs = [1, 1]

    #prompt for user input wrapping in a int() to convert the string to a number
    num = int(input("which fibonacci number do you want?"))

    #generate Fibonacci numbers
    #len() is for the array'.length'
    while len(fibs) < num:
        nextFib = fibs[-2] + fibs[-1] #sum of the last two numbers i think ??
        #append() is the python equvilent to JS push()
        fibs.append(nextFib)
    
    print(f"{fibs[-1]} is the FIbonacci number at postion {num}")

nthFibonacciNumber()

# Search Array/List
# Write a method that searches through an array/list for a value and returns true or false depending on whether or not the value is present in the array/list. Here is the javascript:
'''
const searchArray = (array, value) => {
  for(let i = 0; i < array.length-1; i++) {
    if(array[i] == value) {
      return true;
      break;
    }
  }
  return -1;
};
'''

def serachArray(array, value):
    for i in range(len(array)): 
        #we use range to itterate through until we reach the lenght (len() ) for the array. 
        if array[i] == value:
            print(True)
            return #return acts like a break and exits the function
    print(-1)

print(nums)
serachArray(nums, 10)

# Palindrome
# Write a method that checks whether or not a string is a palindrome. Here is the javascript:
'''
const isPalindrome = (str) => {
  for(let i = 0; i < str.length/2; i++){ #guessing this means half way through the length?
    if(str[i] != str[str.length-i-1]){ #huh???? minus index - 1?
      return false;
      break;
    }
  }
  return true;
};
'''

def isPalindrome(str):
    #range should be half way through the array length?
    for i in range(len(str)//2):
        if str[i] != str[len(str) -i - 1]:
            print(False)
            return
    print(True)
    # print(str == str[::-1])

isPalindrome('racercar')

# hasDupes
# Write a method that checks whether or not an array/list has any duplicates. Here is the javascript:
'''
const hasDupes = (arr) => {
  let obj = {};
  for (i = 0; i < arr.length; i++) {
    if(obj[arr[i]]) {
      return true;
    }
    else {
      obj[arr[i]] = true;
    }
  }
  return false;
};
'''

def hasDupes(arr):
    obj = {}
    for i in arr:
        if i in obj:
            print(True)
            return
        else:
            obj[i] = True
    print(False)

hasDupes([1, 3, 4, 5, 6, 5])

#====================


#Hangman

