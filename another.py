from PIL import Image

words_list = Image.open("word_matrix.png")

mask = Image.open("mask.png")

#check size 
print(mask.size)

print(words_list.size)

mask.putalpha(400)

words_list.paste(mask,(0,0),mask)

