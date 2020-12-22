# Working with data and files

## 1.4.1 Starting in the right place
First, to make sure you start in the right place do this:
```bash
cd ~/BIOS3010/Module-1-Unix-Python
```
Then,
```diff
! Navigate into the `data` folder
! What is found within the `data` folder?
```

If you do not remember how to navigate into the folder and see its contents, you should [look at the part 1 of the exercises again](Unix-1.md).

## 1.4.2 Looking at some data
To look at the content within a file, use `cat`:
```bash
cat molweights.txt
```

```diff
! What is found within the file `molweights.txt`?
```
(If you are experiencing errors with missing files and directories, you should run the following command `git stash` and then start on step 1.4.2 again.)

```diff
! Note:
! Do not use `cat` on big or non-text files. This might stall your system.
! If you get stuck like this, use [CTRL]-c 
```

## 1.4.3 Counting lines in files
To count the number of lines in `molweights.txt` do this:
```bash
wc -l data/molweights.txt
```
Here we use the `wc` ("word count") command with the `-l` flag to get the number of lines.

```diff
! How many lines are in `molweights.txt`?
```

## 1.4.4 Looking at the first lines in files
To only see the top part of a file, do:
```bash
head molweights.txt
```
This will print the first 10 lines of the file

```diff
! Note:
! The `head` command is extremely useful go get a quick view of a text file
```

## 1.4.5 Looking at the last lines in files
To only see the last part of a file, do:
```bash
tail molweights.txt
```
This will print the last 10 lines of the file

## 1.4.6 Sorting file content alphabetically
You may have noticed that the contents of the `molweights.txt` file is not alphabetically sorted according the the 3-letter amino acid codes. To sort the content of the file alphabetically, do:

```bash
sort molweights.txt
```

```diff
! Verify quickly that the output is sorted alphabetically
! Is the `molweights.txt` now sorted? (hint: use `cat` on it)
```

## 1.4.7 Sorting file content numerically
The numbers in the second column are the molecular weights of the amino acids. To sort the amino acids numerically by molecular weight, do:

```bash
sort -k 2n molweights.txt
```
In the above command `-k 2n` sets the sorting to column `2` and the `n` specifies that this is numerical sort.

```diff
! Verify quickly that the output is sorted alphabetically
! Is the `molweights.txt` now sorted by molecular weight? 
```

## 1.4.7 Redirecting command output to files
To store the output of a command in a new file, we can use the `>` symbol to "redirect" the output to a file. Do this:
```bash
sort molweights.txt > molweights.sorted.txt
```
```diff
! Has a new file been created?
! If so, inspect the file
! Is the new file sorted?
! Do the same as above, but create a new file sorted by molecular weight
```

```diff
! Note:
! Never redirect the output of a command that operates on a file to the same file
```

## 1.4.8 Piping command output into other commands

TBD.

- See: http://swcarpentry.github.io/shell-novice/04-pipefilter/index.html
