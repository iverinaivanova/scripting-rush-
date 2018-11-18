'''
This script counts the number of tokens and
calculates the mean number of mentions per coref set,
as well as the mean number of coref sets per tokens,
and the mean number of mentions per tokens.

'''

#Importing the ET module to parse XML data
import xml.etree.ElementTree
my_tree1 = xml.etree.ElementTree.parse(' ').getroot()

'''Creating two empty lists.
To the first one I'll append only alpha tokens and to the second one punctuation tokens.'''
beAlpha = []
nonAlpha = []

'''Iterate through the tokens and if the POS value of any of the tokens is a punctuation mark or an empty space,
append it to the nonAlpha list. Otherwise, append it to the beAlpha list.'''

for token in my_tree1.iter("token"):
    pos_val = token.find("POS").text
    if pos_val == ".":
        nonAlpha.append(pos_val)
    elif pos_val == ",":
        nonAlpha.append(pos_val)
    elif pos_val == ":":
        nonAlpha.append(pos_val)
    elif pos_val == ";":
        nonAlpha.append(pos_val)
    elif pos_val == "*":
        nonAlpha.append(pos_val)
    elif pos_val == "!":
        nonAlpha.append(pos_val)
    elif pos_val == "?":
        nonAlpha.append(pos_val)
    elif pos_val == "<":
        nonAlpha.append(pos_val)
    elif pos_val == "<=":
        nonAlpha.append(pos_val)
    elif pos_val == ">":
        nonAlpha.append(pos_val)
    elif pos_val == ">=":
        nonAlpha.append(pos_val)
    elif pos_val == "(":
        nonAlpha.append(pos_val)
    elif pos_val == ")":
        nonAlpha.append(pos_val)
    elif pos_val == "{":
        nonAlpha.append(pos_val)
    elif pos_val == "}":
        nonAlpha.append(pos_val)
    elif pos_val == "+":
        nonAlpha.append(pos_val)
    elif pos_val == "+=":
        nonAlpha.append(pos_val)
    elif pos_val == "%":
        nonAlpha.append(pos_val)
    elif pos_val == "&":
        nonAlpha.append(pos_val)
    elif pos_val == "''":
        nonAlpha.append(pos_val)
     elif pos_val == "-":
        nonAlpha.append(pos_val)
    elif pos_val == "``":
        nonAlpha.append(pos_val)
    elif pos_val == "-LRB-":
        nonAlpha.append(pos_val)
    elif pos_val == "-RRB-":
        nonAlpha.append(pos_val)
    else:
        beAlpha.append(pos_val)

print("The number of tokens is: ", len(beAlpha))

'''Creating two empty lists.
To the first one I'll append all coref tags and to the second all mention tags.'''
myCorefs =[]
myMent =[]

'''Find all coreference tags and append them to the myCorefs list.'''

for child in my_tree1.iter("coreference"):
    if child.tag == "coreference":
        myCorefs.append(child)

'''Find all mention tags and append them to the myMent list.'''

for child in my_tree1.iter("mention"):
    if child.tag == "mention":
        myMent.append(child.tag)

print("The mean number of mentions per coref sets is: ", float(len(myMent)) / (len(myCorefs) - int(1)))
print("The mean number of coref sets per tokens is: ", float(len(myCorefs) - int(1)) / (len(beAlpha)))
print("The mean number of mentions per tokens is: ", float(len(myMent)) / (len(beAlpha)))
