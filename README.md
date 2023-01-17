# pot2graph


When conducting password analysis, there have been times where it has been beneficial to backup my potfile and conduct analysis on a new potfile that is created after cracking some hashes (this typically has been when ive saved my existing potfile as a hashcat.potfile.bk so as not to lose it IT IS NOT RECOMMENDED TO DELETE YOUR POTFILE!)

This script was created as a quick and easy way to create material that will show the lengths of all the unique passwords cracked.
Remember - this will NOT show how many times a password has been cracked or how many passwords have not been cracked, but will provide some insight into whether those users that represent a risk are using short or long passwords.

Usage:
$python3 pot2graph.py
![image](https://user-images.githubusercontent.com/108965118/212789185-127702dc-ce5c-4efc-9b55-8990c38f8e9e.png)

The tool will produce a pie chart (that will be saved as a jpg)
![image](https://user-images.githubusercontent.com/108965118/212789253-2a1dc785-e648-4897-b7be-586e4a522dce.png)

and will save a CSV file for any other analysis you may want to do



Future development:
* Provide statistics on cracked vs not cracked
* Provide statistics on top passwords
* Provide a search query to identify how many passwords were based off of key words such as password, or the company name

