"""
A page of the application.
Page content is imported from the slide_1.md file.

Please refer to https://docs.taipy.io/en/latest/manuals/gui/pages for more details.
"""

from taipy.gui import Html


data = {
  "Country": ["Rest of the world","Russian Federation","Peru"],
  "Area": [1445674.66,815312,72330.4]
}

slide_1 = Html("""
<h1>Page title</h1>

Any <a href="https://en.wikipedia.org/wiki/HTML"><i>HTML</i></a>
content can be used here.
<taipy:button>Button Label</taipy:button>
""")