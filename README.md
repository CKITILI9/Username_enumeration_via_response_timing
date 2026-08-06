# Username_enumeration_via_response_timing
Finding a valid username and password by monitoring and manipulating timing responses.
—-------
- The lab is vulnerable to username enumeration via response timing.
- Login requests are usually handled at a specific time.
- If the request takes a different amount of time, there's a chance that the username is valid.
- For instance, a valid username and a random password may take a little longer.
- The time difference suggests that a username may be valid, even when the password is incorrect.
—-------
#Application Response
- The application responds ‘Invalid username or password.’ to a wrong username and password.
- It also responds 'You have made too many incorrect login attempts. Please try again in 30 minute(s).' to numerous failed attempts.
- This means it blocks an IP that makes many incorrect attempts
—------
#Lab Requirements
- Brute force and look for valid username first
- Then brute force and look for a valid password.
—------
#Work Environment
- Kali Linux command line, running as a Virtual Machine on Oracle Box
- The VM is connected to SSH through putty. 
------
# NB: 
- The credential lists will be in 2 separate files, usernames.txt and passwords.txt
- The files should have rwx permissions for user (me)
- The file should be in the same directory with the python script.
—-------
#Testing Response Times
- Enter these credentials:  wiener:peter
- Inspect timing on developer tools, network tab.
- The response is returned in 164 ms. (0.164 seconds)
- Used the same username: wiener and a different password: 123456
- The response is returned in 216 ms (0.216 seconds). Not far off from the first response.
- Therefore, I should look out for a response that takes more than 2 seconds.
—-------
#Key Concept to Remember
- Good time to remind myself the following:
* A valid username takes additional time to compare passwords (password stored on server against what I send)
* Therefore, it makes sense to test a longer password.
* A longer password takes additional time to compare.
* An invalid username takes a shorter time.
* This is because the server rejects invalid username immediately, without comparing passwords.
* TIME MODULE USES SECONDS.
—------
#Script Requirements
- Manually brute forcing the list of usernames isn't possible.
- A script will automate the process, and it will include:
----
* import requests and time modules.
* input for target url.
*A function for formatting username and password list (stripping whitespaces on strings)
* An ip spoofing function to generate fake IPs
* A enumerate_username function
* A loop inside enumerate_username function to send one name at a time.
* Store ip_spoofing function in variable, define headers, data, and start time using time module.
* A post method to send URL, headers, data
* Store end time, compute and store difference in end and start time (end - start)
* Use if to check if the elapsed_time is greater than 2SECONDS.
* Print the valid name and elapsed_time
* Call username_formatter function as an argument to enumerate_username function.
-------
#Testing for Valid Username
- Run the script.
- A valid username will take more than 2 seconds to check password.
- Found a valid username that took longer (5 seconds)
----
![ ](images/image1.jpg)
-----
- As seen in the image, the username as400 took 5 seconds.
- The rest of the responses took between 0.6 seconds to 1 second, as shown in the image below:
----
![ ](images/image2.jpg)
---------
#Password bruteforce
- Next is testing a valid password.
- We’ll need an enumerate_password function that almost resembles enumerate_usernames.
- The snippet is shown below:
----
![ ](images/image3.jpg)
------
#Call the Functions
- Call all the username enumeration and username list functions at the end of the script, store the result in variables.
- When running the script, the application will send ‘None’ when it fails to find a valid username.
- Due to this reason, use an if condition to check for a username that doesn’t have the word ‘None’
- Inside that if condition, call the password enumeration function with the password list, and store the result in a variable.
- Finally, print the valid password.
----
#Run Script
- Before running the script, ensure it prints a valid username first.
- Then, ensure it prints the status_code for every password attempt.
- When the password is valid, the application will redirect to another page, and the status_code changes to 302 (meaning redirect).
- The script successfully generated a valid username and password that redirected to a new page.
---
![ ](images/image4.jpg)
----
- The valid username and password pair is app:letmein
- Enter the credential pair in the challenge’s lab.
- With that, the lab was solved
---
![ ](images/image5.jpg)
----


