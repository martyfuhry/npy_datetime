#include <Python.h>
#include <datetime.h>
#include <time.h>

// Frequency Defines
#define FR_Y  13  
#define FR_M  12
#define FR_W  11
#define FR_B  10
#define FR_D  9
#define FR_h  8
#define FR_m  7
#define FR_s  6
#define FR_ms 5
#define FR_us 4
#define FR_ns 3
#define FR_ps 2
#define FR_fs 1
#define FR_as 0

// For defaults and errors
#define FR_ERR  -1

// Offset for number of days between Jan 1, 1970 and Jan 1, 0001
#define DAYS_EPOCH 719163

// Calendar Structure for Parsing Long -> Date
typedef struct {
	int year, month, day;
} ymdstruct;

typedef struct {
	int hour, minute, second;
} hmsstruct;

typedef struct {
	int year, month, day, hour,
		minute, second, msecond,
		usecond, nsecond, psecond, fsecond,
		asecond;
} datestruct;

int freq_to_int(char* freq)
{
	// Absurdidly stupid way of doing this. Should be changed later.
	if (memcmp(freq, "Y", 1) == 0)
		return FR_Y;
	if (memcmp(freq, "M", 1) == 0)
		return FR_M;
	if (memcmp(freq, "W", 1) == 0)
		return FR_W;
	if (memcmp(freq, "B", 1) == 0)
		return FR_B;
	if (memcmp(freq, "D", 1) == 0)
		return FR_D;
	if (memcmp(freq, "h", 1) == 0)
		return FR_h;
	if (memcmp(freq, "m", 2) == 0)
		return FR_m;
	if (memcmp(freq, "s", 1) == 0) 
		return FR_s;
	if (memcmp(freq, "ms", 2) == 0)
		return FR_ms;
	if (memcmp(freq, "us", 2) == 0)
		return FR_us;
	if (memcmp(freq, "ns", 2) == 0)
		return FR_ns;
	if (memcmp(freq, "ps", 2) == 0)
		return FR_ps;
	if (memcmp(freq, "fs", 2) == 0)
		return FR_fs;
	if (memcmp(freq, "as", 2) == 0)
		return FR_as;

	return FR_ERR;
}

//=============
// callbacks
// ============

static PyObject *callback = NULL;

static PyObject *
test_callback()
{
	PyObject *result = NULL;
	PyObject *arglist = NULL;
	int a = 1, b = 2;
	arglist = Py_BuildValue("ii", a, b);
	if (callback == NULL)
	{
		PyErr_SetString(PyExc_TypeError, "callback not set.");
		return NULL;
	}
	result = PyEval_CallObject(callback, arglist);
	Py_DECREF(arglist);
	if (result == NULL)
		return NULL;
	// Use result HERE
	
	return result;
}

static PyObject *
set_callback(PyObject *dummy, PyObject *args)
{
	PyObject *result = NULL;
	PyObject *temp;

	if (PyArg_ParseTuple(args, "O:set_callback", &temp))
	{
		if (!PyCallable_Check(temp))
		{
			PyErr_SetString(PyExc_TypeError, "parameter must be callable");
			return NULL;
		}
		// Reference to new callback
		Py_XINCREF(temp);
		// Dispose of previous callback
		Py_XDECREF(callback);
		// Remember new callback
		callback = temp;
		// Boilerplate to return "None"
		Py_INCREF(Py_None);
		result = Py_None;
	}
	
	return result;
}


PyObject *DateCalc_RangeError = NULL;
PyObject *DateCalc_Error      = NULL;
/*
====================================================
== Beginning of section borrowed from mx.DateTime ==
====================================================
*/

/*
    Functions in the following section are borrowed from mx.DateTime version
    2.0.6, and hence this code is subject to the terms of the egenix public
    license version 1.0.0
*/

#define Py_AssertWithArg(x,errortype,errorstr,a1) {if (!(x)) {PyErr_Format(errortype,errorstr,a1);goto onError;}}
#define Py_Error(errortype,errorstr) {PyErr_SetString(errortype,errorstr);goto onError;}

/* Table with day offsets for each month (0-based, without and with leap) */
static int month_offset[2][13] = {
    { 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365 },
    { 0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366 }
};

/* Table of number of days in a month (0-based, without and with leap) */
static int days_in_month[2][12] = {
    { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 },
    { 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 }
};

