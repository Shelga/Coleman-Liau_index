text = input("your text: ")
    
lettercount = 0
worldcount = 1
sentencecount = 0
length = len(text)
l = 0
s = 0
index = 0
indexT = 0
    
for i in range(length):
    if text[i] >= 'a' and text[i] <= 'z' or text[i] >= 'A' and text[i] <= 'Z': 
        lettercount = lettercount + 1
    elif text[i] == ' ':
        worldcount = worldcount + 1
    elif text[i] == '.' or text[i] == '!' or text[i] == '?':
        sentencecount = sentencecount + 1
    
l = lettercount / worldcount * 100
s = sentencecount / worldcount * 100

index  = (0.0588 * l) - (0.296 * s) - 15.8
indexT = round(index)
    
if indexT < 1:
    print("Before Grade 1")
elif indexT <= 15:
    print("Grade", indexT)
elif indexT >= 16:
    print("Grade 16+")