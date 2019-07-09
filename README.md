# Simulate-Submit-Online-Form

### Description

Use python script to submit online survey form quickly and correctly.  

Write information in excel, let the program read the content as submission data.  

A timer is set and auto submit on time.  

For now only support [问卷星](https://www.wjx.cn).  
Feel free to clone this project and modify some codes to support more platform.  

![run](/web/run-result.png)

***

### Code Explanation  

#### Data Storing 
**data.py**  
Store data objects about the event.  
Initial values are `None`, and will be updated by `fetch.py`

#### Fetch data
**fetch.py**  
Fetching data from excel file and update data in `data.py`.  
The function `current_time` returns current readable time for console print out.  
```python
def current_time() -> str:
    now_time = time.time()
    readable_time = datetime.fromtimestamp(now_time).strftime('%H:%M:%S:%m - ')
    return readable_time
```
  
#### Submit the form
**submit.py**
Fill the form and submit form data.  
The function `selenium_submit(url: str, driver)` accept two parameter:  
* `url`: A string type value, it's passed by `main.py` to determine which form should be submitted.
* 'driver':  Since initial the selenium driver takes a few seconds, the program initial the driver first, and pass it to `submuit.py`.  

The function `wait_until_submit()` is called after the form is filled. It waits an appropriate time until the submit time.

#### Main
**main.py**  
Run this file to run the program.  
The enumeration class determine three cases during the run time:
* `test`: Now is testing time.
* `real`: Now is the time to submit a real registration form.
* `gap`: Now is the time that between testing time and real time.  

According to different time, the function `get_url()` returns different url as string.  
Table-Driven Approach is used in this function.
```python
def get_url() -> str:
    cases = {
        Registration.test: data.test_url,
        Registration.real: data.real_url,
        Registration.gap: data.real_url,
    }

    status = check_registration_status()
    # print(cases[status])
    return cases[status]
```
  


