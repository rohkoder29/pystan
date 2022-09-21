import difflib as dfl
# from difflib import get_close_matches as gcm

words = ['blastula', 'stuff', 'understudy', 'priceless', 'license', 'service']

close_match = dfl.get_close_matches('stu', words)
print(close_match)

close_match = dfl.get_close_matches('ice', words)
print(close_match)
