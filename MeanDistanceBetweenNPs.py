'''
The following script calculates the mean distance between NP occurrences in
texts beyond sentence boundaries.
'''


#Importing the ET module to parse XML data
import xml.etree.ElementTree

prev = 0

#Storing the parsed XML data into the variable my_tree1
my_tree1 = xml.etree.ElementTree.parse('').getroot()

'''Creating two empty lists.
To the first one I'll append all NP occurrences found in the XML file.
To the second one -- the difference (i.e. the result from subtracting the index
under which the current NP is stored minus the index under which the previous NP
is stored.
'''
myNPs = []
myDiff = []

'''
Iterate through the tokens. Get the index of the token whose value equals NN, NNS,
NNP, NNPS, and append them to the myNPs list. If the index of the current NP
is smaller than the index of the previous NP occurrence, append the index of the
current NP to the myDiff list. Otherwise, append the difference.

'''
for token in my_tree1.iter("token"):
    pos_val = token.find("POS").text
    current = int(token.get("id"))
    if pos_val == "NN":
        print(pos_val, current)
        myNPs.append(pos_val)
        if(current < prev):
            print("\t" + str(current))
            myDiff.append(current)
        else:
            difference = current - prev
            print(difference)
            myDiff.append(difference)
        prev = current
    elif pos_val == "NNS":
        print(pos_val,current)
        myNPs.append(pos_val)
        if(current < prev):
            print("\t" + str(current))
            myDiff.append(current)
        else:
            difference = current - prev
            print(difference)
            myDiff.append(difference)
    elif pos_val == "NNP":
        print(pos_val, current)
        myNPs.append(pos_val)
        if(current < prev):
            print("\t" + str(current))
            myDiff.append(current)
        else:
            difference = current - prev
            print(difference)
            myDiff.append(difference)
    elif pos_val == "NNPS":
        print(pos_val, current)
        myNPs.append(pos_val)
        if(current < prev):
            print("\t" + str(current))
            myDiff.append(current)
        else:
            difference = current - prev
            print(difference)
            myDiff.append(difference)
    elif pos_val == ".":
        print(pos_val, current)
        if(current < prev):
            print("\t" + str(current))
            myDiff.append(current)
        else:
            difference = current - prev
            print(difference)
            myDiff.append(difference)
print(myNPs)

#It counts the number of NPs appended to myNPs list.
print("Total NPs: ", len(myNPs))
print(myDiff)
print(len(myDiff))

# It calculates the sum of the differences appended to myDiff list.
sum = 0
for i in range(len(myDiff)):
    sum = sum + float(myDiff[i])
print("The total sum of differences is: ", sum)

'''It calculates the mean distance between NPs by dividing
the total sum of differences by the number of NPs'''

print("The mean distance between NPs is: ", sum / len(myNPs))





