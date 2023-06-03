# **DTL Data Engineer Mini-project**
### A scraper designed to daily download SGX derivatives data.

---
## Installation
```python
pip install -r requirements.txt
```
Dependencies of the project are written in the requirements.txt

It was used with Python 3.9.13 

---

## Usage
Run the program on a command line:
```
python DE_Assessment.py
```
The program would open chrome and direct you to a website.

After that a checkbox widget would open.

![Alt text](Types%20of%20Data.png) ''' ![Alt text](Dates.png)


The Types of Data widget would appear once, while Dates would appear depending on the number of Types of Data was checked.

Every prompt done on the checkbox can be seen on the log file, project_logs.

After answering the checkbox, the program would download the files based on the user's instruction.
The downloads will be located based on the default chrome settings.

---
## Getting the Values
There are two kinds of values on the project: 'checkbox value' and 'positioning value'

---
Checkbox value:

0, represents the unchecked
1, represents the checked

The project would only deal with the user's instruction or the checked.

---
Positioning Value:

This refers to the position of the data after clicking the dropdown. This would be used by the program.

| Type of Data                      | Value |
| :--------------------------------:| :---: |
| Tick                              | 0     | 
| Tick Data Structure               | 1     |
| Trade Cancellation                | 2     |
| Trade Cancellation Data Structure | 3     |

| Dates         | Value |
| :------------:| :---: |
| Newest        | 0     | 
| One Day Ago   | 1     |
| Two Days Ago  | 2     |
| Three Days Ago| 3     |
| Four Days Ago | 4     |

---
## NOTES:
1. The progam currently cannot run on headless mode, there seems to be a bug that it cannot download files when selenium/helium is ran headless.

2. The Historical Data that the webiste have only covers the past 5 market days, other times only four days appear on the dropdown. The program still works fine even on this condition. 

3. Redownloading is possible by comparing the indices that was downloaded to those that was instructed by the user.