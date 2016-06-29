# ADTs and Their Uses

If you've studied _abstract data types_ or __ADTs__ then you should be familiar with concepts and the abstract data structures such as _Stacks_, _Queues_, _Linked Lists_, and perhaps even _Binary Search Trees_ (BST)s. They may not seem useful when you first start learning them, but here are some examples of how these data structures are used in applications. I've picked up a few unusual ones along the way that you may not study in a first or second __data structures__ class, but they are interesting enough to be included here.

__Stacks__: Stacks are used quite often in operating system design as well as compiler design. Other uses include solving mazes, parsing text (ie. looking for balanced brackets or parenthese in math equations), travelling other data structures such as tress in a _depth-first_ manner. Due to their FILO (First In Last Out) nature, stacks are useful when trying to retrieve data in reverse order to how they were stored. Stacks are also used to implement Undo/Redo operations, where the stack keeps track of actions that a user takes, and then removes actions to "undo" the changes. Really, a stack has so many uses it's hard to name them all.

__Queues__:

__Priority Queues__:

__Linked Lists__:

__Binary Search Trees__:

## Other Useful Data Structures

__Gap Buffer__: If you have always wondered how text is stored in memory in a text editor, the answer is typically a _gap buffer_. A gap buffer can be implemented as a dynamic array. Text before the cursor or insertion point is stored at the front of the array, then there is a gap for inserting more characters, and text after the cursor is stored at the end of the array after the gap. The start and end positions of the gap is constantly changing as the cursor is moved around the text in the editor.[[1]]

## References

  [1]:<http://scienceblogs.com/goodmath/2009/02/18/gap-buffers-or-why-bother-with-1/> "Gap Buffers: Why bother with ropes?"

### Other Resources
* <a href="http://stackoverflow.com/questions/2058146/what-real-world-uses-of-the-stack-object-net-have-you-used">What real world uses of the stack object have you used?</a> - Stack Overflow
* <a href="https://msdn.microsoft.com/en-us/library/system.collections.queue(v=vs.110).aspx">Queue Class</a> - Microsoft MSDN entry
* <a href="http://www3.cs.stonybrook.edu/~algorith/video-lectures/">Skiena's Algorithm Lectures</a> - Huge resource of slides, video, and audio
* <a href="http://www.finseth.com/craft/">The Craft of Text Editing</a> - by Craig A. Finseth. An older work but explains gap buffers. In section 6 he compares different structures for storing text and explains why the gap buffer is the superior.
* <a href="http://scienceblogs.com/goodmath/2009/02/18/gap-buffers-or-why-bother-with-1/">Gap Buffers: Why bother with Ropes? - article explaining the implementation of gap buffers with code samples.
