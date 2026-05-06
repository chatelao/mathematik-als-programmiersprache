# Configuration file for the Sphinx documentation builder.

project = 'Mathematik als ultimatives Werkzeug für Softwarespezifikationen'
copyright = '2024, Jules'
author = 'Jules'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
