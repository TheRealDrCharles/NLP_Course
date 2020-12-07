import nltk
from replacers import WordReplacer
replacer=WordReplacer({'congrats':'congratulations'})
s=replacer.replace('congrats')
print(s)
s2=replacer.replace('maths')
print(s2)
