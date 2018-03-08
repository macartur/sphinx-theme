Kytos Sphinx Theme
##################


Kytos Sphinx theme is a sphinx theme build to be used into the kytos
documentations.


Installation
************

Installation from `PyPI` is fairly straightforward:

1. Install the package::

      $ pip install kytos_sphinx_theme

2. Edit the "conf.py" configuration file to point to the kytos theme::

      # At the top.
      import kytos_sphinx_theme

      # ...

      # Activate the theme.
      html_theme = 'kytos'
      html_theme_path = kytos_sphinx_theme.get_html_theme_path()

      html_sidebars = {'**': ['globaltoc_sidebar.html'] }
      html_show_sourcelink = False