/* Return 1/0 iff year points to a leap year in calendar. */
static
int is_leapyear(register long year)
{
    return (year % 4 == 0) && ((year % 100 != 0) || (year % 400 == 0));
}


/* Return the day of the week for the given absolute date. */
static
int day_of_week(register long absdate)
{
    int day_of_week;

	// Add in three for the Thursday on Jan 1, 1970 (epoch offset)
    if (absdate >= 0) 
        day_of_week = (absdate + 4) % 7;
    else 
        day_of_week = 6 - ((-absdate + 2) % 7);
    
    return day_of_week;
}

/* Return the year offset, that is the absolute date of the day
   31.12.(year-1) in the given calendar.
*/
static
long year_offset(register long year)
{
    year--;
    if (year >= 0 || -1/4 == -1)
        return year*365 + year/4 - year/100 + year/400;
    else
        return year*365 + (year-3)/4 - (year-99)/100 + (year-399)/400;
}    

static
int week_from_ady(long absdate, int day, int year)
{
    int week, dotw, day_of_year;
	dotw = day_of_week(absdate);
	day_of_year = (int)(absdate - year_offset(year) + DAYS_EPOCH);

    // Estimate
    week = (day_of_year - 1) - dotw + 3;
    if (week >= 0) 
		week = week / 7 + 1;

    // Verify 
    if (week < 0) 
	{
        // The day lies in last week of the previous year 
        if ((week > -2) || ((week == -2) && (is_leapyear(year-1))))
            week = 53;
        else
            week = 52;
    } 
	else if (week == 53) 
	{
    	// Check if the week belongs to year or year + 1 
        if ((31 - day + dotw) < 3) 
            week = 1;
    }

    return week;
}


// Modified version of mxDateTime function
// Returns absolute number of days since Jan 1, 1970
static
long long absdays_from_ymd(int year, int month, int day)
{

    /* Calculate the absolute date */
    int leap;
    long yearoffset, absdate;

    /* Range check */
    Py_AssertWithArg(year > -(INT_MAX / 366) && year < (INT_MAX / 366),
             DateCalc_RangeError,
             "year out of range: %i",
             year);

    /* Is it a leap year ? */
    leap = is_leapyear(year);

    /* Negative month values indicate months relative to the years end */
    if (month < 0) month += 13;
    Py_AssertWithArg(month >= 1 && month <= 12,
             DateCalc_RangeError,
             "month out of range (1-12): %i",
             month);

    /* Negative values indicate days relative to the months end */
    if (day < 0) day += days_in_month[leap][month - 1] + 1;
    Py_AssertWithArg(day >= 1 && day <= days_in_month[leap][month - 1],
                 DateCalc_RangeError,
                 "day out of range: %i",
				 day);

	// Number of days between (year - 1) and 1970
	// !! This is a bad implementation: if year_offset overflows a long, we lose a potential
	//     of DAYS_EPOCH days range
    yearoffset = year_offset(year) - DAYS_EPOCH;

    if (PyErr_Occurred()) goto onError;

	// Calculate the number of days using yearoffset
    absdate = day + month_offset[leap][month - 1] + yearoffset;

	return absdate;

onError:
	// do bad stuff
	return 0;

}

// Returns absolute seconds from an hour, minute, and second
long long abssecs_from_hms(int hour, int minute, int second)
{
	// Needs to perform checks for valid times
	return hour * 3600 + minute * 60 + second;
}
static
ymdstruct long_to_ymdstruct(long long dlong)
{
	ymdstruct ymd;
    register long year;
   	long long yearoffset;
    int leap, dayoffset;
	int month = 1, day = 1;
    int *monthoffset;
	dlong += DAYS_EPOCH;

    /* Approximate year */
     year = 1970 + dlong / 365.25;
    
	if (dlong > 0) year++;

    /* Apply corrections to reach the correct year */
    while (1) {
        /* Calculate the year offset */
        yearoffset = year_offset(year);

        /* Backward correction: absdate must be greater than the
           yearoffset */
        if (yearoffset >= dlong) {
            year--;
            continue;
        }

        dayoffset = dlong - yearoffset;
        leap = is_leapyear(year);

        /* Forward correction: non leap years only have 365 days */
        if (dayoffset > 365 && !leap) {
            year++;
            continue;
        }
        break;
    }

    /* Now iterate to find the month */
    monthoffset = month_offset[leap];
    {
        for (month = 1; month < 13; month++) {
            if (monthoffset[month] >= dayoffset)
            	break;
        }
        day = dayoffset - month_offset[leap][month-1];
    }
	
	ymd.year  = year;
	ymd.month = month;
	ymd.day   = day;

	return ymd;
}

