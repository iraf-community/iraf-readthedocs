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
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}

html_theme = "bootstrap-astropy"
html_theme_options = {
    'logotext1': 'IRAF',
    'logotext2': 'IRAF',
    'logotext3': ':docs',
    'astropy_project_menubar': False
}
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'brand.css',
]
