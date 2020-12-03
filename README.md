# bath_est.py

## Table of contents
* [About](#about)
* [Example](#example)
* [Setup](#setup)
* [Errors](#errors)
* [Ideas](#ideas)

## About
One of the most important parts of any job, including construction, is pricing the job correctly. In addition the time it takes to 
properly price a job is time consuming. bath_est.py was my very first "program". I tried to "model" pricing a bathroom renovation
in order to address these two issues. 

## Example

The following example was done in spyder using Python 3.7. <br/>

After running bath_est.py the console greets the user and asks for a first and last name, it expects a string input.  
[![Screenshot-from-2020-12-03-13-47-10.png](https://i.postimg.cc/6p98rpGw/Screenshot-from-2020-12-03-13-47-10.png)](https://postimg.cc/8j0kDDHn)

It then asks for a specified date of format (MMM. DD, YYYY). 
[![Screenshot-from-2020-12-03-13-48-28.png](https://i.postimg.cc/9FBMQHgk/Screenshot-from-2020-12-03-13-48-28.png)](https://postimg.cc/F77mT84b)

The program then goes through a series of questions that may be answered easily:
[![Screenshot-from-2020-12-03-13-51-53.png](https://i.postimg.cc/3NT83tX7/Screenshot-from-2020-12-03-13-51-53.png)](https://postimg.cc/Q9fGbkYn)

Finally, the program returns a list of all the material required to complete the job, the cost of material, labor and so on: 
[![Screenshot-from-2020-12-03-13-53-31.png](https://i.postimg.cc/ZKjbhFCt/Screenshot-from-2020-12-03-13-53-31.png)](https://postimg.cc/2VbRQWQ2)

## Setup 
Git clone https://github.com/manuelnjit/bathroom_estimator.git

## Errors 
Some of the options don't run properly, for example if you choose the option "bath" instead of "shower" the program
still loops into the shower condition. 

The labor cost is not based on a mathematical model, therefore the pricing is inaccurate. 

## Ideas 
**Develop a mathematical model for labor costs** 

**Generalize the program**: One example may be to allow calculations for entire houses, different rooms and different jobs. 

**Make the program user friendly**: For example if the program was an application, and a user selected every option they liked, 
but the price is too expensive or inexpensive. Giving the application the ability to change paints and see how that reflects on the price 
in real time, or if they have an option where painting isn't part of the cost and they decide to save the money and paint it themselves. 
