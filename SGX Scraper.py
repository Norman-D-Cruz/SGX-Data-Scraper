from time import sleep
import tkinter as tk 
from helium import *
import chromedriver_autoinstaller

from selenium.common.exceptions import WebDriverException, TimeoutException, NoSuchWindowException
from urllib.error import URLError

import logging
from datetime import date


logging.basicConfig( filename = "project_logs.log",
                    level = logging.INFO,
                    format = '%(asctime)s - %(levelname)s - %(message)s',
                    datefmt= '%d-%b-%y %H:%M:%S')

logger = logging.getLogger()


try:
    chromedriver_autoinstaller.install()
except URLError:
    logger.error("There is no network connection, Please Connect to the Internet")
    print("Please see the log files for the diagnostic")
    exit()
     
start_chrome("https://www.sgx.com/research-education/derivatives")
scroll_down(100)
logger.info("Chrome Initialized")


def type_dropdown_command(steps):
    """"
    The function would click the Type of Data text and press arrow
    down depending on the index of the data that was passed
    """
    wait_until(Text("Type of Data").exists)    
    click(Text("Type of Data"))
    for x in range(steps):
        sleep(1)
        press(Keys.ARROW_DOWN)
    sleep(1)    
    press(Keys.ENTER)    

def date_dropdown_command(steps):
    """
    The function would click the Date text and press arrow
    down depending on the index of the data that was passed.
    It would then click the download button.
    The entire action would be repeated base on the number of
    days needed.
    """
    for index in steps:
        wait_until(Text("Date").exists)  
        click(Text("Date"))
        for i in range(index):
            sleep(1)
            press(Keys.ARROW_DOWN)
        sleep(1)
        press(Keys.ENTER) 
        sleep(1)
        click(Button("Download"))
        sleep(5) 

sleep(3)


# Open a simple checkbox GUI to ask the Type of Data the user want
# The check button would take a boolean value, 0 means unchecked: 1 means checked

root = tk.Tk()
root.geometry("275x200")

values = []

t = tk.Label(root, text ='Types of Data', font = "15", height=2) 
t.pack()

type1 = tk.IntVar()
type2 = tk.IntVar()
type3 = tk.IntVar()
type4 = tk.IntVar()

c1 = tk.Checkbutton(root, text= "Tick", variable= type1).pack(padx=35, anchor="w")
c2 = tk.Checkbutton(root, text= "Tick Data Structure", variable= type2).pack(padx=35, anchor="w")
c3 = tk.Checkbutton(root, text= "Trade Cancellation", variable= type3).pack(padx=35, anchor="w")
c4 = tk.Checkbutton(root, text= "Trade Cancellation Data Structure", variable= type4).pack(padx=35, anchor="w")

def checkbox_values():
    checkbox_values = [type1.get(), type2.get(), type3.get(), type4.get()]
    values.append(checkbox_values)
    root.destroy()

submit_button = tk.Button(root, text="Submit", command=checkbox_values)
submit_button.pack()

root.mainloop()



try:
    for value in values:
        pass
    if value == [0,0,0,0]:
        logger.warning("Please click a checkbox before hitting submit")
        kill_browser()
        exit()
        
    else:
        logger.info(f"Selected Types: {value}")
        types_of_data = {'Tick': value[0] , 'Tick Data Structure' : value[1] ,'Trade Cancellation': value[2], 
                    'Trade Cancellation Data Structure': value[3]}
except NameError:
    logger.warning("The Type of Data widget was closed")
    kill_browser()
    exit()
    
# The loop would only work on checked Types of Data
# Inside the loop is another GUI that would ask about the dates to be download
# NOTE: Please refer to the README.md for information about indexing/position

for position,data in enumerate(types_of_data):
    if types_of_data[data] == 1:
                
        window = tk.Tk()
        window.geometry("250x200")

        date = tk.Label(window, text ='Dates', font = "15", height=1) 
        date.pack()

        date_values = []

        date1 = tk.IntVar()
        date2 = tk.IntVar()
        date3 = tk.IntVar()
        date4 = tk.IntVar()
        date5 = tk.IntVar()

        d1 = tk.Checkbutton(window, text= "Newest", variable= date1).pack(padx=35, anchor="w")
        d2 = tk.Checkbutton(window, text= "One Day Ago", variable= date2).pack(padx=35, anchor="w")
        d3 = tk.Checkbutton(window, text= "Two Days Ago", variable= date3).pack(padx=35, anchor="w")
        d4 = tk.Checkbutton(window, text= "Three Days Ago", variable= date4).pack(padx=35, anchor="w")
        d5 = tk.Checkbutton(window, text= "Four Days Ago", variable= date5).pack(padx=35, anchor="w")

        def date_checkbox_values():
            date_checkbox_values = [date1.get(), date2.get(), date3.get(),
                                    date4.get(), date5.get()]
            date_values.append(date_checkbox_values)
            window.destroy()

        submit_button = tk.Button(window, text="Submit", command=date_checkbox_values)
        submit_button.pack()

        window.mainloop()


        d_index_list = []
            
        for date_value in date_values:
            for d_position, date_val in enumerate(date_value):
                if date_val == 1:
                    d_index_list.append(d_position)
                else:
                    pass  
        
        logger.info(f"{data} selected dates: {d_index_list}")
        

        # After setting up the parameters from GUI the function for dropdown would commence
        try:
            type_dropdown_command(position)
            date_dropdown_command(d_index_list)
        except WebDriverException:
            logger.error("You have accidentally closed Chrome")
            exit()
        except TimeoutException:
            logger.error("The driver stopped")
            exit()
        except NoSuchWindowException:
            logger.error("Window was closed")
            exit()
        except LookupError:
            logger.warning("Scraper could not detect it")
            print("See log files for diagnostic")
            kill_browser()
            exit()

        sleep(3)
        logger.info(f"-------- {data} Download Complete --------")
    
    else:
        pass

logger.info("BROWSER CLOSED")
sleep(2)
kill_browser()