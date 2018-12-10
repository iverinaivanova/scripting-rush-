#### scripting-rush-

## A script that calculates the distance between NP occurences in a text

## Components:
*xml Element Tree Module for parsing xml files

## How it works:
1. Use Python3.x
2. Import the ET (Element Tree) module to parse an xml file(s)
  ```
  import xml.etree.ElementTree
  ```
3. Make sure that you give the correct path to the xml file that you want to parse. The xml file directory should appear between the single quotes.
  ```
  my_tree1 = xml.etree.ElementTree.parse(' ').getroot()
 ```
