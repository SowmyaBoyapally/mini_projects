import streamlit as sl
sl.title("FLAMES GAME")
str1=list(sl.text_input("Enter first name:").lower())
str2=list(sl.text_input("Enter second name:").lower())
for i in str1.copy():
    if i in str2:
        str2.remove(i)
        str1.remove(i)
n=len(str1+str2)
s="flames"
while(len(s)>1):
    i=n%len(s)-1
    if(i==-1):
        s=s[:len(s)-1]
    else:
        s=s[i+1:]+s[:i]
d={'f':'friendship','l':'love','a':'affection','m':'marriage','e':'enimes','s':'siblings'}
if(sl.button("SUBMIT")):
    sl.success(d[s])
    