/* Sets the time part of the DateTime object. */
static
hmsstruct long_to_hmsstruct(long long dlong)
{
    int hour, minute, second;
	hmsstruct hms;

	// Make dlong within a one day period
	dlong = dlong % 86400;

	if (dlong < 0)
		dlong = 86400 + dlong;
    hour   = dlong / 3600;
    minute = (dlong % 3600) / 60;
    second = dlong - (hour*3600 + minute*60);

   	hms.hour   = hour;
   	hms.minute = minute;
   	hms.second = second;

	return hms;
}


/*
====================================================
== End of section borrowed from mx.DateTime       ==
====================================================
*/

//==================================================
// Parsing datetime/datestring to long
// =================================================

// Takes a datetime object and a string as frequency
// Returns the number of (frequency) since Jan 1, 1970
long long datetime_to_long(PyObject* datetime, int frequency)
{
	int year = 0, month = 0, day = 0, hour = 0, 
		minute = 0, second = 0, microsecond = 0;
	
	// Get the time units from PyDateTime
	year        = PyDateTime_GET_YEAR(datetime);
	month       = PyDateTime_GET_MONTH(datetime);
	day         = PyDateTime_GET_DAY(datetime);
	hour        = PyDateTime_DATE_GET_HOUR(datetime);
	minute      = PyDateTime_DATE_GET_MINUTE(datetime);
	second      = PyDateTime_DATE_GET_SECOND(datetime);
	microsecond = PyDateTime_DATE_GET_MICROSECOND(datetime);
	
	// The return value
	long long result = 0;

	// The absolute number of days since 1970
	long long absdays = absdays_from_ymd(year, month, day);

	// 1 for leap, 0 for no leap

	// These calculations depend on the frequency

	if (frequency == FR_Y) {
		result = year - 1970;
	} else if (frequency == FR_M) {
		result = (year - 1970) * 12 + month - 1;
	} else if (frequency == FR_W) {
		// 4 day offset for post 1970 to get correct week
		int dotw = day_of_week(absdays);
		if (absdays >= 0)
			result = (absdays + 4) / 7;
		else
			result = (absdays - dotw)/ 7;
	} else if (frequency == FR_B) {
		int dotw = day_of_week(absdays);
		// Post epoch
		if (year >= 1970) {
			// To get to Sunday, Jan 4, 1970
			// number of weeks * 5 + dotw [0-6] - Saturdays + 1 for offset
			if (absdays > 2)
				result = ((absdays - dotw) / 7) * 5 + dotw - (dotw / 6) + 1;
			else 
				result = dotw - 4 - (dotw / 6);
		// Pre epoch
		} else {
			// To get beyond Sunday, Dec 28, 1969
			if (absdays < -4) {
				// Offset by 1 for Sundays
				if (dotw)
					result = ((absdays + 7 - dotw) / 7) * 5 - (6 - dotw) - 3;
				else
					result = ((absdays + 7 - dotw) / 7) * 5 - (6 - dotw) - 2;
			} else {
				// Offset by 1 for Sundays
				if (dotw)
					result = -4 + dotw;
				else
					result = -3; // Sunday, Dec 28, 1969
			}
		}
	} else if (frequency == FR_D) {
		result = absdays;
	} else if (frequency == FR_h) {
		result = absdays * 24 + hour;
	} else if (frequency == FR_m) {
		result = absdays * 1440 + hour * 60 + minute;
	} else if (frequency == FR_s) {
		result = absdays * 86400LL + abssecs_from_hms(hour, minute, second);
	} else if (frequency == FR_ms) {
		result = absdays * 86400000LL + abssecs_from_hms(hour, minute, second) * 1000LL
			 	+ (microsecond / 1000LL);
	} else if (frequency == FR_us) {
		result = absdays * 86400000000LL + abssecs_from_hms(hour, minute, second) * 1000000LL
			 	+ microsecond;
	}
	// Starting from here, we need extra units (ns, ps, fs, as)
	//  for correct precision: datetime doesn't include beyond microsecond
	else if (frequency == FR_ns) {
		PyErr_SetString(PyExc_NotImplementedError, "not implemented yet");
		result = 0;
	} else if (frequency == FR_ps) {
		PyErr_SetString(PyExc_NotImplementedError, "not implemented yet");
		result = 0;
	} else if (frequency == FR_fs) {
		PyErr_SetString(PyExc_NotImplementedError, "not implemented yet");
		result = 0;
	} else if (frequency == FR_as) {
		PyErr_SetString(PyExc_NotImplementedError, "not implemented yet");
		result = 0;
	} else {
		// Throw some Not Valid Frequency error here
		result = -1;
	}	

	return result;
}

