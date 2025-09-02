# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'A study of Ceph'
copyright = 'Dionysios Kalofonos'
author = 'Dionysios Kalofonos'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = []
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = []

html_theme_options = {
    'github_user': 'dionkalo',
    'github_repo': 'ceph',
    'github_button': False,
    'github_banner': True,
    'sidebar_width': '240pt',
    'page_width': '100%',
    'pre_bg': '#FFFFFF'
}

# # If false, no index is generated.
html_use_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
    ]
}
