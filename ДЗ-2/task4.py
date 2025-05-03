text = input()
text_new = text.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
print(text_new)