// Takes a string object as the date, and a string as frequency, 
//  parses that into a datetime and passes the datetime object 
//  to datetime_to_long
// Returns the number of (frequency) since Jan 1, 1970
long long datestring_to_long(PyObject *string, int frequency)
{
	// Send to datetime_to_long
	PyObject *datetime = NULL;
	long long result = 0;

	// Make the string into a tuple for the callback function
	PyObject *string_arg = PyTuple_New(1);
	PyTuple_SET_ITEM(string_arg, 0, string);
	Py_INCREF(string);

	// Parse the string into a datetime object
	datetime = PyEval_CallObject(callback, string_arg);

	Py_DECREF(string_arg);

	// If the parsing worked, send the datetime and frequency 
	//  to datetime_to_long
	if (datetime)
	{
		result = datetime_to_long(datetime, frequency);
	}
	else
	{
		PyErr_SetString(PyExc_TypeError, "error processing datetime");
		//return NULL;
		//Return bad stuff
		result = -1;
	}

	return result;
}

// This is the callable wrapper for datestring/datetime_to_long
// Decides if the arguments are a string or a datetime object
//  and passes them to the correct datestring/datetime function
// Returns a PyLong generated from the appropriate function
PyObject *
date_to_long(PyObject *self, PyObject *args)
{
	PyObject *date_arg = NULL;    // string or datetime
	PyObject *freq_arg = NULL;	  // frequency as string
	PyObject *result   = NULL;	  // long result

	int freq = FR_ERR;			  // freq_arg is a PyObject to be parsed to freq

	// macro PyDateTime_IMPORT must be invoked for PyDateTime_Check
	PyDateTime_IMPORT;

	// Make sure the callback function is set
	//  ! This doesn't check to make sure it's the right callback function
	//  ! This should all be done in some init script
	if (!PyCallable_Check(callback))
	{
		PyErr_SetString(PyExc_TypeError, "callback not set.");
		return NULL;
	}

	// Parse out date_arg & freq_arg
	if (!PyArg_ParseTuple(args, "OO", &date_arg, &freq_arg))
	{
		return NULL;
	}

	// Make sure frequency is not NULL
	if (!freq_arg)
	{	
		PyErr_SetString(PyExc_TypeError, "frequency not set.");
		return NULL;
	}

	// Parse out frequency into an int so we can use it easily
	if ((freq = freq_to_int(PyString_AsString(freq_arg))) == FR_ERR)
	{
		// If the frequency is invalid, set an error and return null
		PyErr_SetString(PyExc_TypeError, "invalid frequency.");
		return NULL;
	}

	// Make sure date_arg is not NULL
	if (!date_arg)
	{
		PyErr_SetString(PyExc_TypeError, "no date provided.");
		return NULL;
	}

	// Decide if the date_arg is a string or a datetime
	if (PyString_Check(date_arg))
	{
		// XXX PyINCREF here?
		// date_arg is a string, so return datestring_to_long
		result = PyLong_FromLongLong(datestring_to_long(date_arg, freq));
	}
	else if (PyDateTime_Check(date_arg))
	{
		// XXX PyINCREF here?
		// date_arg is a datetime, so return datetime_to_long
		result = PyLong_FromLongLong(datetime_to_long(date_arg, freq));
	}
	else
	{
		// date_arg is neither a string, nor a datetime
		PyErr_SetString(PyExc_TypeError, "invalid date type");
		return NULL;
	}

	if (PyErr_Occurred())
		return NULL;

	return result;
}
//==================================================
// Parsing long to datetime/datestring
// =================================================

