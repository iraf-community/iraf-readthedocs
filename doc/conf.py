import os
import sys
import json

project = 'IRAF'
release = '2.17.1'
version = release
copyright = '1986 Association of Universities for Research in Astronomy Inc.'

master_doc = 'index'
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.extlinks',
    'sphinx_rtd_theme',
    'sphinx_reredirects',
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
html_logo = '_static/logo.svg'

with open('redirects.json') as fp:
    redirects = json.load(fp)
