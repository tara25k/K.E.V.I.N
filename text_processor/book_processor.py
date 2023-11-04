from html.parser import HTMLParser
import json
#Reading in the file
file_name  = "Alice in Wonderland.html"

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
    
        self.book_content[f'Chapter {self.chapter_counter}'].append(tag_data)

 
    def handle_endtag(self, tag):
        pass
    def return_book_content(self):
        return self.book_content


testParser = BookHTMLParser()
testParser.feed(html_content)
book_content = testParser.return_book_content()


#Writing the dictionary to a text file
with open('book_content.txt', 'w') as file:
    file.write(json.dumps(book_content))