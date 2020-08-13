---
jupytext:
  cell_metadata_filter: all
  notebook_metadata_filter: all,-language_info,-toc,-latex_envs
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.10'
    jupytext_version: 1.5.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
toc-autonumbering: true
toc-showcode: true
toc-showmarkdowntxt: true
---

# Markdown to canvas

+++

## Introduction

+++

### Shared presentation

* Part 1: Phil Austin (Associate professor, EOAS) -- set the scene
* Part 2: Mara Colclough (4th year honours computer science -- demo)

+++

## The big picture

### A brief history of the internet

* [Eben Moglen](https://en.wikipedia.org/wiki/Eben_Moglen): coined the term "low-friction collaboration"

* Jupyter/opensource/github: very low friction

* Canvas: Very high friction (by design and necessity)


### OCESE and top-down learning for open source computing

* [Open-source computing for earth science education](https://eoas-ubc.github.io/)

* [EOAS HPC tutorials](https://github.com/eoas-ubc/eoas_hpc_edu/blob/master/Readme.md)

## md2canvas

### Project goal

* collaborate on quizzes using jupyter/[jupytext](https://jupytext.readthedocs.io/en/latest/introduction.html) in a low friction environment

* deploy on canvas for testing and grading

### A typical quiz

* [An EOSC 340 quiz](midterm_sample/quiz2_2019t1.md)

* What I want

- single source of truth (one document provides questions/answers with explanations)

- quizzes stay on github (private repo if needed), canvas is read-only

```{code-cell} ipython3

```


# Part II

## Demonstration of md2canvas

### What is it?

[md2canvas](https://github.com/maracieco/md2canvas) is a command that can be used to convert your Jupyter Notebook quizzes (in markdown or notebook format) directly to Canvas quizzes, which can then be automatically pushed to your Canvas course. It also has the ability to strip the answers from your quiz so that it is distributable to students and the public.

The documentation is [here](https://maracieco.github.io/md2canvas/index.html).

md2canvas is currently under development with the main tasks being adding automatic testing using pytest and GitHub Actions (functional but limited), printing the quizzes without answers to paginated PDF using Sphinx (not started), and parameterizing the quizzes so that multiple versions can be generated.

We are currently looking for alpha testers! If you see this as being useful for your work in any way, please try it out and give us any feedback you have. We are open to suggestions and constructive criticism.

### The Basic Commands

1. Install the package:

    ```
    pip install git+https://github.com/maracieco/md2canvas
    ```

2. Send a quiz to your canvas course:

    ```
    md2canvas examples/demo_quiz/DemoQuiz.md -f path/to/token.txt -c 51824 -u https://canvas.ubc.ca -s
    ```

    -f provides the path to a file containing your authentication token
    
    -c provides the course ID

    -u provides the Canvas URL

    -s tells the program to save these three settings in a config file so they aren't required in the future

    Note: this command won't actually work, you will need to generate your own token and use your own course ID.

3. Strip the answers from your quiz so it can be distributed to students:

    ```
    anstrip examples/demo_quiz/DemoQuiz.md examples/demo_quiz/DemoQuizStripped.md
    ```

### Quiz Details

1. md2canvas uses the cells and their metadata to parse the questions with their answers and send them to Canvas

2. Here is a simple example question in its pure markdown form:

    ```
    +++ {"ctype": "question", "quesnum": 2, "question_type": "matching_question", "points_possible": 5}

    ### Question 2
    Match the same words to each other.

    Left

    * apple
    * bat
    * cat
    * dog

    Right

    * frog
    * cat
    * bat
    * exam
    * apple
    * dog

    +++ {"ctype": "answer", "quesnum": 2}

    Matchings

    * 5
    * 3
    * 2
    * 6

    +++ {"ctype": "answer", "quesnum": 2}

    The goal of this question is to find the matching words. For example, the first word in the left list (apple) appears in the fifth position in the right list. Because of this, the first value in the answer key is 5. Note also that there are some extra answers in the right list which act as distractors and do not have a pairing. In order for these questions to be parsed correctly, the length of the right list must be at least the length of the left list.
    ```

    And here is a screenshot of it in a Jupyter Notebook:

    ![Q1](media/Q1_jn.PNG)
    
    In general, there will be one question cell that contains all the info necessary to understand and solve the question. It will be followed by some answer cells. The first one will be parsed for answer data and must follow specific formatting. The following cells can be anything, so they can be used as descriptions of the answers or code cells for computation or anything really. All of these cells will be stripped by anstrip as long as they are tagged as answer cells in the metadata.

    When this question is part of a quiz that is pushed to Canvas, it looks like this for the student during the quiz:

    ![Q1](media/Q1_cu.PNG)

    And like this once the quiz has been graded:

    ![Q1](media/Q1_cg.PNG)


3. Here is another example that is a matching question, notice that it sets an extra field in the metadata (points_possible) that changes the number of points the question is worth:
    ```
    +++ {"ctype": "question", "quesnum": 2, "question_type": "matching_question", "points_possible": 5}

    ### Question 2
    Match the same words to each other.

    Left

    * apple
    * bat
    * cat
    * dog

    Right

    * frog
    * cat
    * bat
    * exam
    * apple
    * dog

    +++ {"ctype": "answer", "quesnum": 2}

    Matchings

    * 5
    * 3
    * 2
    * 6

    +++ {"ctype": "answer", "quesnum": 2}

    The goal of this question is to find the matching words. For example, the first word in the left list (apple) appears in the fifth position in the right list. Because of this, the first value in the answer key is 5. Note also that there are some extra answers in the right list which act as distractors and do not have a pairing. In order for these questions to be parsed correctly, the length of the right list must be at least the length of the left list.
    ```
    ![Q2](media/Q2_jn.PNG)
    ![Q2](media/Q2_cu.PNG)
    ![Q2](media/Q2_cu_options.PNG)
    ![Q2](media/Q2_cg.PNG)

4. This is a simpler type of question called a short answer question:
    ```
    +++ {"ctype": "question", "quesnum": 3, "question_type": "short_answer_question"}

    ### Question 3
    Type one of the words from the following image.

    ![text](media/captcha.png)

    +++ {"ctype": "answer", "quesnum": 3}

    Answers
    * overlooks
    * inquiry

    +++ {"ctype": "answer", "quesnum": 3}

    The image included in this question is automatically updloaded to Canvas when md2canvas is run. This means that if you can see it when you preview the markdown or Jupyter Notebook, you will see it on Canvas as well.

    +++ {"ctype": "question", "quesnum": 4, "question_type": "numerical_question"}
    ```
    ![Q3](media/Q3_jn.PNG)
    ![Q2](media/Q3_cu.PNG)
    ![Q2](media/Q3_cg.PNG)

5. Finally, this question shows off LaTeX:
    ~~~
    +++ {"ctype": "question", "quesnum": 4, "question_type": "numerical_question"}

    ### Question 4
    Evaluate the expression $$\frac{\pi r^2}{2}$$ where $r = 2$?

    Give your answer to three decimal places.

    +++ {"ctype": "answer", "quesnum": 4}

    * 6.283, 3: precision_answer

    +++ {"ctype": "answer", "quesnum": 4}

    Check this with python:

    ```{code-cell} ipython3
    :ctype: answer
    :quesnum: 4

    import math
    r = 2
    ans = math.pi * r ** 2 / 2
    print(f"{ans:.3f}")
    np.testing.assert_almost_equal(ans,6.383,decimals=3)
    ```
    ~~~
    ![Q4](media/Q4_jn.PNG)
    ![Q2](media/Q4_cu.PNG)
    ![Q2](media/Q4_cg.PNG)

    In the future, we envision that md2canvas will be able to compute the answers just based off the code cells.

6. Other question types also exist. There are examples of all of them in md2canvas/examples/sample_quiz/SampleQuiz.md.