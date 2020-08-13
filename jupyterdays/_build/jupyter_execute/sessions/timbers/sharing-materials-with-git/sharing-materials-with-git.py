# Sharing your teaching materials using Git & GitHub

Now that you have learned how to access & use UBC's JupyterHub ([https://ubc.syzygy.ca/](https://ubc.syzygy.ca/)), this session will demonstrate how to share your teaching materials using Git & GitHub.

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

1. Use [GitHub.com](https://github.com/) to create a repository to host course materials, and use the web interface to edit and upload files.

2. Use UBC's JupyterHub (https://ubc.syzygy.ca/) to create & edit content, as well as send updates to [GitHub.com](https://github.com/).

3. Use [`nbgitpuller`](https://jupyterhub.github.io/nbgitpuller/index.html) to create a link to distribute and share course materials (e.g., data sets and Jupyter notebooks) with students on UBC's JupyterHub (https://ubc.syzygy.ca/).

## Walkthrough of a demo course on Canvas

Canvas is current course management system used by UBC. We can keep the student experience with other courses at UBC consistent by using Canvas as the pointer to our course materials that we host on [GitHub.com](https://github.com/) (a remote version control web archive). From the students perspective, nothing appears much different from their other courses and so there is no unnecessary cognitive load added for them to learn a new system.

Why use [GitHub.com](https://github.com/) for hosting materials? Well [GitHub.com](https://github.com/) is a remote version control web archive that allows you to view the history of your files, track who made changes to which files, use issue tracking to log and assign course/assignment bugs for fixing, or new features to add. Additionally, it is an authentic data science tool used in industry and academia.

Let's explore a demo Canvas course:
- [https://canvas.ubc.ca/courses/66517](https://canvas.ubc.ca/courses/66517)

Course source hosted on [GitHub.com](https://github.com/):
- [`jupyterdays`](https://github.com/UBC-DSCI/jupyterdays)

Some specific source files that might be of interest:
- [Syllabus](https://github.com/UBC-DSCI/jupyterdays/blob/master/jupyterdays/index.md)
- [these notes](https://github.com/UBC-DSCI/jupyterdays/tree/master/jupyterdays/sessions/ttimbers/sharing-materials-with-git/ttimbers/sharing-materials-with-git.ipynb)
- [Demo Jupyter (Python) Assignment](https://github.com/UBC-DSCI/jupyterdays/blob/master/homework/worksheet_01_python/worksheet_01_python.ipynb)

## Creating a course repository to host materials on [GitHub.com](https://github.com/)

A repository on [GitHub.com](https://github.com/) can used to host and share your course materials with your students (and fellow Instructors). 

### Sign up for a free account 

Before you can create repositories, you will need a [GitHub.com](https://github.com/) account. You can sign up for a free account here: [https://github.com/](https://github.com/)

### Create new repository to host your course materials

Login to [GitHub.com](https://github.com/) and click on the "+" icon in the upper right hand corner, and then click on "New Repository" as shown below:

```{figure} img/new_repository_01.png
---
width: 600px
name: new_repository_01
align: left
---
```

On the next page, do the following: 
- [ ] enter the name for the repository (here we put `dsci-101`) 
- [ ] Select "Public"
- [ ] Select "Initialize this repository with a README"
- [ ] click on the green "Create Repository" button

```{figure} img/new_repository_02.png
---
width: 600px
name: new_repository_02
align: left
---
```

Now you should have a repository that looks something like this:

```{figure} img/new_repository_03.png
---
width: 600px
name: new_repository_03
align: left
---
```

## Edit and add materials in your course repository on [GitHub.com](https://github.com/)

There are several ways you can directly use the [GitHub.com](https://github.com/) web interface; either using the pen tool to edit existing files, or the "Add file" drop down where you can choose to "Create new file" or "Upload files". 

### Use the pen tool to edit existing files

The pen tool can be used to edit existing plain text files. Click on the pen tool:

```{figure} img/pen-tool_01.png
---
width: 600px
name: pen-tool_01
align: left
---
```

Use the text box to make your changes:

```{figure} img/pen-tool_02.png
---
width: 600px
name: pen-tool_02
align: left
---
```

Save/commit your changes by click the green "Commit changes" button (adding a useful commit message is recommended).

```{figure} img/pen-tool_03.png
---
width: 600px
name: pen-tool_03
align: left
---
```

### Use the "Add file" drop down menu and "Create new file" to create new plain text files

New, plain text files can be created via the "Add file" drop down menu and selecting the "Create new file" option: 

```{figure} img/create-new-file_01.png
---
width: 600px
name: create-new-file_01
align: left
---
```

After click the "Create new file" option, a page will open with a small text box for the file name to be entered, and a larger text box where the desired file content text can be entered. Note the two tabs, "Edit new file" and "Preview". Togelling betweent them lets you enter and edit text and view what the text will look like when rendered, respectively.

```{figure} img/create-new-file_02.png
---
width: 600px
name: create-new-file_02
align: left
---
```

Save/commit your changes by click the green "Commit changes" button at the bottom of the page (adding a useful commit message is recommended).

```{figure} img/create-new-file_03.png
---
width: 600px
name: create-new-file_03
align: left
---
```

### Use the "Add file" drop down menu and "Upload files" to get files from my laptop to [GitHub.com](https://github.com/)

You can also upload files that you have created on your local machine by using the "Add file" drop down menu and selecting "Upload files":

```{figure} img/upload-files_01.png
---
width: 600px
name: upload-files_01
align: left
---
```

To select the files from your local computer to upload, you can either drag and drop them into the grey box area shown below, or click the "choose your files" link to access a file browser dialog. Once the files you want to upload have been selected, click the green "Commit changes" button at the bottom of the page (adding a useful commit message is recommended).

```{figure} img/upload-files_02.png
---
width: 600px
name: upload-files_02
align: left
---
```

## Using JupyterHub to create & edit content, as well as send updates to [GitHub.com](https://github.com/)

Although there are several ways to create and edit files on [GitHub.com](https://github.com/) they are not quite powerful enough for efficiently creating and editing complex files, or files that need to be executed to assess whether they work (e.g., files containing code). Thus, it is useful to be able to connect the course repository that was created on [GitHub.com](https://github.com/) to a coding environment. This can be done on your local computer, or using a JupyterHub. Given the focus of these Jupyterdays, we will here show how to do this using a JupyterHub.

### Cloning your [GitHub.com](https://github.com/) course repository to a JupyterHub

We will be using a Jupyter lab git extension tool to clone our [GitHub.com](https://github.com/) course repository to the UBC JupyterHub. There are other ways to do this (e.g., use the Git command line tools in the terminal on JupyterHub), however we think this is the most user friendly way to introduce this. 

On the file browser tab, click the Git+ icon:

```{figure} img/clone_01.png
---
width: 600px
name: clone_01
align: left
---
```

Paste the url of the [GitHub.com](https://github.com/) course repository you created and click the blue "CLONE" button:

```{figure} img/clone_02.png
---
width: 600px
name: clone_02
align: left
---
```

On the file browser tab, you will now see a folder for your course repository (and inside it will be all the files that existed on [GitHub.com](https://github.com/)):

```{figure} img/clone_03.png
---
width: 600px
name: clone_03
align: left
---
```

### Sending changes you make on JupyterHub back to [GitHub.com](https://github.com/)

Once you make changes (e.g., create or edit files) in your course repository on JupyterHub, you will need to send them back to the course repository on [GitHub.com](https://github.com/) to be able to share these with your students. We can use the Jupyter lab git extension tool to do this. It is a three stage process which includes: 

1. a `git add` command to flag which modified files you want to send back to the course repository on [GitHub.com](https://github.com/)
2. a `git commit` command that logs the changes and an associated (useful) message about what was changed
3. a `git push` command that sends the added and committed changes to the course repository on [GitHub.com](https://github.com/)

Below we walkthrough how you can use the Jupyter lab git extension tool to do each of the steps outlined above.

#### 1. `git add` the modified files

Below we created and saved a new file (named `demo-code.ipynb`) that we would like to send back to the course repository on [GitHub.com](https://github.com/). To `git add` this modified file, we click the Jupyter lab git extension icon on the far left-hand side of Jupyter lab:

```{figure} img/git_add_01.png
---
width: 600px
name: git_add_01
align: left
---
```

This opens the Git graphical user interface (GUI) pane, and then we click the plus sign beside the file that we want to `git add`. *Note, because this is the first change for this file that we want to add, it lives under the "Untracked" heading. However, next time we edit this file and want to add the changes we made, we will find it under the "Changed" heading.*

> Note: we can ignore the `demo-code-checkpoint.ipynb` file (sometimes called `.ipynb_checkpoints`), as it can be thought of as another type of "back-up" of our Jupyter notebook file we created, and we only need to send the file we directly created and edited to [GitHub.com](https://github.com/).

```{figure} img/git_add_02.png
---
width: 600px
name: git_add_02
align: left
---
```

This moves the file from the "Untracked" heading to the "Staged" heading and we are ready to now `git commit` the changes to log them and associate a (useful) message about what was changed.

```{figure} img/git_add_03.png
---
width: 600px
name: git_add_03
align: left
---
```

#### 2. `git commit` the changes and an associated (useful) message about what was changed

To `git commit` the changes and an associated (useful) message about what was changed, we put our message in the text box at the bottom of the Git GUI pane and click on the blue "Commit" button. *Note: It is highly recommended to make this message useful and relevant to the changes that were made, as this can later be used to peruse the file history and understand how the file evolved.*

```{figure} img/git_commit_01.png
---
width: 600px
name: git_commit_01
align: left
---
```

After commiting the file, you will see there there are 0 "Staged" files and we are now ready to push our changes (and the attached commit message) to our course repository on [GitHub.com](https://github.com/):

```{figure} img/git_commit_02.png
---
width: 600px
name: git_commit_02
align: left
---
```

#### 3. `git push` the changes to the course repository on [GitHub.com](https://github.com/)

To send our added and committed the changes to the course repository on [GitHub.com](https://github.com/), we need to `git push`. To do this we click on the cloud icon with the up arrow on the Git GUI pane:

```{figure} img/git_push_01.png
---
width: 600px
name: git_push_01
align: left
---
```

We will then be prompted to enter our [GitHub.com](https://github.com/) username and password, and click the blue "OK" button:

```{figure} img/git_push_02.png
---
width: 600px
name: git_push_02
align: left
---
```

If the files were successfully pushed to our course repository on [GitHub.com](https://github.com/) we will be given the success message shown below. *Note: click "Dismiss" to continue working in Jupyter.*

```{figure} img/git_push_03.png
---
width: 600px
name: git_push_03
align: left
---
```

If you now go to the course repository on [GitHub.com](https://github.com/) you will see the changes now exist there!

```{figure} img/git_push_04.png
---
width: 600px
name: git_push_04
align: left
---
```

### Pulling changes made in our course repository on [GitHub.com](https://github.com/) to JupyterHub

If you make changes in your course repository on [GitHub.com](https://github.com/) using one of the tools described earlier in this session (e.g., the pen tool, or file create/upload menus) then you will need to `git pull` those changes to the copy of the course repository on JupyterHub to get things in sync. You can do this using the Git GUI pane by clicking on the cloud icon with the down arrow:

```{figure} img/git_pull_01.png
---
width: 600px
name: git_pull_01
align: left
---
```

## Using [`nbgitpuller`](https://jupyterhub.github.io/nbgitpuller/index.html) to share course materials with students on JupyterHub

Finally, to share your materials with your students you can give them the URL to the [GitHub.com](https://github.com/) repository you created and they can browse the files there, you can create html versions of the files in the [GitHub.com](https://github.com/) and embed the content in Canvas using iframes (e.g., one way to do this is to create a Jupyter book, stay tuned to the next talk to learn how to do this), or you can use [`nbgitpuller`](https://jupyterhub.github.io/nbgitpuller/index.html) to create a special link that can be provided to the students. This special link automatically clones the [GitHub.com](https://github.com/) repository (including all files) to the students persistent storage on the JupyterHub specified in the link. Additionally, the link can be setup so that it opens up to a desired file in that repository on the JupyterHub when clicked.

The [`nbgitpuller` documentation](https://jupyterhub.github.io/nbgitpuller/index.html) has a very user friendly web interface, called the "nbgitpuller link generator" for crafting these special links: [https://jupyterhub.github.io/nbgitpuller/link.html](https://jupyterhub.github.io/nbgitpuller/link.html)

The nbgitpuller link generator looks like this:

```{figure} img/nbgitpuller_link_generator_01.png
---
width: 700px
name: nbgitpuller_link_generator_01
align: left
---
```

Here is a demonstration of how you would create a link to give to your students that would:
- clone the `dsci-101` course repository from [GitHub.com](https://github.com/) to the UBC JupyterHub
- uses the Jupyter lab (as opposed to Jupyter notebook) interface when the link is clicked
- opens Jupyter lab to the specified file, here `demo-code.ipynb`

```{figure} img/nbgitpuller_link_generator_02.png
---
width: 700px
name: nbgitpuller_link_generator_02
align: left
---
```

The link below is what is generated from the example above, and is the link you would share with your students: 

[`https://ubc.syzygy.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fttimbers%2Fdsci-101&urlpath=lab%2Ftree%2Fdsci-101%2Fdemo-code.ipynb&branch=master`](https://ubc.syzygy.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fttimbers%2Fdsci-101&urlpath=lab%2Ftree%2Fdsci-101%2Fdemo-code.ipynb&branch=master)

If you distribute the link on Canvas, your assignment instructions could look something like this:

```{figure} img/sample_assignment_01.png
---
width: 700px
name: sample_assignment_01
align: left
---
```

## Additional resources

- [GitHub's Introduction to GitHub free course](https://lab.github.com/githubtraining/introduction-to-github)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [`nbgitpuller` documentation](https://jupyterhub.github.io/nbgitpuller/index.html)