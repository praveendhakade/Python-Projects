import re, pyperclip

# Regex for urls

urlsRegex = re.compile(r'''(
    ([http://]|[https://])+                           #1 URLs start
    
    ([a-zA-Z0-9.-_])+                                 #2 site name
    (\/)?     
    )''', re.VERBOSE)

# matches on the clipboard
text =str(pyperclip.paste())
matches = []

# conditions
for group in urlsRegex.findall(text):
    matches.append(group[0])

# display on clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to Clipboard:')
    print('\n'.join(matches))
else:
    print('No URLs are found')

