#program to count number of vowels using input given
def findvowels(str):
    count = 0
    vowels = set('aeiouAEIOU')
    
    for alphabets in str:
        if alphabets in vowels:
            count = count+1
            
    print("Number of vowels",count)
    
str = 'welcome to python world' 

findvowels(str)
     
            