#include <Python.h>
#include <structmember.h>
#include <string.h>

// Define the Frequencies
char* freq_char[]   = {"NS",
	                   "US",
			           "MS",
					   "S",
					   "MIN",
					   "H",
					   "D",
					   "B",
					   "W",
					   "MON",
					   "Y",
					   NULL
};

#define NS  1
#define US  2
#define MS  3
#define S   4
#define MIN 5
#define H   6
#define D   7
#define B   8
#define W   9
#define MON 10
#define Y   11

/*
 * Takes a string and a frequency and returns
 * a longlong value corresponding to that datea
 *
 * -- Valid Strings
 *    > 2008-07-03T17:31:00
 *    July 3, 2008 at 5:31:00PM
 *
 * 	  > 
 */

int str_to_date(char* d_string, int freq)
{
//	printf("--Date: %c --Freq: %i", d_string, freq);
	return -1;	
}

staticforward PyTypeObject datetimeType;

typedef struct
{
	PyObject_HEAD   // macro used for refcount & pointer
	int freq;       // frequency of date_value
	long time; // 64 bit time since epoch
} datetimeObject;

static PyObject *
datetime_freq(datetimeObject *self, void *closure)
{
	return PyString_FromString(self->freq);
}

static PyObject *
datetime_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
	datetimeObject *self;

	self->freq = 0;
	self->time = 0;
	
	return (PyObject *)self;
}

static int
datetime_init(datetimeObject *self, PyObject *args, PyObject *kwds)
{
	char *arg_freq = NULL;
	long *arg_time = 0;

	static char* kwlist[] = {"freq", "time", NULL};

	if (! PyArg_ParseTupleAndKeywords(args, kwds, "i|L", kwlist,
			      &arg_freq, &arg_time))
		return -1;

	if (arg_freq)
	{
		/* Do frequency conversion based on a character */
		self->freq = arg_freq;
	}

	if (arg_time)
	{
		self->time = arg_time;
	}

	return 0;
}

static PyObject *
datetime_str(datetimeObject *self)
{
	return PyString_FromFormat("<datetime: --time: %ld --freq: %s>", 
					            self->time, self->freq);
}

static int
datetime_ReadOnly(datetimeObject *self, PyObject *value, void *closure)
{
	PyErr_SetString(PyExc_AttributeError, "Cannot set to read-only property");
	return -1;
}

static void
datetime_dealloc(PyObject* self)
{
	PyObject_Del(self);
}

// Methods
static PyMethodDef datetime_methods[] = {
	{NULL, NULL, 0, NULL}
};

// Members
static PyMemberDef datetime_members[] = {
	{"freq", T_INT, offsetof(datetimeObject, freq), 0,
	 "frequency"},
	{"time", T_LONGLONG, offsetof(datetimeObject, time), 0,
	 "64 bit representation of a time"},
	{NULL} /* Sentinel */
};

// Object Type
static PyTypeObject datetimeType = {
	PyObject_HEAD_INIT(NULL)
	0,			   			   /*ob_size*/
	"npy_datetime.datetime", /*tp_name*/
	sizeof(datetimeObject),       /*tp_basicsize*/
	0,                         /*tp_itemsize*/
    (destructor)datetime_dealloc,        /*tp_dealloc*/
    0,                         /*tp_print*/
    0,                         /*tp_getattr*/
    0,                         /*tp_setattr*/
    0,                         /*tp_compare*/
    0,                         /*tp_repr*/
    0,                         /*tp_as_number*/
    0,                         /*tp_as_sequence*/
    0,                         /*tp_as_mapping*/
    0,                         /*tp_hash */
    0,                         /*tp_call*/
    (reprfunc)datetime_str, /*tp_str*/
    0,                         /*tp_getattro*/
    0,                         /*tp_setattro*/
    0,                         /*tp_as_buffer*/
    Py_TPFLAGS_DEFAULT,        /*tp_flags*/
    "datetime objects",     /*tp_doc*/
    0,                         /*tp_traverse*/
    0,                         /*tp_clear*/
    0,                         /*tp_richcompare*/
    0,                         /*tp_weaklistoffset*/
    0,                         /*tp_iter*/
    0,                         /*tp_iternext*/
    datetime_methods,       /*tp_methods*/
    datetime_members,       /*tp_members*/
    0,        /*tp_getset*/
    0,                         /*tp_base*/
    0,                         /*tp_dict*/
    0,                         /*tp_descr_get*/
    0,                         /*tp_descr_set*/
    0,                         /*tp_dictoffset*/
    (initproc)datetime_init,/*tp_init*/
    0,                         /*tp_alloc*/
    datetime_new            /*tp_new*/
};


PyMODINIT_FUNC
initnpy_datetime(void)
{
	PyObject *date_object;

	/* Default new object creation */
	datetimeType.tp_new = PyType_GenericNew;

	/* Initilize the datetimeType */
	if (PyType_Ready(&datetimeType) < 0)
		return;

	/* Create a new module object based on a name and table of functions, 
	   returning the module object */
	date_object = Py_InitModule3("npy_datetime", datetime_methods,
				  "datetime module that creates a datetime object");

	/* Increment the reference count for this object */	
	Py_INCREF(&datetimeType);

	/* Adds the Object type to the module dictionary */
	PyModule_AddObject(date_object, "datetime", (PyObject *)&datetimeType);
}

