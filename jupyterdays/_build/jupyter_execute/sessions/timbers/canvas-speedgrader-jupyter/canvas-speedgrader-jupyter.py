# Intro to using Canvas Speedgrader with Jupyter

Now that you have learned how to create and share teaching materials using GitHub & JupyterHub ([https://ubc.syzygy.ca/](https://ubc.syzygy.ca/)), this session will demonstrate how you use Canvas and its speedgrader functionality to perform manual grading. This is probably the easiest and most straight-forward way to get started grading Jupyter assignments, but not the most efficient. Patrick Walls will talk about autograding Jupyter assignments using a tool called [`nbgrader`](https://nbgrader.readthedocs.io/en/stable/), which is more efficient but a little more complex to setup and use. 

## Introduction to me

Hi! I am [Tiffany Timbers](https://www.tiffanytimbers.com/), an Assistant Professor of Teaching in the [Department of Statistics](https://www.stat.ubc.ca/) at UBC. I am also a Co-Director for the [Master of Data Science Program (Vancouver Option)](https://ubc-mds.github.io/).

```{figure} img/ttimbers.png
---
height: 200px
name: im-tiff
align: left
---
```

## Learning outcomes

By the end of this session, participants will be able to:

1. Choose which files students should submit for grading a Jupyter assignment using Canvas and its speedgrader functionality.

2. Create a Canvas rubric for grading Jupyter assignments.

3. Use Canvas and its speedgrader functionality to manually grade Jupyter assignments.

## File submission type for Canvas speedgrader graded Jupyter assignments

Manually grading Jupyter assignments in Canvas using the speedgrader is pretty straightforward to set up, however there are a few small things to be aware of to make this run smoothly. First is the file type the students submit. When working on their assignments in Jupyter, the students will be working with an `.ipynb` file. These files are great that they are executable and can run Python or R code, for example. However, they only render nicely in Jupyter (and on GitHub too). Such files look like this in a plain text editor (and do not render at all on Canvas):


```
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Worksheet 1: Introduction to Data Science\n",
    "\n",
    "Welcome to DSCI 100: Introduction to Data Science!  \n",
    "\n",
    "Each week you will complete a lecture assignment like this one. For this worksheet, there are two parts:\n",
    "\n",
    "1. [Introduction to using Jupyter Notebooks](#1.-Introduction-to-Jupyter-Notebooks)\n",
    "2. [Introduction to analyzing data in R](#2.-Analyze-some-data)"
   ]
  },
 ...
 ```
 
 Thus, it is highly recommened to get the students to submit a more Canvas friendly file format for grading Jupyter assignments. Probably the lightest weight, and most true to render (i.e., in respect to what the `.ipynb` file looks like on Jupyter) filetype is an `.html` file. Happily, `.html` files are viewable in Canvas! `.pdf` also works, but in practice we find that sometimes errors in markdown or LaTeX can lead to annoying error in the rendering to `.pdf` process that are difficult to debug and demotivating for students. 
 
 > Note: I also always ask the students to submit the `.ipynb` file even though it cannot be rendered in Canvas, as it is the only way to test if their code actually runs. 

An `.html` render of the students `.ipynb` Jupyter assignment can be generated in Jupyter Lab via the File > Export Notebook As... > Export Notebook to HTML menu selection:

```{figure} img/download_html.png
---
width: 800px
name: download_html
align: left
---
```

The `.ipynb` Jupyter assignment can be downloaded from JupyterHub via right-clicking on the file and selecting "Download":

```{figure} img/download_ipynb.png
---
width: 800px
name: download_ipynb
align: left
---
```

> Note: this file conversion/rendering can also be done at the command line using the tool `nbconvert`, please see [the docs](https://nbconvert.readthedocs.io/en/latest/) to learn more.

It is very important to clearly communicate these filetype restrictions to students. This can be done using text in the assignment instructions on Canvas, as well as by restricting the filetype for file submission for the assignment. Screen shots of these are shown below:


```{figure} img/sample_assignment_01.png
---
width: 800px
name: sample_assignment_01
align: left
---
```


```{figure} img/sample_assignment_02.png
---
width: 600px
name: sample_assignment_02
align: left
---
```

## Creating Canvas rubrics for manual grading coding assignments

Grading can be made more transparent and efficient with the use of rubrics! When creating assignments in Canvas, there is an option to create a rubric. Below is an exampe Canvas rubric for our sample assignment:

```{figure} img/sample_assignment_03.png
---
width: 700px
name: sample_assignment_03
align: left
---
```

You can see that some of the criteria in the rubric are specific to questions - and would be used to assess whether an answer was "correct" or not. Some of the criteria are more general - to the document and code as a whole. Both types of criteria are useful to fairly and wholistically assess a data science assignment. For more examples of data science assignment rubric criteria, you can visit the UBC MDS public GitHub repository where we publicly share all of our rubrics: [https://github.com/UBC-MDS/public/tree/master/rubric](https://github.com/UBC-MDS/public/tree/master/rubric)

## Using the Canvas speedgrader and rubrics to grade Jupyter assignments

The Canvas speedgrader tool can be accessed from the assignment page:

```{figure} img/speedgrader.png
---
width: 800px
name: speedgrader
align: left
---
```

Once in the speedgrader tool, click on the "Rubric" button to view the rubric:

```{figure} img/speedgrader_rubric_01.png
---
width: 800px
name: speedgrader_rubric_01
align: left
---
```

Then the rubric and assignment can be viewed side by side and grades easily, efficiently and fairly entered:

```{figure} img/speedgrader_rubric_02.png
---
width: 800px
name: speedgrader_rubric_02
align: left
---
```