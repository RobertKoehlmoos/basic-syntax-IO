""""
We need your help to write our software that processes new users into our system
Write a program that prompts a user five times for the following information in order:
1. First Name
2. Last Name
3. Year Born
4. Month Born
5. Day Born

And print that information out in the following format:
<First Name> <Last Name> was born on <Month> <Day> in <Year>

Then print out their user id, consisting of the first four letters of their last name,
the first letter of their first name, and the day of the month they were born:
<first four of last name><first letter of first name><Day Born>
(Corporate believes there are no possible issues with this system)

Finally, print out their temporary password, consisting of the last letter of their first name,
their last name backwards, the last digit of the year they were born spelled out lowercase:
<last letter of first name><last name backwards><last digit of year born spelled out>
(Corporate insisted on user friendly passwords)

Finally, print 'Unlucky' if the user was born on the 13th, otherwise print 'Lucky'
(Don't even ask)

But, the user will provide month as a number from 1 to 12 (inclusive), you need to convert it
into the word representing the month.
For example, the below input
Scooby
Doo
1969
9
13

Would print

Scooby Doo was born on September 13 in 1969
ScooD13
yooDnine
Unlucky

Don't worry, the users will only give months consisting of integers that correspond to months that actually exist.

Additionally, it will be tested with the following inputs and outputs:
Bugs
Bunny
1940
7
27

Bugs Bunny was born on July 27 in 1940
BugsB27
synnuBzero
Lucky

Daffy
Duck
1937
4
17

Daffy Duck was born on April 17 in 1937
DaffD17
ykcuDseven
Lucky

Homer
Simpson
1955
5
10

Homer Simpson was born on May 10 in 1955
HomeS10
rnospmiSfive
Lucky

Mickey
Mouse
1928
11
18

Mickey Mouse was born on November 18 in 1928
MickM18
yesuoMeight
Lucky
"""
