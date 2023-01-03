**Course Level Programming Assignment - Programming a Calculator using
Python**

In this assignment you will write a computer program from scratch using
the Python programming language. This program will function as a simple
calculator.

**Objectives**

  - Write a simple Python program that performs arithmetic operations
    based on the user input

**Stage 1: A simple calculator**

Your calculator should provide the following arithmetic and control
operations.

  - Arithmetic Operations
    
      - Addition (+)                 add(a,b)
    
      - Subtraction (-)             subtract(a,b)
    
      - Multiplication (\*)         multiply(a,b)
    
      - Division (/)                  divide(a,b)
    
      - Power (^)                    power(a,b)
    
      - Remainder (%)            remainder(a,b)

  - Control Operations
    
      - Terminate (\#)
    
      - Reset ($)

Write a function select\_op(choice) to select the appropriate
mathematics function based on the users selection.

The behavior of the program should be as follows:

  - The program should ask the user to specify the desired operation
    (addition/subtraction/multiplication/division/power/remainder/terminate/reset). **You
    can start with the code already given in the answer box**. Also,
    check the example test cases given below.

  - Once the user inputs/selects an arithmetic operation, the program
    should ask the user to enter the two operands one by one, separated
    by Enter key. If the user made a mistake while entering the
    parameters, he can return to main menu by pressing ‘$’ key at the
    end of the input string, followed by the Enter key

  - Calculate the result and display the result. Inputs need to be
    processed as floating point values, even thought the values entered
    are integers. Example: 2.0 + 4.0 = 6.0

  - Return to main menu after displaying the calculation result

  - All possible errors (at input or at generation of result) should be
    handled by the program
    
      - Examples: 

<!-- end list -->

  - Anything other than a number as operand input

  - Anything other than +, -, \*, /, ^ and % as arithmetic operators

  - Anything other than \# and $ as control operators

  - Division by zero

<!-- end list -->

  - The program should keep running until it is stopped by the user
    (using the terminate command \#)

**Task 1:** Get user input 

  - Section 1: 

<!-- end list -->

  - Input Arithmetic operation

  - Reset or Termination

<!-- end list -->

  - Section 2: 

<!-- end list -->

  - Input first operand

  - Input second operand

  - Reset or Termination

**Task 2:** Implement functions that performs given arithmetic operation
on the given operands and produces the result

  - Arithmetic operation and the two operands as parameters

  - Return the result of the arithmetic operation

**Task 3:** Call the calculation function by passing user input
to select\_op(choice) and display the result from within
the select\_op(choice) function

        Here are some of the messages you might want to display to the
users at certain occasions. Copy and paste them as necessary in your
code in appropriate situations to help with auto-grading.  If there is
any differences between the output of your code and the expected output,
it will be displayed once you click the "Check" button. You can click on
"Show differences" button to highlight the difference between outputs.
This will be helpful for you to change your code to match the expected
output.

"Enter first number: "  
"Enter second number: "  
"Not a valid number,please enter again"  
"Unrecognized operation"  
"Something Went Wrong"


**For example:**

<table>
<thead>
<tr class="header">
<th><strong>Input</strong></th>
<th><strong>Result</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>#</td>
<td><p>Select operation.</p>
<p>1.Add : +</p>
<p>2.Subtract : -</p>
<p>3.Multiply : *</p>
<p>4.Divide : /</p>
<p>5.Power : ^</p>
<p>6.Remainder: %</p>
<p>7.Terminate: #</p>
<p>8.Reset : $</p>
<p>Enter choice(+,-,*,/,^,%,#,$): #</p>
<p>Done. Terminating</p></td>
</tr>
<tr class="even">
<td><p>+</p>
<p>2</p>
<p>4</p>
<p>#</p></td>
<td><p>Select operation.</p>
<p>1.Add : +</p>
<p>2.Subtract : -</p>
<p>3.Multiply : *</p>
<p>4.Divide : /</p>
<p>5.Power : ^</p>
<p>6.Remainder: %</p>
<p>7.Terminate: #</p>
<p>8.Reset : $</p>
<p>Enter choice(+,-,*,/,^,%,#,$): +</p>
<p>Enter first number: 2</p>
<p>Enter second number: 4</p>
<p>2.0 + 4.0 = 6.0</p>
<p>Select operation.</p>
<p>1.Add : +</p>
<p>2.Subtract : -</p>
<p>3.Multiply : *</p>
<p>4.Divide : /</p>
<p>5.Power : ^</p>
<p>6.Remainder: %</p>
<p>7.Terminate: #</p>
<p>8.Reset : $</p>
<p>Enter choice(+,-,*,/,^,%,#,$): #</p>
<p>Done. Terminating</p></td>
</tr>
<tr class="odd">
<td><p>/</p>
<p>5</p>
<p>0</p>
<p>#</p></td>
<td><p>Select operation.</p>
<p>1.Add : +</p>
<p>2.Subtract : -</p>
<p>3.Multiply : *</p>
<p>4.Divide : /</p>
<p>5.Power : ^</p>
<p>6.Remainder: %</p>
<p>7.Terminate: #</p>
<p>8.Reset : $</p>
<p>Enter choice(+,-,*,/,^,%,#,$): /</p>
<p>Enter first number: 5</p>
<p>Enter second number: 0</p>
<p>float division by zero</p>
<p>5.0 / 0.0 = None</p>
<p>Select operation.</p>
<p>1.Add : +</p>
<p>2.Subtract : -</p>
<p>3.Multiply : *</p>
<p>4.Divide : /</p>
<p>5.Power : ^</p>
<p>6.Remainder: %</p>
<p>7.Terminate: #</p>
<p>8.Reset : $</p>
<p>Enter choice(+,-,*,/,^,%,#,$): #</p>
<p>Done. Terminating</p></td>
</tr>
</tbody>
</table>

Answer:(penalty regime: 0 %)
