# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

pwd - print working directory
cd - change directory
ls - list contents in directory
mv - move file/directory
cp - copy file/directory
rm - remove directory
find - find file
grep - find something within a file
echo - print some arguments
chmod - change permission modifiers
sudo - become super user
env - look at environment
chown - change ownership
exit - exit the shell
man - manuals

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

ls - lists contents
ls -a list all contents, even hidden files/directories beginning with a .
ls -l list all contents in long format
ls -lh lists all contents in a long format with file sizes in byte, kilobyte, megabyte, gigabyte, etc.

---


---

What does `xargs` do? Give an example of how to use it.

xargs gets the execute arguments. This is useful when combined with other functions. For example, if you want to first find a file, and from those files get files that contain a certain string, you can combine find and grep with xargs.

find . -name '*.txt' | xargs grep 'Jason'

---