// Takes a long long value and a frequency
// Returns a datestruct formatted with the correct calendar values
datestruct long_to_datestruct(long long dlong, int frequency)
{
	int year = 1970, month = 1, day = 1, 
		hour = 0, minute = 0, second = 0,
		msecond = 0, usecond = 0, nsecond = 0,
		psecond = 0, fsecond = 0, asecond = 0;

	datestruct result;

	if (frequency == FR_Y) {
		year = 1970 + dlong;
	} else if (frequency == FR_M) {
		if (dlong >= 0) {
			year  = 1970 + dlong / 12;
		   	month = dlong % 12 + 1;
		} else {
			year  = 1969 + (dlong + 1) / 12;
			month = 12 + (dlong + 1)% 12;
		}
	} else if (frequency == FR_W) {
		ymdstruct ymd;
		ymd = long_to_ymdstruct((dlong * 7) - 4);
		year  = ymd.year;
		month = ymd.month;
		day   = ymd.day;
	} else if (frequency == FR_B) {
		ymdstruct ymd;
		long long absdays;
		if (dlong >= 0) {
			// Special Case
			if (dlong < 3)
				absdays = dlong + (dlong / 2) * 2;
			else
				absdays = 7 * ((dlong + 3) / 5) + ((dlong + 3) % 5) - 3;
		} else {
			// Special Case
			if (dlong > -7)
				absdays = dlong + (dlong / 4) * 2;
			else
				absdays = 7 * ((dlong - 1) / 5) + ((dlong - 1) % 5) + 1;
		}
		ymd = long_to_ymdstruct(absdays);
		year  = ymd.year;
		month = ymd.month;
		day   = ymd.day;
	} else if (frequency == FR_D) {
		ymdstruct ymd = long_to_ymdstruct(dlong);
		year  = ymd.year;
	    month = ymd.month;
		day   = ymd.day;	
	} else if (frequency == FR_h) {
		ymdstruct ymd;	
		if (dlong >= 0) {
			ymd  = long_to_ymdstruct(dlong / 24);
			hour  = dlong % 24;
		} else {
			ymd  = long_to_ymdstruct((dlong - 23) / 24);
			hour = 24 + (dlong + 1) % 24 - 1;
		}
		year  = ymd.year;
		month = ymd.month;
		day   = ymd.day;
	} else if (frequency == FR_m) {
		ymdstruct ymd;
		hmsstruct hms;
		if (dlong >= 0) {
			ymd = long_to_ymdstruct(dlong / 1440);
		} else {
			ymd = long_to_ymdstruct((dlong - 1439) / 1440);
		}
		hms = long_to_hmsstruct(dlong * 60);
		year   = ymd.year;
		month  = ymd.month;
		day    = ymd.day;
		hour   = hms.hour;
		minute = hms.minute;
	} else if (frequency == FR_s) {
		ymdstruct ymd;
		hmsstruct hms;
		if (dlong >= 0) {
			ymd = long_to_ymdstruct(dlong / 86400);
		} else {
			ymd = long_to_ymdstruct((dlong - 86399) / 86400);
		}
		hms = long_to_hmsstruct(dlong);
		year   = ymd.year;
		month  = ymd.month;
		day    = ymd.day;
		hour   = hms.hour;
		minute = hms.minute;
		second = hms.second;
	} else if (frequency == FR_ms) {
		ymdstruct ymd;
		hmsstruct hms;
		if (dlong >= 0) {
			ymd = long_to_ymdstruct(dlong / 86400000LL);
			hms = long_to_hmsstruct(dlong / 1000);
			msecond = dlong % 1000;
		} else {
			ymd = long_to_ymdstruct((dlong - 86399999LL) / 86400000LL);
			hms = long_to_hmsstruct((dlong - 999LL) / 1000);
			msecond = (1000 + dlong % 1000) % 1000;
		}
		year    = ymd.year;
		month   = ymd.month;
		day     = ymd.day;
		hour    = hms.hour;
		minute  = hms.minute;
		second  = hms.second;
		usecond = msecond * 1000;
	} else if (frequency == FR_us) {
		ymdstruct ymd;
		hmsstruct hms;
		if (dlong >= 0) {
			ymd = long_to_ymdstruct(dlong / 86400000000LL);
			hms = long_to_hmsstruct(dlong / 1000000LL);
			msecond = (dlong / 1000) % 1000;
			usecond = msecond * 1000LL + dlong % 1000LL;
		} else {
			ymd = long_to_ymdstruct((dlong - 86399999999LL) / 86400000000LL);
			hms = long_to_hmsstruct((dlong - 999999LL) / 1000000LL);
			msecond = (1000 + (dlong / 1000) % 1000) % 1000;
			usecond = (1000000LL + (dlong % 1000000)) % 1000000;
		}
		year    = ymd.year;
		month   = ymd.month;
		day     = ymd.day;
		hour    = hms.hour;
		minute  = hms.minute;
		second  = hms.second;
	}
	// Starting from here, we need extra units (ns, ps, fs, as)
	//  for correct precision: datetime doesn't include beyond microsecond
	else if (frequency == FR_ns) {
		PyErr_SetString(PyExc_NotImplementedError, "not implemented yet");
	} else if (frequency == FR_ps) {
		PyErr_SetString(PyExc_NotImplementedError, "not implemented yet");
	} else if (frequency == FR_fs) {
		PyErr_SetString(PyExc_NotImplementedError, "not implemented yet");
	} else if (frequency == FR_as) {
		PyErr_SetString(PyExc_NotImplementedError, "not implemented yet");
	} else {
		// Throw some Not Valid Frequency error here
	}
	
	result.year    = year;
	result.month   = month;
	result.day     = day;
	result.hour    = hour;
	result.minute  = minute;
	result.second  = second;
	result.msecond = msecond;
	result.usecond = usecond;
	result.nsecond = nsecond;
	result.psecond = psecond;
	result.fsecond = fsecond;
	result.asecond = asecond;

	return result;
}

