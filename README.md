#README 

##Environment setup

#### Install required filesets

$ pip3 install -r requirements.txt

#### Run web server in 127.0.0.1:5000

$ python main.py index.py

#### Test

The test program will generate two requests:

-  Normal request, for simulating daily user request
-  Abnormal request, for simulating unwanted hacking behaviour


##### Run test

$ python test.py

#### Expected result

The normal request should get the response from server. Based on the setting, the abnormal request should be terminated, or sending a warning to user.
Web.log file in server side should generate two new log entries:

-  A logged normal request
-  A logged suspicious request

Also it will generate the run time of function Sample:

* INFO - mock_db spent 0.0 s
* INFO - 127.0.0.1 - - [22/Oct/2019 23:19:18] "POST / get_user_info HTTP/1.1" 200 -
* WARNING - being attacked
* INFO - mock_db spent 0.0009999275207519531 