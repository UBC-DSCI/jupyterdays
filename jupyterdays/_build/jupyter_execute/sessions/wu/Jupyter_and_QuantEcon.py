# Jupyter and QuantEcon

Peifan Wu (Postdoc @ Vancouver School of Economics, Intructor of ECON323)

## About QuantEcon

[QuantEcon](https://quantecon.org/) is a nonprofit organization dedicated to improving economic modeling by enhancing computational tools for economists. In particular, it provides three sets of lectures:
- QuantEcon with Python
    - Basic: Introductory
    - Advanced: Tools in (macro)economic Research
- QuantEcon with Julia
- **QuantEcon DataScience**

### QuantEcon DataScience

[QuantEcon DataScience](https://datascience.quantecon.org/) presents lectures on (Python) programming, data science, and economics.
- Consists of different parts
    - [Python Fundamentals](https://datascience.quantecon.org/python_fundamentals/): Basic operations, collections, control flow, functions, etc.
    - [Scientific Computing](https://datascience.quantecon.org/scientific/): Brief intro to Numpy and Scipy; Optimizations; Basic Applications in Economics
    - [Pandas](https://datascience.quantecon.org/pandas/): Playing around with Pandas DataFrames
    - [Applications](https://datascience.quantecon.org/applications/): Case studies. More advanced techniques in visualization; More statistical methods and machine learning in Economics
- Taught in various places
    - Utilize all the course contents: UBC, Huazhong University of Science and Technology
    - Partly used: 5+ schools around the world (NYU, PennState, Peking-HSBC Business School, NUS)
- Good Resource for Self-study
    - Lectures in the form of Jupyter notebooks [Github Repository](https://github.com/QuantEcon/quantecon-notebooks-datascience.git)
    - [Discourse forum](https://discourse.quantecon.org/) for Q&A

## Jupyter and QuantEcon DataScience Lectures

### Running the Lectures with Jupyter

We offer several options to run the lectures:
- [Local Installation](https://datascience.quantecon.org/introduction/local_install.html) (*not recommended*) running the notebooks offline and locally
- Running on the cloud, with NBGitPuller(https://github.com/jupyterhub/nbgitpuller) fetching the latest version of the notebooks
    - Google Colab
    - [ubc.syzygy.ca](https://ubc.syzygy.ca/)
    - [pims.syzygy.ca](https://pims.syzygy.ca/)
    - We can help setup Jupyter Hubs if people want to teach with this material
    
(Demo: Navigation Bar)

Advantages:
- A uniform environment saves teaching time from software installation
- In-class demonstrations can be easily shared and fully replicated by the students

### Writing/Updating Lectures

We write the lectures with `reStructuredText`(rst) file format. For webpage formatting, we include custom environments (`warning`, `exercise`, etc).

Then the [Jupinx](https://jupinx.quantecon.org/) tool converts `rst` files into a website via Jupyter Notebooks. The name of [Jupinx](https://jupinx.quantecon.org/) comes from Jupyter + Sphinx.
- [Jupinx](https://jupinx.quantecon.org/) generates several versions of notebooks: original vs executed, website vs local ones
- WYSIWYG
- The source files are synchronized from Github repositories, and compilations are on AWS clusters.

For web-based data, we cache the data we need on AWS bucket.
- Fetching data online depends on the stability of the API, and the Internet. Not ideal for teaching.
- Some data are relatively large and takes time for the Jupyter notebook to download.
- Easy and consistent to maintain.

## Teaching

### Instructor's Experience

- Code and execute in class, immediate feedback from the students
- Students vary in programming background. Skip the hardest steps...
- Explain in detail the meaning of the codes, and do variations
- Remote teaching through Canvas is slick!

### Students' Feedback
(Mean 4.5/5.0, IM 4.7/5.0 -- not bad!) The students love the comprehensive selection of the topics and the inter-discipline course material. The setting of this course is perfect for online teaching during COVID-19 as well.

Feedback and comments:
- *It touches too many topic without spending sufficient time on each of them*
    - We aim at an introductory course that covers a wide range of topics
    - We don't require previous knowledge on machine learning
- *Focus on the machine learning portion*
    - This course is more about economics
    - Maybe machine learning in data science programs?
- *This class would greatly benefit from a flipped class format*
    - Instead of going through the lectures one by one, we can put more course material for reading and give interactive coding sessions
    - More interactive options?
   
### Final Project Showcase
The students are supposed to work on a [final project](https://github.com/ubcecon/ECON323_2020/blob/master/final_project.md) at the end of the semester and we showcase their projects [here](https://datascience.quantecon.org/projects.html) with their permissions.
- Resume building, advertising, cross-reference...