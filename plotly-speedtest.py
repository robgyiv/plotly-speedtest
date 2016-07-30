#!/usr/bin/env python

import os
import subprocess
import datetime
import plotly.plotly as py
import plotly.graph_objs as go


def parse_results(speedtest_output, date_time):
    test_results = []
    for i in xrange(0, len(speedtest_output), 3):
        test_results.append({
            "statistic": speedtest_output[i].replace(":", ""),
            "value": speedtest_output[i + 1],
            "measurement": speedtest_output[i + 2],
            "date": date_time
            })
    update_chart(test_results, date_time)


def update_chart(test_results, date_time):
    username = os.environ['PLOTLY_USERNAME']
    api_key = os.environ['PLOTLY_API_KEY']
    py.sign_in(username, api_key)
    data = []

    for item in test_results:
        """Choose a different marker depending on the statistic.

        This is to make everything easier to see."""
        if item["statistic"] == "Upload":
            marker_style = "lines"
        elif item["statistic"] == "Download":
            marker_style = "lines+markers"
        elif item["statistic"] == "Ping":
            marker_style = "markers"

        # Format the statistic and measurement into a string
        marker_name = item["statistic"] + " (%s)" % item["measurement"]

        data.append(
            go.Scatter(
                x=date_time,
                y=item["value"],
                mode=marker_style,
                name=marker_name
                )
            )

    py.plot(
        data,
        filename="utils/broadband-speed",
        fileopt="extend",
        sharing="public"
    )


def main():
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    speedtest_cmd = "/usr/local/bin/speedtest-cli --simple"
    process = subprocess.Popen(speedtest_cmd.split(), stdout=subprocess.PIPE)
    process_output = process.communicate()[0]
    speedtest_output = process_output.split()
    parse_results(speedtest_output, date_time)


if __name__ == '__main__':
    main()
