#! python3
# mpclip.py - A multi - clipboard programmd.

TEXT = {'agree':"""Yes, I agree, thatt sounds fine to me""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would You consider making this a monthly donation?"""}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()
keyphrase = sys.argv[1] # first command line arg in the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for' + keyphrase + 'copied to clipboard.')
else:
    print('There is no text for' + keyphrase)