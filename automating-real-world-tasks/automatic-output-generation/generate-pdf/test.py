from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.lib.units import inch
from reportlab.graphics.charts.piecharts import Pie

styles = getSampleStyleSheet() #default styles
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]

fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

#We need to create a two-dimensional array to hold the data for our table. Each row in the table will be a list of values, and each row will be appended to the table_data list.
table_data = []
for k, v in fruit.items():
    table_data.append([k, v])

#Create a Pie chart
report_pie = Pie(width=3*inch, height=3*inch)
#The Pie object isn’t Flowable, but it can be placed inside of a Flowable Drawing.
report_chart = Drawing()
report_chart.add(report_pie)
report_pie.data = []
report_pie.labels = []

# we need two separate lists: One for data, and one for labels.
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)


report = SimpleDocTemplate("./template/report.pdf")
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
#Put a spacer between the table and the chart
report.build([report_title, report_table, Spacer(1, 40), report_chart])