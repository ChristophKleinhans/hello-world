#A Class of Methods, which return Lists with the demanded Tiemstamps in a time range of indidvidual
#sequence with tolerances, like it is defined in RFC3338 (https://tools.ietf.org/html/rfc3339)

import re
import pandas as pd


class Time_stamps:

	def __init__(self, start_date, start_time, end_date, end_time, period = 1800, tolerance = 1, tolerance_required = False, filesystem = 'CSV', filename = 'Timestamps_uncustomized', path = ''):
		self.start_date = start_date #yyyymmdd
		self.start_time = start_time #hhmmss
		self.end_date = end_date 
		self.end_time = end_time 
		self.period = period
		self.tolerance = tolerance
		#Default Arguments
		self.tolerance_required = tolerance_required
		self.filesystem = filesystem
		self.filename = filename
		self.path = path


	def _string_to_int(self):
		#Start Times
		self._start_year = int(self.start_date[0:4])
		self._start_month = int(self.start_date[4:6])
		self._start_day = int(self.start_date[6:8])
		self._start_hour = int(self.start_time[0:2])
		self._start_minute = int(self.start_time[2:4])
		self._start_second = int(self.start_time[4:6])

		#End Times
		self._end_year = int(self.end_date[0:4])
		self._end_month = int(self.end_date[4:6])
		self._end_day = int(self.end_date[6:8])
		self._end_hour = int(self.end_time[0:2])
		self._end_minute = int(self.end_time[2:4])
		self._end_second = int(self.end_time[4:6])
	



	def _stop_watch(self):
		self._string_to_int() #Convert the string characters to int
		_stoped_times = []
		_loop_count = 0
		_period_multi = 1
		_current_time = {'seconds': self._start_second,
						 'minute': self._start_minute,
						 'hour': self._start_hour,
						 'day': self._start_day,
						 'month': self._start_month,
						 'year': self._start_year}

		_end_time = 	{'seconds': self._end_second,
						 'minute': self._end_minute,
						 'hour': self._end_hour,
						 'day': self._end_day,
						 'month': self._end_month,
						 'year': self._end_year}
		
		#---------Stop Watch----------
		while True:	#Running the stop watch and save all required times into a list
			add = 1
			_loop_count += 1					

			if _current_time['seconds'] == 59 and _current_time['minute'] != 59:
				_current_time['seconds'] = 0
				_current_time['minute'] = _current_time['minute'] + add

			elif _current_time['seconds'] == 59 and _current_time['minute'] == 59 and _current_time['hour'] != 23:
				_current_time['seconds'] = 0
				_current_time['minute'] = 0
				_current_time['hour'] = _current_time['hour'] + add	

			elif _current_time['seconds'] == 59 and _current_time['minute'] == 59 and _current_time['hour'] == 23 and _current_time['month'] != 12: 
				_current_time['seconds'] = 0
				_current_time['minute'] = 0
				_current_time['hour'] = 0	
				_current_time['day'] = 	_current_time['day'] + add

				if _current_time['day'] - 1 == 31 and _current_time['month'] % 1 == 0 and _current_time['month'] != 2 and _current_time['month'] != 12:
					_current_time['day'] = 1
					_current_time['month'] = _current_time['month'] + add

				if _current_time['day'] - 1 == 30 and _current_time['month'] % 2 == 0 and _current_time['month'] != 2 and _current_time['month'] != 12:
					_current_time['day'] = 1
					_current_time['month'] = _current_time['month'] + add

				if _current_time['year'] % 4 == 0 and _current_time['month'] == 2 and _current_time['day'] - 1 == 29: #Leapyear
					_current_time['day'] = 1
					_current_time['month'] = _current_time['month'] + add

				if _current_time['year'] % 4 != 0 and _current_time['month'] == 2 and _current_time['day'] - 1 == 28: #no Leapyear
					_current_time['day'] = 1
					_current_time['month'] = _current_time['month'] + add

			elif  _current_time['seconds'] == 59 and _current_time['minute'] == 59 and _current_time['hour'] == 23 and  _current_time['day'] == 31: #New Year's Eve
				_current_time['seconds'] = 0
				_current_time['minute'] = 0
				_current_time['hour'] = 0	
				_current_time['day'] = 	0
				_current_time['month'] = 1
				_current_time['year'] = _current_time['year'] + add

			
			else:
				_current_time['seconds'] += add
			#---------Stop Watch End----------

			#---------Instructins for saving the timestamps while the watch is running------------
			if self.tolerance_required == False and _loop_count % self.period == 0: #If no tolerances are requiered
				_stoped_times.append([_current_time['year'], _current_time['month'], _current_time['day'], _current_time['hour'], _current_time['minute'], _current_time['seconds']])

			if self.tolerance_required == True: #If tolerances are requiered	
				if ((self.period * _period_multi) - self.tolerance/2 <= _loop_count <= (self.period * _period_multi) + self.tolerance/2):
					_stoped_times.append([_current_time['year'], _current_time['month'], _current_time['day'], _current_time['hour'], _current_time['minute'], _current_time['seconds']])					
					if _loop_count == (self.period * _period_multi) + self.tolerance/2:
						_period_multi += 1		


			if _current_time == _end_time: #Abort the loop
				break	
			
		return _stoped_times



	#-------------Writing the results---------------	
	filesystem_dict = {'CSV': 1, 'HDF5': 2}	

	def rfv(self): #The resulting RFV List saved in CSV or HDF5
		filesystem_dict = {'CSV': 1, 'HDF5': 2}	
		_rfv_basic_format = []
		_rfv_formatted = []
		
		if filesystem_dict[self.filesystem] == 1:
			_result = self._stop_watch()
			for times in _result: #Format it to RFV Norm			
				_rfv_basic_format.append(str(times[0])+'-'+str(times[1])+'-'+str(times[2])+'T'+str(times[3])+':'+str(times[4])+':'+str(times[5]))

			for init_string in _rfv_basic_format: #Add the missing 0's in the RFV format 
				initial_string = init_string
				init_string_splitted = re.split('-|T|:', initial_string)

				if len(init_string_splitted[1]) == 1: #update month
					initial_string = initial_string[:5] + '0' + initial_string[5:]

				if len(init_string_splitted[2]) == 1: #update day
					initial_string = initial_string[:8] + '0' + initial_string[8:]

				if len(init_string_splitted[3]) == 1: #update hour
					initial_string = initial_string[:11] + '0' + initial_string[11:]

				if len(init_string_splitted[4]) == 1: #update minute
					initial_string = initial_string[:14] + '0' + initial_string[14:]

				if len(init_string_splitted[5]) == 1: #update second
					initial_string = initial_string[:17] + '0' + initial_string[17:]	
				
				_rfv_formatted.append(initial_string)						

		
		if filesystem_dict[self.filesystem] == 1:
			RFV_result = pd.DataFrame(_rfv_formatted)	
			RFV_result.to_csv(self.path+self.filename+'.csv', index = False)
