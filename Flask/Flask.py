from flask import Flask, make_response, request, render_template


app = Flask(__name__)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/bild')
@app.route('/bild/<range>')
def bild(range=48):
    plot(range)
    return render_template('hello.html')


@app.route('/bild2')
def bild2():
    return render_template('hello.html')


@app.route('/')
def hello():
    return 'hello world'


@app.route("/simple.png")
def simple():
    import datetime as dt
    import StringIO
    import os
    import time

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    #Some configuration for the matplot
    fig = Figure(figsize=(12, 10))
    ax = fig.add_subplot(111)

    #Time initizilation
    To = int(time.time())
    From = To - 86400

    #Go to the sensors directory
    os.chdir('/home/pi/Projects/Home-automation/sensors')

    #Loop throuch all the sensors
    for i in os.listdir(os.getcwd()):
        #some inits
        dates = []
        values = []
        data_dict = {}
        #Change directory to the current sensor
        os.chdir(i)
        #Make a list of the files in the given time seconds back in time
        file_list = [l for l in os.listdir(os.getcwd()) if To+86400 > int(l) > From-86400]
        #Loop through those files
        for j in file_list:
            #Open the files
            with open(j, 'r') as f:
                #loop through the data
                for k in f:
                    #Split the time and data values
                    split_list = k.split('|')
                    #If the data is within the given time frame,
                    #add it to the dict, the first field is timethe second data
                    if To > int(split_list[0]) > From:
                        data_dict[split_list[0]] = split_list[1]

        #Loop through the created dict
        for key in sorted(data_dict.keys()):
            #Append the lists, List concetation???????????????
            dates.append(dt.datetime.fromtimestamp(int(key)))
            values.append(data_dict[key])
        #Some more configuration of the plot
        ax.plot_date(dates, values, '-', label='aaa')
        #Change the directory for next sensor
        os.chdir('..')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    #fig.legend(loc='upper left')
    canvas = FigureCanvas(fig)
    png_output = StringIO.StringIO()
    canvas.print_png(png_output)
    response = make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response


@app.route("/simple96.png")
def simple96():
    import datetime as dt
    import StringIO
    import os
    import time

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig = Figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    To = time.time()
    From = To - 345600
    os.chdir('/home/pi/Projects/Home-automation/sensors')
    for i in os.listdir(os.getcwd()):
        dates = []
        values = []
        data_dict = {}
        os.chdir(i)
        file_list = [l for l in os.listdir(os.getcwd()) if int(To)+345600  > int(l) > int(From)-345600]
        #print(file_list)
        for j in file_list:
            with open(j, 'r') as f:
                for k in f:
                    split_list = k.split('|')
                    if To > int(split_list[0]) > From:
                        data_dict[split_list[0]] = split_list[1]

        for key in sorted(data_dict.keys()):
            dates.append(dt.datetime.fromtimestamp(int(key)))
            values.append(data_dict[key])
        ax.plot_date(dates, values, '-', label='aaa')
        os.chdir('..')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    #fig.legend(loc='upper left')
    canvas = FigureCanvas(fig)
    png_output = StringIO.StringIO()
    canvas.print_png(png_output)
    response = make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response


@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


def Flaskrun():
    app.run(host='0.0.0.0')


def plot(plot_range=24):
    import datetime as dt
    import os
    import time

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    #plot range hours => seconds
    plot_range = plot_range * 3600

    #Some configuration for the matplot
    fig = Figure(figsize=(12, 10))
    ax = fig.add_subplot(111)

    #Time initizilation
    To = int(time.time())
    From = To - plot_range

    #Go to the sensors directory
    os.chdir('/home/pi/Projects/Home-automation/sensors')

    #Loop throuch all the sensors
    for i in os.listdir(os.getcwd()):

        #some inits
        dates = []
        values = []
        data_dict = {}
        #Change directory to the current sensor
        os.chdir(i)
        #Make a list of the files in the given time spectra (86400) seconds back in time
        file_list = [l for l in os.listdir(os.getcwd()) if To+plot_range > int(l) > From-plot_range]
        #Loop through those files
        for j in file_list:
            #Open the files
            with open(j, 'r') as f:
                #loop through the data
                for k in f:
                    #Split the time and data values
                    split_list = k.split('|')
                    #If the data is within the given time frame, add it to the dict, the first field is time, the second data
                    if To > int(split_list[0]) > From:
                        data_dict[split_list[0]] = split_list[1]

        #Loop through the created dict
        for key in sorted(data_dict.keys()):
            #Append the lists, List concetation???????????????
            dates.append(dt.datetime.fromtimestamp(int(key)))
            values.append(data_dict[key])
        #Some more configuration of the plot
        ax.plot_date(dates, values, '-', label='aaa')
        #Change the directory for next sensor
        os.chdir('..')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    #fig.legend(loc='upper left')
    canvas = FigureCanvas(fig)
    #png_output = StringIO.StringIO()
    canvas.print_png('/home/pi/Projects/Home-automation/Flask/static/bild.png')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    #app.run(host='0.0.0.0')
