# Timestamps RFV

timestampsrfv is a Python library which writes RFV normed timestamps in a .csv file. You can define in which range, period and with which tolerance the timestamps should be written.

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
