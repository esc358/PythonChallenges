#Emilio Sebastian Conde Ludena
#June 26, 2025
#From: https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

#function string s and integer k
def merge_the_tools(s, k):
    # loop for length of s iterating by k
    for i in range(0, len(s), k):
        #assign to substring the string at location i to i + k
        substring = s[i:i + k]
        #create variable unique and assign empty string
        unique = ""
        #loop through substring
        for char in substring:
            #validate that char is not in variable unique
            if char not in unique:
                #add char to unique
                unique += char
        print(unique) #print and run next set of substring

# Test
s = 'AABCAAADA'
k = 3
merge_the_tools(s, k)

