# nmr-inte-great
Tkinter GUI that performs trapezoidal sum on Nuclear Magnetic Resonance peak list data (ASC) to get the area between a given range.
This is a personal project created to learn more about tkinter.

![](demo.gif)

## Purpose: 
This program parses the chemical shift and real intensity values 
of NMR data (.asc format) into two separate lists. 
It then calculates the integral on the desired interval based on the 
trapezoidal sum. 

Data Format and Parsing: Each line of data is formatted as the
following: "chemicalShift\trealValue\timaginaryValue\n".
I split each line of data into a list based on the \t separator.
Therefore, an individual instance of this line list may look like the following:
["12.31", "0.008", "-0.007\n"].
I have the program start making the chemical shift and peak list when
the first chemical shift within the specified bounds is encountered. For
example, the program begins to construct the alkenyl chemical shift and 
peak list when the chemical shift is 5.9 ppm and 
then it stops constructing this list when the chemical shift is less than 5.4 ppm. 
It then constructs the ferrocene chemical shift and peak list in the same way. 

Mathematics: After parsing the data and creating the appropriate lists
the trapezoidal sum formula is used.
Tn = Δx/2 [f(x0)+ 2f(x1) + 2f(x2) + ... + 2f(xn−1) +f(xn)].
Delta x is the average of delta x over all x values within the specified interval. 
I constructed a list of delta x's as follows:
[x0 - x1, x1 - x2, (xn - 1) - xn] then summed that list and took the average
to define delta x in the formula Tn.
The sum from 2f(x1) + 2f(x2) + ... + 2f(xn−1) is calculated independently and
then plugged into the trapezoidal sum formula.

## Considerations:
* How to organize toplevel widgets
   e.g. self.analysis_window in MainWindow
   and  self.plot_options_window in AnalysisWindow
   Possibly rename to toplevel1, toplevel2 etc.
* The organization for this is just not good at this point
   too many method calls to keep track of things. What would be a good way to organize this? Draw diagrams and see how information is shared
* May be worth splitting all classes into separate files for 
   readability purposes. Currently it's quite a lot of scrolling
   to navigate.... unsure on this one.
* Display whole plot might be useful.
   A scroll wheel for determining integration range would be
   nice.

## Documentation:
   **Tkinter:**
   * Canonical doc:
      - http://tcl.tk/man/tcl8.5/TkCmd/options.htm#M-wraplength

   * https://coderslegacy.com/python/python-gui/

   * https://www.python-course.eu/tkinter_dialogs.php

   * https://wiki.python.org/moin/TkInter

   **Matplotlib**
   * https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py


## Questions:
   ***On class structure***
   * https://stackoverflow.com/questions/19993795/how-would-i-access-variables-from-one-class-to-another

   ***Get temp matplotlib figure:***
   * https://stackoverflow.com/questions/57316491/how-to-convert-matplotlib-figure-to-pil-image-object-without-saving-image

   ***kwargs and class:***
   * https://stackoverflow.com/questions/8187082/how-can-you-set-class-attributes-from-variable-arguments-kwargs-in-python

   ***tkinter frames:***
   * https://stackoverflow.com/questions/9759496/aligning-widgets-using-grid-between-multiple-tkinter-labelframes


  ***git:***
   * https://stackoverflow.com/questions/5697750/what-exactly-does-the-u-do-git-push-u-origin-master-vs-git-push-origin-ma

   * https://stackoverflow.com/questions/52704/how-do-i-discard-unstaged-changes-in-git

   ***misc gui:***
   * Icon Image:
      - https://www.geeksforgeeks.org/iconphoto-method-in-tkinter-python/

   ***misc:***
   * Dir Path:
      - https://help.pythonanywhere.com/pages/NoSuchFileOrDirectory/

   * string slicing:
      - https://www.programiz.com/python-programming/methods/string/find

      - https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python
