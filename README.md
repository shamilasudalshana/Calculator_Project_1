# Calculator_Project_1
This is my python code for a calculator assignment 


Course Level Programming Assignment - Programming a Calculator using Python
In this assignment you will write a computer program from scratch using the Python programming language. This program will function as a simple calculator.
Objectives
•	Write a simple Python program that performs arithmetic operations based on the user input
Stage 1: A simple calculator
Your calculator should provide the following arithmetic and control operations.
•	Arithmetic Operations
o	Addition (+)                 add(a,b)
o	Subtraction (-)             subtract(a,b)
o	Multiplication (*)         multiply(a,b)
o	Division (/)                  divide(a,b)
o	Power (^)                    power(a,b)
o	Remainder (%)            remainder(a,b)
•	Control Operations
o	Terminate (#)
o	Reset ($)
Write a function select_op(choice) to select the appropriate mathematics function based on the users selection.
The behavior of the program should be as follows:
•	The program should ask the user to specify the desired operation (addition/subtraction/multiplication/division/power/remainder/terminate/reset). You can start with the code already given in the answer box. Also, check the example test cases given below.
•	Once the user inputs/selects an arithmetic operation, the program should ask the user to enter the two operands one by one, separated by Enter key. If the user made a mistake while entering the parameters, he can return to main menu by pressing ‘$’ key at the end of the input string, followed by the Enter key
•	Calculate the result and display the result. Inputs need to be processed as floating point values, even thought the values entered are integers. Example: 2.0 + 4.0 = 6.0
•	Return to main menu after displaying the calculation result
•	All possible errors (at input or at generation of result) should be handled by the program
o	Examples: 
•	Anything other than a number as operand input
•	Anything other than +, -, *, /, ^ and % as arithmetic operators
•	Anything other than # and $ as control operators
•	Division by zero
•	The program should keep running until it is stopped by the user (using the terminate command #)


Task 1: Get user input 
•	Section 1: 
•	Input Arithmetic operation
•	Reset or Termination
•	Section 2: 
•	Input first operand
•	Input second operand
•	Reset or Termination
Task 2: Implement functions that performs given arithmetic operation on the given operands and produces the result
•	Arithmetic operation and the two operands as parameters
•	Return the result of the arithmetic operation
Task 3: Call the calculation function by passing user input to select_op(choice) and display the result from within the select_op(choice) function
        Here are some of the messages you might want to display to the users at certain occasions. Copy and paste them as necessary in your code in appropriate situations to help with auto-grading.  If there is any differences between the output of your code and the expected output, it will be displayed once you click the "Check" button. You can click on "Show differences" button to highlight the difference between outputs. This will be helpful for you to change your code to match the expected output.
"Enter first number: "
"Enter second number: "
"Not a valid number,please enter again"
"Unrecognized operation"
"Something Went Wrong"
Some common issues and solutions are explained in This Forum Post

For example:
Input	Result
#	Select operation.
1.Add      : +
2.Subtract : -
3.Multiply : *
4.Divide   : /
5.Power    : ^
6.Remainder: %
7.Terminate: #
8.Reset    : $
Enter choice(+,-,*,/,^,%,#,$): #
Done. Terminating
+
2
4
#	Select operation.
1.Add      : +
2.Subtract : -
3.Multiply : *
4.Divide   : /
5.Power    : ^
6.Remainder: %
7.Terminate: #
8.Reset    : $
Enter choice(+,-,*,/,^,%,#,$): +
Enter first number: 2
Enter second number: 4
2.0 + 4.0 = 6.0
Select operation.
1.Add      : +
2.Subtract : -
3.Multiply : *
4.Divide   : /
5.Power    : ^
6.Remainder: %
7.Terminate: #
8.Reset    : $
Enter choice(+,-,*,/,^,%,#,$): #
Done. Terminating
/
5
0
#	Select operation.
1.Add      : +
2.Subtract : -
3.Multiply : *
4.Divide   : /
5.Power    : ^
6.Remainder: %
7.Terminate: #
8.Reset    : $
Enter choice(+,-,*,/,^,%,#,$): /
Enter first number: 5
Enter second number: 0
float division by zero
5.0 / 0.0 = None
Select operation.
1.Add      : +
2.Subtract : -
3.Multiply : *
4.Divide   : /
5.Power    : ^
6.Remainder: %
7.Terminate: #
8.Reset    : $
Enter choice(+,-,*,/,^,%,#,$): #
Done. Terminating
Answer:(penalty regime: 0 %)

