lyrics=["when I find myself in times of trouble",
        "mother Mary comes to me",
        "speaking words of wisdom , let it be",
        "and in my hour of darkness",
        "she is standing right in front of me",
        "speaking words of wisdom , let it be",
        "let it be , let it be",
        "let it be , let it be",
        "whisper words of wisdom , let it be",
        "and when the broken hearted people",
        "living in the world agree",
        "there will be an answer , let it be",
        "for though they may be parted",
        "there is still a chance that they will see",
        "there will be an answer , let it be",
        "let it be , let it be",
        "let it be , let it be",
        "yeah there will be an answer , let it be",
        "let it be , let it be",
        "let it be , let it be",
        "whisper words of wisdom , let it be",
        "let it be , let it be",
        "ah let it be , yeah let it be",
        "whisper words of wisdom , let it be",
        "and when the night is cloudy",
        "there is still a light that shines on me",
        "shine on until tomorrow , let it be",
        "i wake up to the sound of music,",
        "mother Mary comes to me",
        "speaking words of wisdom , let it be",
        "yeah let it be , let it be",
        "let it be , yeah let it be",
        "oh there will be an answer , let it be",
        "let it be , let it be",
        "let it be , yeah let it be",
        "oh there will be an answer , let it be",
        "let it be , let it be",
        "ah let it be , yeah let it be",
        "whisper words of wisdom , let it be"]
print len(lyrics)

d=dict()
for i in range(0,len(lyrics)):
    k=lyrics[i]
    for c in k.split():
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
print d
for c in d:
    if d[c]>10:
        print c
        print d[c]
input()