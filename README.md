
# **Radians to Degrees Function**

I literally just Googled Python projects and pulled the first ones I found [here](https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/): **Convert Radians into Degrees.** The website _did_ say that there's already a function in Python that could do that _but_ the challenge is to figure out how to do it myself. I'm currently a student and took my first Python class last semester and I wanted to keep practicing and learning. I want to be able to say, "I know Python!" But I still have so much to learn.

## **The Challenge:**
The website only said to write a function that accepted a numerical value as a parameter--the value was to be the radians of an angle and the function would convert the radians to degrees. I _could_ have just left it at that... But that's boring. I wanted to:
* Get user input
  * _Validate_ the user input
* Print the result
* Ask if the user wanted to enter another value
  * Validate _that_, too
* Say goodbye when the user was done. Because it's _polite_.

### **The Process**
1. Using the hint, "You can import the value for Pi from Python’s math module," I looked through the Python documentation to figure out what the python math module _for_ Pi is.

2. Imported the math module.

3. Defined the function: **radianstodegrees(rad)**.
3a. Here I tried to create variables: `degrees` (_where I set the value to the equation to convert to degrees_) and `choice`. I wanted to use `choice` to carry the rest of the function.

4. I tried to create a while loop where I said `while choice == "y" or choice == "Y":` **_but_** I realized that it interfered with the flow of logic. I couldn't remember the method to make it so that I didn't _have_ to type so much (yaaaaay optimization) for _a while_. Eventually, I _did_ figure it out and reordered my while loops and logic. I kept the `degrees` and `choice` variables and just reordered them like so:
```
while True:
    degrees = rad * (180 / math.pi)
    print(an f string that shows the answer)
    choice = input(get user input to continue or not).lower()
```
5. Here I started another while loop to validate the user input by checking `choice` against an array with "y" and "n" in it. If the input was _not_ in the array, I prompted the user for input again.

6. Created an `if` statement (_if `choice` == "y"_).
6a. Got user input with a try/except statement to validate that the input was numerical. The `try` part got a new `rad` value from the user (_then started the main `while` loop back over_), and the `except` statement printed an error prompting the user to enter a numerical value.

7. Created an `else` statement:
```
if choice == "y"
    #try/except statements
else: return "Goodbye!"
```
8. Created the variable `radians` to get initial user input _outside_ the function.

9. Printed the function, passing the `radians` variable into the function parameter.

# **BAM, done!**

### What I Learned:
* You can literally just start a while loop with `while True`. I forgot that.
* Math.pi method.
* Refreshed my memory of the .lower() method.
* I can use an array to start a while loop.
* Python doesn't like camel case notation.
* I have so, so, so much left to learn.

### **Thanks for reading!**
