# How to Build an Interactive Course
Using an open source framework created by SpaCy developer [Ines Montani](https://github.com/ines) 


<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Learning-Outcomes" data-toc-modified-id="Learning-Outcomes-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Learning Outcomes</a></span></li><li><span><a href="#Course-Examples" data-toc-modified-id="Course-Examples-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Course Examples</a></span></li><li><span><a href="#Course-Options" data-toc-modified-id="Course-Options-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Course Options</a></span></li><li><span><a href="#Setup" data-toc-modified-id="Setup-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Setup</a></span></li><li><span><a href="#Repository-Structure" data-toc-modified-id="Repository-Structure-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Repository Structure</a></span></li><li><span><a href="#Demo---How-to-make-it-work" data-toc-modified-id="Demo---How-to-make-it-work-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Demo - How to make it work</a></span></li><li><span><a href="#Sneak-Peak:-A-brief--look-at-what-I've-been-working-on:" data-toc-modified-id="Sneak-Peak:-A-brief--look-at-what-I've-been-working-on:-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Sneak Peak: A brief  look at what I've been working on:</a></span></li><li><span><a href="#Resources" data-toc-modified-id="Resources-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Resources</a></span></li><li><span><a href="#Thank-you!" data-toc-modified-id="Thank-you!-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>Thank you!</a></span></li></ul></div>

## Introduction

![](img/wave.png)

Hello! My name is Hayley Boyce. I work for the University of British Columbia's Master of Data Science program as an Educational Specialist. I did my undergraduate degree in Applied mathematics and I am an alumna of the Master of Data Science program. 

For the last 8 months I have been working with an open source platform where you can built your own online interactive course. This course was developed by SpaCy developer [Ines Montani](https://github.com/ines). 


## Learning Outcomes 

At the end of this seminar, you should be able to: 

1. Recognize courses that use this framework.
1. Use resources to begin to install and create your own course. 
1. Identify the different question style you can use to test students knowledge.
1. Recall key criteria needed to create lectures slides. 
1. Explain the structure needed for your course repository. 
5. See how it can be scaled to larger courses. 

## Course Examples 

- [Advanced NLP with SpaCy](https://course.spacy.io/en)
- [R Bootcamp](https://r-bootcamp.netlify.app/) - by Ted Laderas
- [Generalized Additive Models in R](https://noamross.github.io/gams-in-r-course/) - by Noam Ross
- [Supervised Machine Learning: Case Studies in R!](https://supervised-ml-course.netlify.app/) - by Julia Silge
- [Allen NLP Guide](https://guide.allennlp.org/your-first-model#7) (inspired by this framework) 
- And coming September 22, 2020 [Programing in Python for Data Science](https://mcl-dsci-011-programming-in-python.netlify.app/) by Tiffany Timbers, Mike Gelbart and Hayley Boyce

##  Course Options 

Currently this platform is available in 2 programming languages: 

- [Python](https://github.com/ines/course-starter-python)
- [R](https://github.com/ines/course-starter-r)

Of course this course can be used for other non programming subjects but the interactivity is limited to multiple choice questions only. 


## Setup

- Docker compose for Python 
- Python Course [Documentation](https://ines.github.io/course-starter-python/) 
- Installation of Node and Gatsby 


```{tip}
If you have any issues with Python setup, I recommend looking in the issue of the [course-starter-python repo](https://github.com/ines/course-starter-python/issues) or even referring to her [SpaCy course repo](https://github.com/ines/spacy-course). 
```


## Repository Structure 

```
course-starter-python
├── .gitignore          
├── .prettierrc          
├── LICENSE             
├── README.md            
├── docker-compose.yml  
├── dockerfile          
├── gatsby-browser.js    
├── gatsby-config.js    
├── gatsby-node.js      
├── main.js
├── meta.json         
├── package-lock.json
├── package.json
├── theme.sass          
│   │
├── binder   
|   └── requirements.txt     
│   │
├── chapter               
|   ├── module0.md
|   ├── module1.md
|   ├── ...
|   └── moduleN.md
│   │    
├── data                     
    └── exercise-data.csv
│   │
├── exercises            
|   ├── exercise_01.py
|   ├── solution_01.py
|   └── test_01.py
│   │
├── slides              
|   ├── module0_00.md
|   ├── ...
|   └── moduleN_nn.md
│   │
├── src                 
|   ├── markdown.js
|   ├── context.js
|   ├── components              
|   |   ├── button.js
|   |   ├── choice.js
|   |   ├── code.js
|   |   ├── exercise.js
|   |   ├── hint.js
|   |   ├── juniper.js
|   |   ├── layout.js
|   |   ├── link.js
|   |   ├── seo.js
|   |   ├── slides.js
|   |   └── typography.js
|   |   |   
|   ├── pages              
|   |   └── index.js
|   |   |
|   ├── styles               
|   |   ├── button.module.sass
|   |   ├── choice.module.sass
|   |   ├── code.module.sass
|   |   ├── exercise.module.sass
|   |   ├── hint.module.sass
|   |   ├── index.module.sass
|   |   ├── index.sass
|   |   ├── layout.module.sass
|   |   ├── link.module.sass
|   |   ├── reveal.css
|   |   ├── slides.module.sass
|   |   └── typography.module.sass
|   |   |
    └── templates              
        └── chapter.js
|   |   |
└── static               
    ├── icon.png
    ├── icon_check.svg
    ├── icon_slides.svg
    ├── logo.svg
    ├── profile.jpg
    └── social.jpg

```

We are going to concentrate on these ones:

- `chapters/`
- `slides/`
- `exercises/` 
- `binder/`
- `static/`

- Important things I don't have time to talk about but that are explained in the documentation: 
    - `meta.json`
    - `theme.sass`
    - `src/`

## Demo - How to make it work

- Making a chapter 
- Making slides 
- Making a multiple choice exercise question 
- Making a coding question (exc, solution, test) 

```{note}
It's important that before doing any of the content and question making, you build a binder and change the information in the `meta.json` file. This is explained in the setup documentation provided in the `README.md` of the `course-starter` repositories.
```

##  Sneak Peak: A brief  look at what I've been working on:

- Small customizations 
- Similar video style as Ines's SpaCy course
- A bit of a different repo structure
- Use `rmd` and a script to produce slides -> Much easier!

## Resources

- [Course Starter Python](https://github.com/ines/course-starter-python)
- [Course Starter R](https://github.com/ines/course-starter-r)
- Python Course [Documentation](https://ines.github.io/course-starter-python/) 
- Course coming soon - [Programing in Python for Data Science](https://mcl-dsci-011-programming-in-python.netlify.app/)
- Programing in Python for Data Science [GitHub repo](https://github.com/UBC-MDS/MCL-DSCI-011-programming-in-python)
- Me and my contact! 
    - [Website](www.hayleyfboyce.com)
    - [GitHub: hfboyce](https://github.com/hfboyce)
    - [Twitter: @hfboyce](https://twitter.com/hayleyfboyce)
    - [Email: hfboyce@cs.ubc.ca](mailto:hfboyce@cs.ubc.ca?subject=JupyterDays) 

## Thank you! 

![](img/thanks.png)