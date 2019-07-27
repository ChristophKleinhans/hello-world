# Timestamps RFV

timestampsrfv is a Python library which writes RFV normed timestamps in a .csv or HDF5 file. You can define in which range, period and with which tolerance the timestamps should be written.

## Installation

(Use the package manager [pip](https://pip.pypa.io/en/stable/) to install timestampsrfv.)

```bash
pip install timestampsrfv
```

## Usage

```python
import timestampsrfv
```

The Time_stamps Class contains all the attributes for the creation of the the desired list.

```python
rfvstamps = Time_stamps(self,
                        start_date,
                        start_time,
                        end_date,
                        end_time,
                        period = 1800,
                        tolerance = 1,
                        tolerance_required = False,     
                        filesystem = 'CSV',
                        filename = 'Timestamps_uncustomized',
                        path = '')
```
In more Detail:

### start_date and start_time
For the start_date use a string in the form YYYYMMDD and at which time the timestamps should be obtained is defined by start_time in the form HHMMSS, f.i.:
```python
start_date = '20190324', start_time = '080130' #Start at 8.30 o'clock and 30 seconds on March the 24th in the year 2019.
```
### end_date and end_time
For the end_date and end_time also use a string which must be a date after the start_date. Please note, that we need to use 24-hour days, f.i.:
```python
end_date = '20190426', end_time = '235959' #End one second before midnight on April the 26th.
```
### period
Maybe you don't want all the timestamps between an end and start point. Maybe just all 50 seconds or 3600 seconds. Initally the period is 1800 seconds (a half hour). But if you it in an other periodically pattern, just define your custom period in seconds, f.i.

```Python 
period = 750 #A period of 12 minutes and 30 seconds to get a timestamp.
```
### tolerance
The initial tolerance of 1 means, that exactelly the value of the period gets written into the .csv file. Better make a example:
Let's say that the start_time is 8 o'clock and you want the timestamps in a period of 30 seconds.
```Python 
period = 750 #A period of 12 minutes and 30 seconds to get a timestamp.
```
