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

## 1.4.8 Redirecting command output to files
To store the output of a command in a new file, we can use the `>` symbol to "redirect" the output to a file. Do this:
```bash
sort molweights.txt > molweights.sorted.txt
```
```diff
! Has a new file been created?
! If so, inspect the file
! Is the new file sorted?
! Do the same as above, but create a new file named (molweights.numsort.txt) sorted by molecular weight
```

```diff
! Note:
! Never redirect the output of a command that operates on a file to the same file
```

## 1.4.9 Searching (or "grepping") for content within files
To output lines matching a specific pattern, you can use the `grep` command. For example, to only output the line in the `molweights.txt` file starting with with "Leu", do this:

```bash
grep "Leu" molweights.txt
```
To search for and output all lines starting with "L", do this:

```bash
grep "^L" molweights.txt
```
the `^` specifies that the lines  should start with the "L"  

To specify a search pattern, `grep` uses "regular expressions", an extremely flexible and useful way of searching. We will not use these as part of the course, but if you are interested you can read more about these [here](https://www.cyberciti.biz/faq/grep-regular-expressions/).

```diff
! Which lines in `molweights.txt` start with an L?
! Which lines in `molweights.txt` start with a T?
! Create a file (`molweights.Gl.txt`) containing only lines from `molweights.txt` starting with "Gl"
```

## 1.4.10 Sending (or "piping") command output into other commands
It is also possible to combine multiple commands by sending the output of one command into another command. This is called "piping", and is a powerful way of creating pipelines of commands. To illustrate a simple example, perform the following command:

```bash
grep "T" molweights.txt | sort -k 2n
```
As you see, we use the vertical line `|` character to indicate the the output from the left command should go as input to the right command. 

```diff
! Explain the commands on the left and right side of the `|`
! Make a command that creates a file called "top10.txt" containing the 10 amino acids with the highest molecular weights
```

```diff
Note:
! pipes can chain together many commands: command1 | command2 | command3 (etc.)
! We call commands chained together like this "oneliners"
```

## 1.4.11 Downloading files from the internet
To download files from the internet, you first need the full URL (starting with http, https or ftp) linking to the file you want to download. To download the file, do this:
```bash
curl -O http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/refGene.txt.gz
```
You may already be used to using another command called `wget` to download files. If so, feel free to use `wget` instead of `curl -O`.

```diff
Note:
! What does the `-O` flag do? (hint: --help)
```

## 1.4.12 Unzipping files (`.gz`, `.zip` and `.tar.gz`)
You may have noticed that the name of the file you downloaded in the previous step ends with a `.gz`. If you for example tried using `head` on the file, you noticed a lot of strange symbols. This is because the file is compressed (or "zipped") to save space, and it needs to be decompressed to be read as a normal text file. To decompress or "unzip" the files ending in `.gz` we use the `gunzip` command. Do this to decompress the file:

```bash
gunzip refGene.txt.gz
```

```diff
! See what happened and inspect the file
```

There are also other types of decompressed files. For files ending with `.zip` we use `unzip`. To try this out, do this:

```bash
curl -O https://hgdownload.soe.ucsc.edu/goldenPath/hg18/bigZips/liftAll.zip
unzip liftAll.zip
```

To decompress a file ending with `.tar.gz`, we use the command `tar -zxvf`. To try this out,  do this:

```bash
curl -O http://hgdownload.cse.ucsc.edu/goldenPath/hg19/bigZips/chromTrf.tar.gz
tar -zxvf chromTrf.tar.gz
```

```diff
! Download this file using `curl`:
! http://hgdownload.cse.ucsc.edu/goldenPath/hg19/chromosomes/chr22.fa.gz
! Inspect the file. What do you think it contains?
```

## 1.4.13 A summary of what we have learned
You have now learned about the following commands/concepts:
- cat
- wc 
- head
- tail
- sort
- grep
- "redirection"
- "grepping"
- "piping"

```diff
! See if you remember what each of the above commands and concepts do
! Remembering most of this will help you in the course
```

- See: http://swcarpentry.github.io/shell-novice/04-pipefilter/index.html
