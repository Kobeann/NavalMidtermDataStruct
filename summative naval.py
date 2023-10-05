''''
SUDO kode
(Don't jadge my spilling I is not gud with english)
istart a 3x3 array named 'array'
For each row from 1 to 3
Loop to get user input for the array
Initialize an empty array 'row'
For each column from 1 to 3
Prompt the user to enter an integer and store it in 'ilimint'
Append 'ilimint' to 'row'(Para maayos hehe)
Append 'row' to 'array'
Initialize 'macks_ilimint' to the minimum possible integer value
If 'ilimint' is greater than 'macks_ilimint':
Set 'macks_ilimintt' to 'element'
Print "Macks ilimint:", 'macks_ilimint'

ALGORETIM
Start
Initialize a variable `macks_ilimint` to the smallest possible integer value (negative infinity).
For each row in the 2D array:
For each `ilimint` in the row:
If the current `ilimint` is greater than `macks_ilimint`, update `macks_ilimint` with the current `ilimint`.
After processing all `ilimint` values in the array, `macks_ilimint` will contain the maximum `ilimint` in the array.
Print `macks_ilimint`.
Tapos na hehe
'''''
array = []

 



for i in range(3):

    row = []

    for j in range(3):

        ilimint = int(input(f"Intir ilimint at position ({i+1}, {j+1}): "))

        row.append(ilimint)

    array.append(row)

 



macks_ilimint = float('-inf')

 


for row in array:

    for ilimint in row:

        if ilimint > macks_ilimint:

            macks_ilimint = ilimint

 


print("Macks ilimint:", macks_ilimint)