"""
A page of the application.
Page content is imported from the slide_1.md file.

Please refer to https://docs.taipy.io/en/latest/manuals/gui/pages for more details.
"""

from taipy.gui import Markdown

data = {
  "Country": ["Rest of the world","Russian Federation","Peru"],
  "Area": [1445674.66,815312,72330.4]
}

slide_1 = Markdown("pages/slide_1/slide_1.md")
