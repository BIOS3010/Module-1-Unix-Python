In these exercises, you will be introduced to how to navigate in the filesystem on your computer using the shell.

# Working and navigating with directories/folders
Your computer organizes files and directories (these are sometimes called "folders") in a file system. As you probably already know, files contain data and information, and directories contain files and/or other directories. On your computer, you are probably used to clicking on files and folders to navigate around in them. On the shell, however, all oparations has to be done using commands. Here, we will learn the basic (and important) commands allowing us to move around in the file system on our computer.

## 1.3.1 Printing our current position ("where we are") in the filesystem  
Type in the following command in the terminal
```bash
pwd
```
This `pwd` (print working directory) command prints your current position in the file system. The output should be similar to: `[/your/home/]/BIOS3010`, where `[/your/home/]` is the position of your "home directory". Note that the path will look different on different computers. On a windows machine, it might look something like this:  `C:\Users\myname\BIOS3010\`, and on a Mac it could look like this: `/Users/myname/BIOS3010`. Your

To understand what a ‘home directory’ is, let’s have a look at how the file system as a whole is organized. For the sake of this example, we’ll be illustrating the filesystem on the (made up) scientist Nelle’s computer. After this illustration, you’ll be learning commands to explore your own filesystem, which will be constructed in a similar way, but not be exactly identical.

On Nelle’s computer, the filesystem looks like this:
![](https://user-images.githubusercontent.com/5373069/102868272-47e64f80-443a-11eb-90fa-1ea4a6e84f21.png)

The file system is made up of a root directory that contains sub-directories
titled `bin`, `data`, `users`, and `tmp`.

At the top is the root directory that holds everything else. We refer to it using a slash character, `/`, on its own; this is the leading slash in `/Users/nelle`.

Inside that directory are several other directories: `bin` (which is where some built-in programs are stored), `data` (for miscellaneous data files), `Users` (where users’ personal directories are located), `tmp` (for temporary files that don’t need to be stored long-term), and so on.

We know that our current working directory `/Users/nelle` is stored inside `/Users` because `/Users` is the first part of its name. Similarly, we know that `/Users` is stored inside the root directory `/` because its name begins with `/`.

```diff
! Note:
! There are two meanings for the / character:
! When it appears at the front of a file or directory name, it refers to the root directory.
! When it appears inside a path, it’s just a separator.
```

Underneath `/Users`, we find one directory for each user with an account on Nelle’s machine, her colleagues `imhotep` and `larry`.

![](https://user-images.githubusercontent.com/5373069/102868346-5df41000-443a-11eb-9212-1293ade3eecd.png)

The user `imhotep`’s files are stored in `/Users/imhotep`, user `larry`’s in `/Users/larry`, and Nelle’s in `/Users/nelle`. Because Nelle is the user in our example here, this is why we get `/Users/nelle` as our home directory. Typically, when you open a new command prompt you will be in your home directory to start.

```diff
! Note:
! The "home directory" is the base directory of our user
! The "working directory" is where we are currently placed in the filesystem
```

## 1.3.2 Listing files and directories in our working directory

```bash
ls
```

This will list the files and direcories in our current working directory.
```diff
! Which directories and files are in your current working directory?
```

If you are having trouble distinguising between directories and files, you can use `ls -F` to show a `/` after each directory (and a `*` after the executables).


## 1.3.3 Navigating into a directory
From the step above, you should have seen a single directory called `Module-1-Unix-Python` inside the `BIOS3010` directory. To navigate into the `Module-1-Unix-Python` execute the following command:

```bash
cd Module-1-Unix-Python
```
```diff
! What is now the path of your working directory?
! Which files and folders are inside the Module-1-Unix-Python directory?
```

## 1.3.4 Navigating one step up in the directory
From the step above, you entered into the `Module-1-Unix-Python`, to move one step up again (into the "parent directory"), execute:
```bash
cd ..
```
```diff
! What is now the path of your working directory?
```

```diff
! Note:
! The two dots (`..`) are used as a shortcut to "one step up" in the filesystem.
```

## 1.3.5 Using `.` as a reference to your working directory
First, enter back into the `Module-1-Unix-Python` directory. This time, we will do this with another shortcut (a single dot, `.`)
```bash
cd ./Module-1-Unix-Python
```
This is equivalent to `cd Module-1-Unix-Python`, but we use it here to show you that the single dot `.` can be used as a reference to your current working directory. This reference can come in handy from time to time.

```diff
! Note:
! A single dot (`.`) is used as a shortcut to your current working directory in the filesystem.
```

## 1.3.6 Using `~` as a reference to your home directory
While we are at it, let's take a look at another refence, this time to your home directory:
```bash
cd ~/BIOS3010/Module-1-Unix-Python
```
Again, here, this is equivalent to `cd Module-1-Unix-Python`, but the `~` which is a shortcut reference to your home directory is very useful. You can use the above command if you get "lost" somewhere in the filesystem and want to go back to the base directory of this week's exercises.

```diff
! Note:
! The tilde character (`~`) is used as a shortcut to your home directory in the filesystem.
```
## 1.3.7 Navingating back and forth in the filesystem
```diff
! Spend 3-5 minutes using the above commands to move around in the filesystem in the BIOS3010 folder we created
```
When you are done make sure to go back to the directory for this week's exercises:

```bash
cd ~/BIOS3010/Module-1-Unix-Python
```

## 1.3.8 Clearing the terminal
Whenever you want to clear all the text in the terminal to make it easier to get an overview for the next command. Type in:
```bash
clear
```
This will just remove the text in the terminal, and will not change or delete anything. It is always safe to use `clear` whenever you need a clean terminal.

## 1.3.9 Creating a new directory

To create a new directory, use the `mkdir` command followed by the name of the new/empty directory:
```bash
mkdir hello
```

```diff
! Use the commands we learned about to:
! List the name of the new folder
! Navigate into the new folder
! Navigate one step up
```

## 1.3.10 Removing directories
In the step above, we created an empty directory. Delete the empty directory using `rmdir`:
```bash
rmdir hello
```

```diff
! Try the above command on the directory named `data`
! What happens?
```

## 1.3.11 Removing files
In the step above, we removed a directory. To remove a file use the `rm` command:
```bash
rm README.md
```
```diff
! Check that the README.md file is removed
```

```diff
Note:
! Be careful when removing files!
! On Unix, removed files are lost forever and not placed in a trashcan
```
## 1.3.12 Moving directories and files
To move a directory or a file, we use the `mv` command. Run this:
```bash
mv data/molweights.txt .
```
Note that `mv` takes in two "arguments" like this: `mv [argument1] [argument2]`, where each of the two arguments are a path to a file or a directory. The first argument gives the file/directory that should be moved, and the second argument gives the path in the filesystem where it should end up.

```diff
! Where did the `molweights.txt` end up? (hint: use `ls`)
! Explain the logic of the command above
```

```diff
! Note:
! An "argument" is something you provide when you run a command
! Some commands (like `pwd`) take no arguments, some take 1, 2 or even more arguments
! When we used `-F` in step 1.3.2 above, this is called a "flag"
```

Now, move the `molweights.txt` file back into the `data` folder:
```bash
mv molweights.txt data/
```
```diff
Note:
! The `mv` command can also be used to move entire directories around
```

## 1.3.13 Renaming directories and files**
In the above step, we learned about the `mv` command to move files and directories. If you by accident misspelled the name of the `data` directory, for example, you may have noticed that you can rename files and folders by "moving them" to a new name again using `mv?`. To this:
```bash
mv data/molweights.txt data/moleculeweights.txt
mv data dataset
```

```diff
! What happened in the two lines above?
```
Now, rename the file and directory back to their original names:
```bash
mv dataset/moleculeweights.txt dataset/molweights.txt 
mv dataset data
```

## 1.3.14 Using TAB to speed things up
You may already have noticed, but you can use tab as a shortcut instead of typing long paths. Type in:
```bash
ls da
```
and stop there. Then:
```diff
! press the TAB key on your computer
! What happens?
! press the TAB key again
! What happens?
```

## 1.3.15 Other useful shortcuts
These shortcuts can speed up things even further:

- [CTRL]-a: Go to start of line, just after the prompt
- [CTRL]-e: Go to end of line
- [CTRL]-u: Delete everything before the cursor
- [CTRL]-k: Delete everything after the cursor
- [CTRL]-c: Kills (stops) a job that is running
- Using the up/down arrows on your keyboard, you can display your previous commands

```diff
! Type in some random text in the terminal window
! Try out the above shortcuts
```

```diff
! Note:
! If you ever get stuck in a command that never ends, [CTRL]-c is your friend
```

## 1.3.16 Getting help in using the commands

TBD: --help and `man

## 1.3.16 A summary of what we have learned
You have now learned about the following commands/concepts:
- cd 
- mkdir
- pwd
- ls
- rmdir
- rm
- mv 
- ..
- /
- ~
- Some shortcuts to speed things up

```diff
! See if you remember what each of the above commands and concepts do
! Remembering these basics can speed things up for you in the course
```

Now [go to the second part of the exercises](Unix-2.md)



(Some of the examples are taken from here [http://swcarpentry.github.io/shell-novice/02-filedir/index.html)

