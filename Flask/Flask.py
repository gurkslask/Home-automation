from flask import Flask, make_response
app = Flask(__name__)

@app.route('/')
def hello():
	return 'hello world'
 
@app.route("/simple.png")
def simple():
	import datetime as dt
	import StringIO
	import random
	import os
	import time
 
	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	from matplotlib.figure import Figure
	from matplotlib.dates import DateFormatter
 
	fig=Figure(figsize=(12,10))
	ax=fig.add_subplot(111)
	To = time.time()
	From = To - 86400
	os.chdir('/home/pi/Projects/Home-automation/sensors')
	for i in os.listdir(os.getcwd()):
		dates=[]
		values=[]
		data_dict={}
		os.chdir(i)
		file_list=[l for l in os.listdir(os.getcwd()) if int(To)+86400  > int(l) > int(From)-86400]
		#print(file_list)
		for j in file_list:
			with open(j, 'r') as f:
				for k in f:
					split_list = k.split('|')
					if To > int(split_list[0]) > From:
						data_dict[split_list[0]]=split_list[1]

		for key in sorted(data_dict.keys()):
			dates.append(dt.datetime.fromtimestamp(int(key)))
			values.append(data_dict[key])
		ax.plot_date(dates, values, '-', label='aaa')
		os.chdir('..')
	ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
	fig.autofmt_xdate()
	#fig.legend(loc='upper left')
	canvas=FigureCanvas(fig)
	png_output = StringIO.StringIO()
	canvas.print_png(png_output)
	response=make_response(png_output.getvalue())
	response.headers['Content-Type'] = 'image/png'
	return response

def Flaskrun():
	app.run(host='0.0.0.0')


 
if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
