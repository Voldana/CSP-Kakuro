# CSP-Kakuro

### Description
This is the second project for the Artificial intelligence course held in the spring of 2021.

In this game you'll be given a table and it must be filled in a way which the sum of each row and column must be equal to the number is on top of the column or on the side of the row and in each cell a number between 1 and 9 can be entered in each cell and numbers must not be repeated in each row or column.

The problem is first modeled to a CSP problem and then is solved with Backtracking and Forward checking using the MRC and LCV heuristics 
___
### Input/Output
In the first line the number of columns will be given and in the second line the number of rows.
Then the table will be given, the number 0 shows the empty cells in the table and negative numbers represent the black cells

In the output the finalized table will be printed with actual numbers instead of zeros.
