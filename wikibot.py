import wikipedia

def scrape(name="Microsoft",length=2):
    result=wikipedia.summary(name, sentences=length)
    #print(result)
    return result

print(scrape("Microsoft", 2))
print(scrape("Python (programming language)", 2))