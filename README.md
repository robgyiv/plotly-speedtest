# plotly-internet-speed
Simple Python script to be run on a Raspberry Pi to test internet speed and plot to a chart.

## Installation

You'll need a Plotly account and the following:

### Libraries
- plotly
- speedtest-cli

### Environment varibles
- `PLOTLY_USERNAME`
- `PLOTLY_API_KEY`


## Running

A basic example is to set up a cron job to run `python plotly-speedtest.py` at set intervals.
