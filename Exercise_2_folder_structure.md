# Ex. 2 - File System and Directories

We will use the introduction to the file system and directory structure provided by Software Carpentry. I recommend that you go through these exercises if you are not already familiar with folders and in Linux. The introduction demonstrates the tree-like structure used by UNIX systems, how to navigate them  using command line only and how to move, copy, and remove files and directories.  

In order to get the same directories and files used in the exercise available on your home on Saga you can do the following (copy paste the commands in ```the grey boxes```):
- Open your terminal and log on to Saga if you are not already logged on (see [Exercise 1](Exercise_1.md))   
  ```ssh username@saga.sigma2.no```
- Check were you are (it should read something like _/cluster/home/username_).  
  ```pwd```  
- Copy the zip-file with the data used in the exercise with this command (don't worry about the details for now, we will look at how to [download stuff later](Exercise_3_cmds.md)):   
  ```wget http://swcarpentry.github.io/shell-novice/data/data-shell.zip```
- unzip the data:   
  ```unzip data-shell.zip```  
- check that you now have some content in your $HOME:   
  ```ls```
- _Optionally:_ remove the zipfile (Careful, since there is no trash can on Saga the file will be lost forever)  
  ```rm data-shell.zip```

### Now you should do these Software Carpentry:
- [Navigating Files and Directories](http://swcarpentry.github.io/shell-novice/02-filedir/index.html) were you will learn
    - ```ls``` - list files and directories
    - ```cd``` - change directories
    - ```pwd``` - print working directory
    - ```/``` - root or path
    - ```.``` - current directory
    - ```..```  - parent directory  

(NB: Some of the solutions in the exercises assume that you are working on a personal computer with a slightly different set of folders than you will find in your home directory on Saga. In fact your home directory is empty until you download something to it. There is no ```Desktop```, ```Documents``` etc. Keep that in mind when you do the exercises.)

- [Working With Files and Directories](http://swcarpentry.github.io/shell-novice/03-create/index.html) were you will learn
    - ```cp``` - copy files and directories
    - ```mkdir``` - make directories
    - ```mv``` - move file and directories
    - ```rm``` - rm files and directories (Careful! There is no trashcan on saga. Removed items will be lost forever)
    - about wildcards

When you are done you can go to [Exercise 3](Exercise_3_cmds.md)

### For those who want to learn more (not part of curriculum)
This video explains some of the folders commonly found on linux computers for those who are particularly interested. [DorianDotSlash - Linux File System/Structure Explained!](https://youtu.be/HbgzrKJvDRw)
