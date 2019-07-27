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
                        timestamps_list = [],
                        filesystem = 'CSV',
                        filename = 'Timestamps_uncustomized',
                        path = '')
```
In more Detail:

For the start_date use a string in the form YYYYMMDD and at which time the timestamps should be obtained is defined by start_time in the form HHMMSS, f.i.:
```python
start_date = '20190324', start_time = '080130' #Start at 8.30 o'clock and 30 seconds on March the 24th in the year 2019.
```
For the end_date and end_time also use a string which must be a date after the start_date. Please note, that we need to use 24-hour days, f.i.:
```python
end_date = '20190426', end_time = '235959' #End one second before midnight on April the 26th
```
