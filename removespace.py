word="   my name is satya  "
start=0
end=0
for i in range(len(word)):
    if word[i]!=" ":
      start=i
      break
for i in range(len(word)-1,-1,-1):
   if word[i]!=" ":
      end=i
      break

sent=word[start:end+1]
print(sent)


print(word.strip())