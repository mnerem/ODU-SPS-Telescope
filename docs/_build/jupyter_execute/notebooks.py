#!/usr/bin/env python
# coding: utf-8

# # Jupyter Data Analysis
# 
# You can use Jupyter Notebooks to perform data analysis and create written content to communicate your work. This means that you can include code blocks and their outputs in your book.
# 
# The following is a sample of what can be done with Jupyter.
# This is a powerful tool that we can use to write up reports **and** analyze the data collected from our observations. This tool also allows for collaboration with anyone regardless of their location.
# 
# ## Markdown + notebooks
# 
# Jupyter notebooks can use Markdown (md) formatting for clear communications.
# 
# Markdown can process LaTeX to generate mathematical formulas
# ```{panels}
# Raw TeX string
# ^^^
#     $$
#         -\frac{\hbar^2}{2m}\vec{\nabla}\psi+ 
#         V(\vec{r}\,) \psi 
#         = i\hbar
#           \frac{\partial\,\psi}{\partial t}
#     $$
# ---
# Processed LaTeX
# ^^^
# $$
#     -\frac{\hbar^2}{2m}\vec{\nabla}\psi + V(\vec{r}\,) \psi = i\hbar\frac{\partial\,\psi}{\partial t}
# $$
# ```
# 
# ## Code blocks and outputs
# 
# Jupyter Book will also embed your code blocks and output in your book.
# For example, here's some sample Matplotlib code:

# In[1]:


from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np
plt.ion()


# In[2]:


# Fixing random state for reproducibility
np.random.seed(19680801)

N = 10
data = [np.logspace(0, 1, 100) + np.random.randn(100) + ii for ii in range(N)]
data = np.array(data).T
cmap = plt.cm.coolwarm
rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))


from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

fig, ax = plt.subplots(figsize=(10, 5))
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot']);


# There is a lot more that you can do with outputs (such as including interactive outputs)
# with your book. For more information about this, see [the Jupyter Book documentation](https://jupyterbook.org)
