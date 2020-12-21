# Module 1: Learning the basics of Bash/UNIX (and repeating Python)
**1. Install a shell on your computer**
- Show here

In the exercises below, all commands that should be run in the shell are shown:

```bash
Like this
```
In some places, you will be asked to do something. This will be shown:
- Like this

In some places, there are questions where you are meant to write down your answer. These are written
```diff
!Like this
```


# Python exercises
* Read [this guide](guide_getting_started_with_python.md) if you need help to get Python installed on your computer.
* [Repetition](Python-exercise1.md) ([Solution](solutions/Exercise1-solution.py))
* [More training](..)

# Unix exercises
In these exercises, you will first try out some basic UNIX commands, and then you will work in groups afterwards. You will learn about the follow UNIX commands and concepts:

**Install gitbash**

**Creating, moving and deleting files**
- mkdir
- rmdir
- cp
- mv
- rm

**1. Entering your home directory: `cd`** 
Type in the following command in the terminal
```bash
cd
```
This command will take you back to your home/user directory.

**2. Creating a new directory: `mkdir`** 
To create a new directory, use the `mkdir` command followed by the name of the new/empty folder:
```bash
mkdir BIOS3010
```

**3. Moving around in the file system** 
To navigate into the newly created folder (with the name BIOS3010), type in the following command:
```bash
cd BIOS3010
```
**4. Using the `pwd` command** 
Type in:
```bash
pwd
```

```diff
! What got printed to the screen when you used the `pwd` command?
```
Obs. Unlike the other commands above, the `pwd` command only prints to the screen, and does not change anything.

**5. `cd ..` **
Type in:

```bash
cd ..
```

```diff
! Use the `pwd` command again. What happened when you typed `cd ..`?
```

**6. `ls`**
Type in:
```bash
ls
```

```diff
! What does the `ls` command do?
```
Obs: Like the `pwd` command, this command command only prints to the screen.

**7. `cd .`**
- Go back to the BIOS3010 (hint: use `cd`).
Then type in:
```bash
cd .
```
Note that we use a single dot instead of two dots like in step 5.

```diff
! What is the difference between `cd .` and `cd ..`
```

Note: `.` (a single dot) and `..` (two dots) can be used as references in all UNIX commands.

**8. `cd ~`**

Type this:
```bash
cd ~ 
```
Now you should be back to your home directory (check with `pwd` and `ls`. The `~` symbol is a general reference to your home diretory, that you can use instead of writing the full path.
Do this:
```bash
cd ~/BIOS3010/ 
```
Now you should be back in the BIOS3010 folder.
```diff
! Check that you are in the BIOS3010 folder (using the some of the commands you just learned)
```


- cp
- mkdir
- rmdir
- mv
- rm

- cat
- head
- tail
- wc
- grep
- sort
- uniq









* Idea: Make your own cheat sheet. Each breakout-group gets assigned a unique set of commands (ls, cd, pwd, etc.), and should describe each and show an example in the terminal. Report on Padlet?
* [Exercise 2: folder structure and navigation](Exercise_2_folder_structure.md) 
* [Exercise 3: Important UNIX commands](Exercise_3_cmds.md) 
