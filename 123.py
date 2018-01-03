import re

def camelCase(tag_str):
    words = re.findall(r'\w+', tag_str)
    nwords = len(words)
    if nwords == 1:
        return words[0] # leave unchanged
    elif nwords > 1: # make it camelCaseTag
        return words[0].lower() + ''.join(map(str.title, words[1:]))
    return '' # no word characters

tags_str = """ 'tHiS iS a tAg, 'whitespace' !&#^ , secondcomment , no!punc$$, 
ifNOSPACESthenPRESERVEcaps' """
print("\n".join(filter(None, map(camelCase, tags_str.split(',')))))()