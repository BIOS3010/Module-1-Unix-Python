# Ex. 3 - Some important commands

In this exercise we will briefly look a handful of commonly used Linux commands. Here is a nice cheat sheet that sums up the usage of some of them: [Dave Child cheat sheet. ](https://cheatography.com/davechild/cheat-sheets/linux-command-line/)

In the following exercises will look at:   
```scp``` - Secure copying of files and directories  
```rsync``` - Synchronise and transfer files and directories  
```wget``` - non-interactive download of files from the Web  
```less``` - Print content of file to screen  
```more``` - Print content of file to   
```head``` - Print the head of file(s)  
```tail``` - Print the end (tail) of file(s)  
```wc```- word count  
```grep``` - Search through text files  
```sort``` - Sort the content of files  
```uniq``` - Print unique (lines, or words)  

### Copying and downloading files over networks

If you want to transfer files to saga with a graphic interface follow the instructions from the [lecture](/Lectures/BIOS3010_Week19_intro_to_unix.pdf) slides 44-47 (for windows users) or 48-49 (mac users).

On command line ```scp``` is used to copy files from one machine to a remote machine over a secure SSH connection.

The syntax of the scp command is similar to cp, but you can provide a host and username to direct the copying command to the correct host. ```scp``` is useful when you need to transfer files from saga to your computer (or from your computer to Saga). When downloading files from e.g. Saga it is easiest to do this when you are located on your computer, i.e. before logging on to the cluster. That is, open a new terminal window without logging on to the cluster, navigate to the folder on _your own computer_ where you will store the content. You can now use the short cut for "here" (the full stop ```.```) as you do with the ```cp```command. The biggest difference between ```cp``` and ```scp``` is that you will have to provide your username, the location of Saga, followed by a colon and the **the full path** to the file you want to download.

```scp username@saga.sigma2.no:/cluster/home/username/data-shell/notes.txt .```   

Wildcards can be used:

```scp username@saga.sigma2.no:/cluster/home/username/data-shell/* .```    
will download all **files** (not any folders) from the _data-shell_ folder on saga. If you want to download all files and folders nested inside _data-shell_ you can provide the ```-r``` option:

```scp -r username@saga.sigma2.no:/cluster/home/username/data-shell/* .```

This will download everything inside the _data-shell_ folder including subfolders and files (and their subfolders and files).  

For uploading you specify the file you want to upload first, then the path to saga:

```scp file_to_upload.txt username@saga.sigma2.no:/cluster/home/username/data-shell/```

```wget``` can be used to download files from the web, as you already saw when you downloaded the files used in the first exercise.

### Printing content of files

Finally you should do the exercises related to viewing content of files. [Pipes and Filters](http://swcarpentry.github.io/shell-novice/04-pipefilter/index.html)
