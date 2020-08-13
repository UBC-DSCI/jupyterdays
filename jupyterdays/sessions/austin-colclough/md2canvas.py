# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info,-toc,-latex_envs
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.5.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   toc-autonumbering: true
#   toc-showcode: true
#   toc-showmarkdowntxt: true
# ---

# %% [markdown]
# # Markdown to canvas

# %% [markdown]
# ## Introduction

# %% [markdown]
# ### Shared presentation
#
# * Part 1: Phil Austin (Associate professor, EOAS) -- set the scene
# * Part 2: Mara Colclough (4th year honours computer science -- demo)

# %% [markdown]
# ## The big picture
#
# ### A brief history of the internet
#
# * [Eben Moglen](https://en.wikipedia.org/wiki/Eben_Moglen): coined the term "low-friction collaboration"
#
# * Jupyter/opensource/github: very low friction
#
# * Canvas: Very high friction (by design and necessity)
#
#
# ### OCESE and top-down learning for open source computing
#
# * [Open-source computing for earth science education](https://eoas-ubc.github.io/)
#
# * [EOAS HPC tutorials](https://github.com/eoas-ubc/eoas_hpc_edu/blob/master/Readme.md)
#
# ## md2canvas
#
# ### Project goal
#
# * collaborate on quizzes using jupyter/[jupytext](https://jupytext.readthedocs.io/en/latest/introduction.html) in a low friction environment
#
# * deploy on canvas for testing and grading
#
# ### A typical quiz
#
# * [An EOSC 340 quiz](midterm_sample/quiz2_2019t1.md)
#
# * What I want
#
# - single source of truth (one document provides questions/answers with explanations)
#
# - quizzes stay on github (private repo if needed), canvas is read-only

# %%
