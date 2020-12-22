In these exercises, you will be introduced to how to 

**Install gitbash**

**Working and navigating with directories/folders**
Your computer organizes files and directories (these are sometimes called "folders") in a file system. As you probably already know, files contain data and information, and directories contain files and/or other directories. On your computer, you are probably used to clicking on files and folders to navigate around in them. On the shell, however, all oparations has to be done using commands. Here, we will learn the basic (and important) commands allowing us to move around in the file system on our computer.

## 1.3.1 Printing our current position ("where we are) in the filesystem  ** 
Type in the following command in the terminal
```bash
pwd
```
This `pwd` (print working directory) command prints your current position in the file system. The output should be similar to: `[/your/home/]/BIOS3010`, where `[/your/home/]` is the position of your "home" or user directory. Note that the path will look different on different computers. On a windows machine, it might look something like this:  `C:\Users\myname\BIOS3010\`, and on a Mac it could look like this: `/Users/myname/BIOS3010`. Your

To understand what a ‘home directory’ is, let’s have a look at how the file system as a whole is organized. For the sake of this example, we’ll be illustrating the filesystem on our scientist Nelle’s computer. After this illustration, you’ll be learning commands to explore your own filesystem, which will be constructed in a similar way, but not be exactly identical.

On Nelle’s computer, the filesystem looks like this:
![](https://user-images.githubusercontent.com/5373069/102868272-47e64f80-443a-11eb-90fa-1ea4a6e84f21.png)

The file system is made up of a root directory that contains sub-directories
titled bin, data, users, and tmp

At the top is the root directory that holds everything else. We refer to it using a slash character, /, on its own; this is the leading slash in /Users/nelle.

Inside that directory are several other directories: bin (which is where some built-in programs are stored), data (for miscellaneous data files), Users (where users’ personal directories are located), tmp (for temporary files that don’t need to be stored long-term), and so on.

We know that our current working directory /Users/nelle is stored inside /Users because /Users is the first part of its name. Similarly, we know that /Users is stored inside the root directory / because its name begins with /.

```diff
!Notice that there are two meanings for the / character. 
When it appears at the front of a file or directory name, it refers to the root directory.
When it appears inside a path, it’s just a separator.
```

Underneath /Users, we find one directory for each user with an account on Nelle’s machine, her colleagues imhotep and larry.



![](https://user-images.githubusercontent.com/5373069/102868346-5df41000-443a-11eb-9212-1293ade3eecd.png)

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
Note: `..` (two dots) can be used like this in all UNIX commands where a path should be given

**6. `ls`**
Type in:
```bash
ls
```

```diff
! What does the `ls` command do?
```
Obs: Like the `pwd` command, this command command only prints to the screen.

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

**9. Removing directories with `rmdir`**
Do this:
```bash
mkdir abc
ls
rmdir abc
```

```diff
! Describe what happened in the three commands above
```

**10. Navigating in directory paths**
```bash
mkdir abc
mkdir abc/def
mkdir abc/def/ghi
```
Note: The slash symbol `/` is used to indicate the (relative) paths of the directories

```diff
! Describe what happened in the three commands above
! Navigate into the new direcories with `cd` and look at where you are with `pwd`
! Navigate back to the BIOS3010 folder (hint: use the commands you have learned above)
```

**11. Combining `..` and `/`**
```bash
cd abc/def/ghi/
cd ../../
```

```diff
! In which folder are you now placed?
! Navigate back to the BIOS3010 folder
```

**11. Moving directories and files with `mv`**
Do this:
```bash
mkdir xyz
mv xyz zzz
ls
```
Note: `mv` moves files and directories, and can therefore also be used to rename these by "moving" them to their new name

```diff
! Describe what happened in the three commands above
! Make two new directories (`aaa` and `bbb`)
! Move the `aaa` directory into the `bbb` directory
! Try to remove the `aaa` directory. What happens?
```

**11. Summarize what you have learned**
You have now learned about the following commands/concepts:
- cd 
- mkdir
- pwd
- ls
- rmdir
- mv 
- ..
- /
- ~

```diff
! Write down a short description of what each of these does
```

