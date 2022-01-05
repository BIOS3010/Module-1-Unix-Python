# Module 1: Learning the basics of Bash/UNIX (and repeating Python)
In the exercises below, all commands that should be run in the shell are shown:

```bash
Like this
```
In some places, there are tasks for you to do, or questions where you are meant to write down your answer. These are written
```diff
! Like this
```

In some places, there are things for you to simply note. These are written:
```diff
+ Note:
+ Like this
```

Follow each of the step in numerical order. If you have problems/errors along the way, contact a lecturer and refer to the step number where you are having issues.

## 1.1 Install and setup all required software on your computer
- We will need a Terminal application running Bash, nano and git installed on our computers for this course
- To install everything you need, follow the instructions here https://carpentries.github.io/workshop-template/#setup by chosing the tab corresponding to your system (Windows, Mac or Linix).
- As you will see from the instructions, if you have a Mac or a Linux machine you already have something called a “Terminal” installed.
- If you need to install the terminal (typically Windows users), make sure to test the terminal after it is installed.
- A short video introduction to using git bash (mainly for Windows users): https://www.youtube.com/watch?v=oQc-2gsjgDg&ab_channel=MarioKaack

For all Python exercises in the course, we will need:
- Python (obviously). [See installation instructions for your system here](https://carpentries.github.io/workshop-template/#python)
- A text editor: [Notepad++](https://notepad-plus-plus.org/downloads/) or [Atom](https://atom.io/) (or another text editor suitable for programming)
You may have Python installed on your system already

## 1.2 Setup today's exercises
Start your Bash shell (Terminal) and copy and paste the commands below into your terminal:
```bash
cd
mkdir BIOS3010
cd BIOS3010
git clone https://github.com/BIOS3010/Module-1-Unix-Python.git
```
For the moment, don't worry if you do not understand these commands. We are going to learn about these in the exercises today. These commands are there to make a new directory (`mkdir`) with the name BIOS3010 where all our exercises will be placed. We then move into that directory (`cd`) and then download the material needed for today's exercies (`git clone`). You will do a similar thing at the beginning of each exercises in each week of the course.

## 1.3 Learning how to navigate in your file system
* Go to [these exercises](exercises/Unix-1.md), and follow all the steps

## 1.4 Learning how to work with files and data
* Go to [these exercises](exercises/Unix-2.md), and follow all the steps

## 1.5 Repeating Python
Unless you already feel comfortable using Python, repeat what you learned e.g. in BIOS1100 by doing these exercises:
* Go to [these exercises](exercises/Python-exercise1.md). ([Solutions](solutions/Exercise1-solution.py))
* [More training](exercises/Python-exercise2.md) ([Solutions](solutions/Exercise2-solution.py))
