import os
import sys


project = 'IRAF'
release = '2.16.2'
version = release

master_doc = 'index'
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.extlinks',
    'sphinx_rtd_theme',
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'collapse_navigation': True,
}
html_static_path = ['_static']

html_css_files = [
    'brand.css',
]
#html_logo = '_static/iraflogo.png'
