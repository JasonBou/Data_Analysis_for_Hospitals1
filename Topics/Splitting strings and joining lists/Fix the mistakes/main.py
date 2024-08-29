text = input()
words = text.split()
web_list = [] 
for word in words:
    if word.startswith("www.") or word.startswith("WWW."):
        web_list.append(word)
    if word.startswith("https:") or word.startswith("http:"):
        web_list.append(word)

for urls in web_list:
    print(urls)
        
        
    # finish the code here
