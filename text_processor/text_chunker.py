import os
import sys

from html.parser import HTMLParser
import json
#Reading in the file

#Reading in the font size 
n = len(sys.argv)
file_name = sys.argv[1]
font_size = sys.argv[2]


#Reading in the json content


with open(file_name, 'r', encoding = 'utf-8') as f:
    html_content = f.read()




class BookHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()

        self.reset()
        self.book_content = {'Chapter 0':  []}
        self.chapter_counter = 0
        self.escape_codes = ['\\n', '\\xa0']



    #When the parser sees a div tag with a class == Chapter - we need to create a new item in the dictionary 
    def handle_starttag(self, tag, attrs):
        tag_attrs = attrs
        if tag == 'div':
            if len(tag_attrs) == 1:
                if tag_attrs[0][0] == 'class' and tag_attrs[0][1] == 'chapter':
                    self.chapter_counter += 1
                    self.book_content[f'Chapter {self.chapter_counter}'] = []
        

        
        
    #Needs to read in the data to the element in book_chapter
    def handle_data(self, data):
        tag_data = data
        if tag_data != '\n':
            tag_data = tag_data.replace("\n", " ")
            tag_data = tag_data.replace("\xa0", "")
            tag_data = tag_data.strip()
            self.book_content[f'Chapter {self.chapter_counter}'].append(tag_data)

 
    def handle_endtag(self, tag):
        pass
    def return_book_content(self):
        return self.book_content



def chunk_the_chapter(chapter_content, max_char):
    #Turning the chapter content into a list of words
    chapter_words = chapter_content
    blocks =[]
    current_block = ""
    block_length = len(current_block)
    for word_ind in range(0, len(chapter_words)):
        if chapter_words[word_ind] != '':
            #Check to see whether adding another word will exceed block length 
            if block_length + len(chapter_words[word_ind]) + 1 <= max_char:
                current_block  = current_block + chapter_words[word_ind] + " "
                block_length = len(current_block)

            else:
                blocks.append(current_block + "-")
                current_block = chapter_words[word_ind]
                block_length = 0



    return blocks


testParser = BookHTMLParser()
testParser.feed(html_content)
book_content = testParser.return_book_content()



#Splitting the text into chunks
# - Every 'Card' will be 185 characters long
# - Number_of_characters = 221 - font size

num_of_char = 221 - int(font_size)



for x in range(1,len(book_content.keys())):
    chap = list(book_content.keys())[x]
    entire_chapter = " ".join(book_content[chap])
    entire_chapter_split = entire_chapter.split(" ")

    
   
    chapter_chunks = chunk_the_chapter(entire_chapter_split, num_of_char)
    print(chapter_chunks)



  


    for y in range(0, len(chapter_chunks)):
        with open(f'{chap}_{y}.txt', 'w') as f:
            f.write(chapter_chunks[y])




    


