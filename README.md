# Butopea

## Task 1 

### About the Script:
- The script creates a ProductFeed class that connects to a SQLite database and can filter products based on a given query
- The filtered products are returned as a list of dictionaries
- The class also has a method to create an XML file with the filtered product data
- The XML file is created in the same directory as the script, with the filename "feed.xml"
- The main function at the bottom of the script creates an instance of the ProductFeed class and runs a specific SQL query to filter the data, which is then passed to the create_xml_file method to generate the XML file.

### How to run this script:
To run this script, you will need to have Python3 installed on your system.
1. Clone the repo using:
```
git clone https://github.com/abhijeetgupto/Butopea.git
```
2. Navigate to the directory where the script is located:
```
cd <repo_path>/Task1
```
3. Run the script:
```
python task1.py
```

## Task 2

### About the tests:
1. Test 1 - It confirms if a particular square on the webpage have some text and a button, if it doesn't the test will fail.
2. Test 2 - It confirms if a particular square on the webpage have some image,if it contains the image the url of the image is extraxted else the test will fail.
3. Test 3 - It clicks on a particular tab and then confirms if there are ponducts or not, if it contains porducts, their info is extracted else the test will fail.

These tests also creates a file named "results.txt" which log the information that extracted in the same directory.


### How to run these tests on your system
To run this Cypress test script, you will need to have Node.js and Cypress installed on your system.

1. Clone the repo using:
```
git clone https://github.com/abhijeetgupto/Butopea.git
```
2. Navigate to the directory where the script is located:
```
cd <repo_path>/Task2
```
3. Install cypress using
```
npm install cypress
```
4. Run the tests using
```
npx cypress open
```
### results.txt
Results.txt:
[results.txt](https://github.com/abhijeetgupto/Butopea/files/10478082/results.txt)

### Video:

https://user-images.githubusercontent.com/53190754/213997604-8c9c1ca3-4d9d-4c39-9f9b-d597ee4ee6b0.mp4

