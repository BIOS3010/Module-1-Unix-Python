# Getting started with Python

In this course, we primarily want you to run Python programs from the command line in a unix-like environment. This way, what you learn will be closer to a typical bioinformatics-like setting where you run different tools on the command line.

The first step is thus to have a terminal and be able to navigate around on it 

### Step 1: Make sure you have a terminal
#### Mac (osX)

If you are on a Mac computer, you already have a terminal installed, and can open that e.g. by opening the Launchpad and typing terminal. You will also find the terminal in the Applications folder.

#### Windows

We recommend that you use gitbash, which gives you a unix-like environment on Windows. Follow [this guide (see the section "The Bash shell")](https://carpentries.github.io/workshop-template/).

#### Linux

Linux-systems all have a terminal built in. You probably know how to open this if you are a linux-user.


### Step 2: Make sure you know how to navigate on the terminal

It is important that you feel somewhat comfortable navigating directories on the command line. You should at least know the following commands. If you do not feel comfortable using them, it is a good idea to spend some time playing around with them:

* `ls`: List all files and folder in the current directory
* `pwd`: Get the full path of the current directory. Useful if you don't know where you are.
* `cd somedirectory`: Change directory to `somedirectory`. You can use `cd ~` to go to your home directory, which is a good idea if you are a bit lost.

Also, make sure you know these tricks which will save you a lot of time:
* Use *tab* to autocomplete commands and folder/file-names. When you are navigating to a folder, you should never type the full folder name (unless it is very short). Only type the first few letters, and then press tab to autocomplete.
* Use arrow up to go back to the previous command you ran. When you are running python scripts, you will very often want to re-run the last command. You simply do this by pressing arrow up on the keyboard and then enter.
* Don't use spaces in folder or file names. Since unix commands use spaces to separate arguments, spaces in file and folder names are a bad idea since the names then will be interpreted as separate arguments to a command. The best solution is to just use underscore instead of space. Some people also like to always only use lowercase letters for all file and folder names, so that one doesn't need to remember whether uppercase or lowercase was used.


### Step 3: Get a program for writing code in
When writing Python code, you need to write it in a text-editor (not in a program like Word). On windows, you most likely already have Notepad installed, which works fine. However, there are other options that give you a bit more functionality (like syntax highlightning, line numbers, etc):
* [Notepad++](https://notepad-plus-plus.org/downloads/)
* [Atom](https://atom.io/)

These two should both be fairly easy to install and get started using.

When you have a text-editor, try to make a new file in it and save the file somewhere as `test.py`. Write the following in `test.py` and save it:
```
print("Hello")
```
 
 Make sure you know where you saved it. Then try to go to the terminal and navigate to where you saved id. Use the command `ls` to verify that the file is there.


### Step 3: Get Python installed and test it out
You may already have Python installed on your system.

If you are on windows, simply try typing `python` in the gitbash terminal window and then enter. If you don't get any error messages, that means you have python installed. You will also see a version number. After typing `python` you will go into an interactive python shell. In order to come out from the shell, type `exit()` and then enter.

If you are on mac, your python command may be `python3` instead. Type `python3` in the terminal window in order to see if you have Python installed.

If you don't have Python installed, follow this guide to install it (see the Python section): [https://carpentries.github.io/workshop-template/#python](https://carpentries.github.io/workshop-template/#python)



### Step 4: Run the python script
If you now have Python installed, use the terminal window to navigate to the directory where you created your test.py file. Simply type `python test.py` or `python3 test.py` (depending on your installation). If everything works, you should see "hello" on the screen.
