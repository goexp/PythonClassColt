'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''
import re
def statistics(source):
    with open(source) as src_handle:
        src_contents=src_handle.read()    
    return {'lines':len(src_contents.split("\n")),'words':len(re.findall(r"[\w']+",src_contents)), 'characters':len([letter for letter in src_contents if letter != " " and letter != "\n"]) }

if __name__ == '__main__':
	print(statistics("story.txt"))
