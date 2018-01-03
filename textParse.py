import re

sample = "Adult beavers have long flat tails that are about a foot long. Beavers slap their tails on the water surface as an alarm to alert the colony when they sense danger. Female beavers are larger than male beavers of the same age. Prior to European immigration there were over 60 million beavers in North America. Due primarily to over trapping beavers were an endangered species in the early part of the 20th Century. Beavers are very active on Pinterest and often are considered social media mavens. Tiny beavers (Microtheriomys brevirhinus) lived in Oregon 28 Million Years Ago. They were 1/10 the size of modern beavers."
matches = re.findall('\w+', sample)
words = re.split('\w', matches)
#print(matches)
print(words)
for match in matches:
    match = sorted(match)
    print(match.sort())

print(sorted(matches))

