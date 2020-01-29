# Generate the README from the Jupyter Notebook.
README.md: README.ipynb
	jupyter-nbconvert --to markdown --output=${@} ${<}


