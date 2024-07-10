#Regular Expression is also known as RegEx, is a bunch of characters or patters
#create search for a string within given string or validate given string
#if it follows given pattern (email/password validation)

#Regular Expression Syntax defines some special characters called sequence that we can use to match given string

'''
\d - matches any digit 0-9(single character)
\D - matches any non digit character
\s - matches any whitespaces
\S - matches any non-whitespaces
\w - matches an alpha-numeric value(a-z)
\W - matches non alpha-numeric values
\b - matches space around words
\A - matches only begining or start of string
\Z - matches end of the string
'''

#search() - searches regular expression
import re
#re is regular expression

str="Take up one idea.One idea at a time"
result=re.search(r'o\w\w',str)
print(result.group())

#findall()
str='Take up one idea.One idea at a time '
result=re.findall(r'i\w\w',str)
print(result)
#will find all words which contain i from i upto next 2 characters since \w is 2 time so including i next 2 characters

#Match() - will match only 1st character of entire string
str='How are you'
result=re.match(r'H\w\w\s\w\w\w',str)
print(result.group())

#split()
str='Take 1 up one 23 idea.One idea 45 at a time'
result=re.split(r'\d',str)
print(result)

#substitute()
str="Take up one idea.One idea at a time"
result=re.sub(r'One','Two',str)
print(result)


#Quantifiers() - they are used to match multiple characters
'''
+ - one or more repetitions of preceeding RE
\d+ - one or more digits for preceeding RE
* - 0 or more repetitions of preceeding RE
? - 0 or 1 repetitions of preceeding RE
{m} - exactly m occurences of preceeding RE
{m,n}
'''

str="Take up one idea on 05-09-2024"
result=re.findall(r'\d{2}--\d{2}--\d{4}',str)
print(result)

#special characters
# \,.,^,$
'''
\ - escape character
. - matches any character except newline
^ - matches at the beginning of string
$ - matches at the end of the string
'''

str='Take up one idea.One idea at a time'
result=re.search(r'^T\w\w\w',str)
print(result.group())

s="How are you"
result=re.search(r'u$',s)
print(result.group())

s='How are you ?'
result=re.search(r'\?$',s)
print(result.group())

s='Thank You!'
result=re.search(r'!$',s)
print(result.group())

#Write a python program that matches an a followed zero or more b's in given string

def match_text(str):
    pattern='ab*'
    if re.search(pattern,str):
        return 'Found'
    else:
        return "Not Found"

print(match_text('abbc'))
print(match_text('adffbbbbs'))