// Takes a long and a frequency
// Returns a Python DateTime Object
PyObject *
long_to_datetime(PyObject *self, PyObject *args)
{
	PyObject *long_arg = NULL;    // string or datetime
	PyObject *freq_arg = NULL;	  // frequency as string
	PyObject *result   = NULL;	  // long result

	long long dlong = 0;          // Stores the long_arg
	int freq = FR_ERR;			  // freq_arg is a PyObject to be parsed to freq
	datestruct dstruct;		      // To store date values

	// macro PyDateTime_IMPORT must be invoked for PyDateTime_Check
	PyDateTime_IMPORT;

	// Make sure the callback function is set
	//  ! This doesn't check to make sure it's the right callback function
	//  ! This should all be done in some init script
	if (!PyCallable_Check(callback))
	{
		PyErr_SetString(PyExc_TypeError, "callback not set.");
		return NULL;
	}

	// Parse out long_arg & freq_arg
	if (!PyArg_ParseTuple(args, "OO", &long_arg, &freq_arg))
	{
		return NULL;
	}

	// Make sure frequency is not NULL
	if (!freq_arg)
	{	
		PyErr_SetString(PyExc_TypeError, "frequency not set.");
		return NULL;
	}

	// Parse out frequency into an int so we can use it easily
	if ((freq = freq_to_int(PyString_AsString(freq_arg))) == FR_ERR)
	{
		// If the frequency is invalid, set an error and return null
		PyErr_SetString(PyExc_TypeError, "invalid frequency.");
		return NULL;
	}
	// Make sure long_arg is not NULL
	if (!long_arg)
	{
		PyErr_SetString(PyExc_TypeError, "no date provided.");
		return NULL;
	}
	// Be sure long_arg is a long
	if (PyLong_Check(long_arg))
	{

		// XXX PyINCREF here?
		// Convert long_arg to a long long
		dlong = PyLong_AsLongLong(long_arg);
		// Format the dstruct to create the datetime object
		dstruct = long_to_datestruct(dlong, freq);
		// Create the PyDateTime Object as result
		result = PyDateTime_FromDateAndTime(dstruct.year, dstruct.month,
				 dstruct.day, dstruct.hour, dstruct.minute, dstruct.second,
				 dstruct.usecond);
	}
	else
	{
		// long_arg is not a long; error
		PyErr_SetString(PyExc_TypeError, "invalid date type");
		return NULL;
	}

	if (PyErr_Occurred())
		return NULL;

	return result;
}

