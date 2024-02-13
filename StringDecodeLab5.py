#!/usr/bin/env python
# coding: utf-8

# In[1]:


def DecodeWord(encoded_word):
    decoded_word = ""
    for char in encoded_word:
        if char == 'T':
            decoded_word += 'L'
        elif char == 'L':
            decoded_word += 'T'
        elif char == 'A':
            decoded_word += 'E'
        elif char == 'E':
            decoded_word += 'B'
        elif char == 'B':
            decoded_word += 'A'
        elif char == 'B':
            decoded_word += 'B'
        elif char == '8':
            decoded_word += 'A' 
        elif char == 'B':
            decoded_word += 'E'
        elif char == '0':
            decoded_word += 'J' 
        else:
            decoded_word += char 
    return decoded_word

def main():
    encoded_words = [
        "WBLARF8TTS",
        "L8KAOUL",
        "E8N8N8",
        "8TRA8DY T8LA",
        "8TT LHA TILLTA LIMAS",
        "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS",
        "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"
    ]
    
    for encoded_word in encoded_words:
        print(DecodeWord(encoded_word))

if __name__ == "__main__":
    main()


# In[ ]:




