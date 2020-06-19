from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

drawing = svg2rlg("ileslh.svg")
renderPDF.drawToFile(drawing, "ileslh.pdf")
renderPM.drawToFile(drawing, "ileslh.png", fmt="PNG")

print(drawing.contents[0].contents[0].contents[0])
print(drawing.contents[0].contents[0].contents[1])
print(drawing.contents[0].contents[0].contents[2])
