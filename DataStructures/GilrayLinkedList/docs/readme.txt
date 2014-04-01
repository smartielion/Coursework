Linked List Curriculum

In this curriculum you will learn one way linked lists in Java along with object oriented techniques.

Author: James Van Boxtel

Version: 1.5

Setup:

To get started do the following.
Extract the zip to a folder. (if you havn't already)

Setup In Eclipse: (recommended)
	Start a new Java project.
        Remove the src folder if one is created for you
	Copy all the files in this distribution (the linked-list-* folder) into the project folder.
		If asked to overwrite, say yes
	File -> Refresh
	Project -> Properties
		Java Build Path -> Configure Build Path -> Libraries - Add linkedlist-<xxx>.jar and lib/jig.jar
		Java Build Path -> Configure Build Path -> Source - Add the src folder as a source folder.
	 		Enable output folders. Set the output folder of src to itself.
	 		By default eclipse puts compiled class files in the 'bin' directory.
			Instead we want them in the source folder because that is where the simulation looks.
	To run the project
		Expand 'Referenced Libraries'
		Right click linkedlist-<xxx>.jar -> Run as -> Java application
		This is equivalent to running the simulation jar file only through eclipse.
		In the future you can run simply by clicking the play button at the top.

	Eclipse Notes:
	If you ever change files outside of eclipse you will need to File -> Refresh
		Eclipse only watches for changes to the project from within eclipse.
		This tells eclipse that new files have been copied to the project
	If you get errors and everything seems to be setup right, you may need to clean the project.
		Project -> Clean
		This ensures everything is recompiled and up to date.


	To see the Documentation for the SinglyLinkedList interface, open up the stub code:
             StudentLinkedList.  Find the class declaration that looks like:
		public class StudentLinkedList implements SinglyLinkedList {
	     and double click to select SinglyLinkedList. Then right click and select 
             "Open Declaration"

Setup by Command Line:
	Develop your own solution to the problem by extending the classes.
	 An example is provided in the 'src/linkedlist/' folder.
	Ensure your solution has the package 'linkedlist'
	Compile your solution making sure to compile with the linkedlist jar
	  In windows this looks like
	  cd linkedlist-project\src
	  javac -classpath ..\lib\jig-<xxx>.jar;..\linkedlist-<xxx>.jar linkedlist/StudentLinkedList.java
	  Linux and Mac will be similar.
	Ensure their is .class file version of your solution in the 'src/linkedlist/' folder.
	Run the command 'java -jar linkedlist-<xxx>.jar'

Running The Simulation:

If all the methods are implemented correctly, running the game will allow you to move elements in
the linked lists. The object of the game is to get each column to have only one type
of shape, and for shapes to be in ascending order(numbers increase as you go down).

Click an object to select it and everything after it. Then click above the first element in a column
to insert at the top or click below the top element in a column to insert at the bottom. You may use
a power up once per level. Press space to use it. The powerup allows you to pull a single element out
of a linked list.

If any errors occur during runtime, they should be displayed at the bottom of the screen and to
standard error.
