# Working with data and files

## 1.4.1 Starting in the right place
First, to make sure you start in the right place do this:
```bash
cd ~/BIOS3010/Module-1-Unix-Python
```
## 1.4.2 Looking at some data
```diff
!First navigate into the `data` folder
```
If you do not remember how to navigate into the folder, you should (look at the part 1 of the exercises again)[Unix-1.md].

To look at the content within a file, use `cat`:
```bash
cat molweights.txt
```
```diff
! What is found within the file `molweights.txt`?
```

(If you are experiencing errors with missing files and directories, you should run the follwing command `git stash` and then start on step 1.4.2 again.)

## 1.4.3 Counting lines in files
To count the number of lines in `molweights.txt` do this:
```bash
wc -l data/molweights.txt
```



If you  1.3.12





- See: http://swcarpentry.github.io/shell-novice/04-pipefilter/index.html
