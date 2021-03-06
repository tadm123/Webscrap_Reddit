# "Automate the Boring Stuff" Book
# CH7: phoneAndEmail.py 
# Finds phone numbers and email addresses on the clipboard.

import re, pyperclip

phoneRegex = re.compile(r'''(        # notice this first parenthesis which makes the whole string be a group (group[0]) in the tuple
    (\d{3}|\(\d{3}\))?               # area code  -> either 561 or  (561)
    (\s|-|\.)?                       # separator  (if there is)
    (\d{3})                          # first 3 digits
    (\s|-|\.)                        # separator
    (\d{4})                          # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?   # extension
    )''', re.VERBOSE)

emailRegex= re.compile(r'''(
    [a-zA-Z0-9._%+-]+                # username
    @                                # @symbol
    [a-zA-Z0-0._%+-]+                # domain name
    (\.[a-zA-Z]{2,4})                # dot something
    )''',re.VERBOSE)

# find matches in clipboard text.
text = str(pyperclip.paste())               #paste all clipboard string in to 'text' string
                                            #This string will contain all complete string
matches = []
for groups in phoneRegex.findall(text):             
    phoneNum= '-'.join([groups[1],groups[3],groups[5]])   #the string phoneNum= '561-699-5175'
    if groups[8] != ' ':                #if it has an extension
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)            #matches = ['561-699-5175 x',
                                        #           '555-699-9070 x',

for groups in emailRegex.findall(text):
    matches.append(groups[0])           #append the e-mails string as it is

#Copy results to the clipboard. (our new string)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))   #make it a string
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers of email addresses found.')


'''Output:

800-420-7240 x
415-863-9900 x
415-863-9950 x
info@nostarch.com
media@nostarch.com
academic@nostarch.com
info@nostarch.com

'''


