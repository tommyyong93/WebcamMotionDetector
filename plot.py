from WebcamMotionDetector.motiondetector import df

from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df['Start_string'] = df['Start'].dt.strftime("%Y-%m-%d %H:%M:%S")
df['End_string'] = df['End'].dt.strftime("%Y-%m-%d %H:%M:%S")
cds = ColumnDataSource(df)

hover = HoverTool(tooltips = [("Start","@Start_string"),("End","@End_string")])

p = figure( x_axis_type = 'datetime',height = 500, width = 2000, title = "Motion Graph")
p.add_tools(hover)
p.yaxis.minor_tick_line_color = None
p.title.text_font = 'times'
p.title.align = 'center'
p.title.text_font_size = '25pt'
p.ygrid[0].ticker.desired_num_ticks = 1

quadrant = p.quad(left = 'Start',right='End',bottom = 0, top = 1, color = 'green', source = cds)

output_file("Graph.html")
show(p)