PyObject *
long_to_datestring(PyObject *self, PyObject *args)
{
	PyObject *long_arg = NULL;    // string or datetime
	PyObject *freq_arg = NULL;	  // frequency as string
	PyObject *result   = NULL;	  // string result

	long long dlong = 0;          // Stores the long_arg
	int freq = FR_ERR;			  // freq_arg is a PyObject to be parsed to freq
	datestruct dstruct;		      // To store date values

	// macro PyDateTime_IMPORT must be invoked for PyDateTime_Check
	PyDateTime_IMPORT;

	// Make sure the callback function is set
	//  ! This doesn't check to make sure it's the right callback function
	//  ! This should all be done in some init script
	if (!PyCallable_Check(callback))
	{
		PyErr_SetString(PyExc_TypeError, "callback not set.");
		return NULL;
	}

	// Parse out long_arg & freq_arg
	if (!PyArg_ParseTuple(args, "OO", &long_arg, &freq_arg))
	{
		return NULL;
	}

	// Make sure frequency is not NULL
	if (!freq_arg)
	{	
		PyErr_SetString(PyExc_TypeError, "frequency not set.");
		return NULL;
	}

	// Parse out frequency into an int so we can use it easily
	if ((freq = freq_to_int(PyString_AsString(freq_arg))) == FR_ERR)
	{
		// If the frequency is invalid, set an error and return null
		PyErr_SetString(PyExc_TypeError, "invalid frequency.");
		return NULL;
	}
	// Make sure long_arg is not NULL
	if (!long_arg)
	{
		PyErr_SetString(PyExc_TypeError, "no date provided.");
		return NULL;
	}
	// Be sure long_arg is a long
	if (PyLong_Check(long_arg))
	{

		// XXX PyINCREF here?
		// Convert long_arg to a long long
		dlong = PyLong_AsLongLong(long_arg);
		// Format the dstruct to create the datetime object
		dstruct = long_to_datestruct(dlong, freq);
		// Create the Python String formatted according frequency
		if ((freq == FR_Y) || (freq == (FR_M) ||
		   (freq == FR_W) || (freq == FR_B) || freq == (FR_D))) {
			// Good. PyString_FromFormat won't let me do simple printf stuff
			// like "%04d-%02d-%02d" for simple date formatting.
			// Now I have to write this stuff from scratch...
		
			char year[4];
			char month[2];
			char day[2];
				
			sprintf(year,  "%04d", dstruct.year);
			sprintf(month, "%02d", dstruct.month);
			sprintf(day,   "%02d", dstruct.day);

			// Now form the result with our char*
			result = PyString_FromFormat("%s-%s-%s", year, month, day);
		} else if ((freq == FR_h) || (freq == FR_m) || freq == (FR_s)) {
			char year[4];
			char month[2];
			char day[2];
			char hour[2];
			char minute[2];
			char second[2];
				
			sprintf(year,   "%04d", dstruct.year);
			sprintf(month,  "%02d", dstruct.month);
			sprintf(day,    "%02d", dstruct.day);
			sprintf(hour,   "%02d", dstruct.hour);
			sprintf(minute, "%02d", dstruct.minute);
			sprintf(second, "%02d", dstruct.second);

			result = PyString_FromFormat("%s-%s-%s %s:%s:%s", year,
				     month, day, hour, minute, second);	
		} else if ((freq == FR_ms) || (freq == FR_us)) {
			char year[4];
			char month[2];
			char day[2];
			char hour[2];
			char minute[2];
			char second[2];
			char usecond[24];
				
			sprintf(year,   "%04d", dstruct.year);
			sprintf(month,  "%02d", dstruct.month);
			sprintf(day,    "%02d", dstruct.day);
			sprintf(hour,   "%02d", dstruct.hour);
			sprintf(minute, "%02d", dstruct.minute);
			sprintf(second, "%02d", dstruct.second);
			result = PyString_FromFormat("%s-%s-%s %s:%s:%s.%d", 
					 year, month, day, 
					 hour, minute, second,
					 dstruct.usecond);
		}
	}
	else
	{
		// long_arg is not a long; error
		PyErr_SetString(PyExc_TypeError, "invalid date type");
		return NULL;
	}

	if (PyErr_Occurred())
		return NULL;

	return result;
}

//=============
// module
// ============

// Tell Python what methods we can run from this module
static PyMethodDef methods[] = {
	{"set_callback", (PyCFunction)set_callback, 
	 METH_VARARGS, ""},
	{"test_callback", (PyCFunction)test_callback,
	 METH_VARARGS, ""},
	{"date_to_long", date_to_long,
	 METH_VARARGS, ""},
	{"long_to_datetime", long_to_datetime,
	 METH_VARARGS, ""},
	{"long_to_datestring", long_to_datestring,
	 METH_VARARGS, ""},
	{NULL, NULL}
};

PyMODINIT_FUNC
initparsedates(void)
{
	PyObject *parser;

	parser = Py_InitModule("parsedates", methods);
	if (parser == NULL)
		return;
}
