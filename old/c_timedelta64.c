#include <Python.h>
#include <structmember.h>

/************************************************************
**   Helper functions, etc?
************************************************************/




/*************************************************************
**   timedelta64 Type Definition
**************************************************************/

/* Tell the compiler what timedelta64Type is */
staticforward PyTypeObject timedelta64Type;

/* timedelta64 Object */
typedef struct
{
	PyObject_HEAD   // macro used for refcount & pointer
	int freq;       // frequency of date_value
	long long int time; // 64 bit time since epoch
} timedelta64;

/* Create new timedelta64 objects */
static PyObject *
timedelta64_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
	timedelta64 *self;

	self = (timedelta64*)type->tp_alloc(type, 0);
	if (self !=NULL)
	{
		/* initialize attributes here */
		self->freq = 1;
		self->time = 1;
	}

	return (PyObject *)self;
}

/* The initilization function */
static int
timedelta64_init(timedelta64 *self, PyObject *args, PyObject *kwds)
{
	char *arg_freq = NULL;
	long long int *arg_time = 0;

	static char* kwlist[] = {"freq", "time", NULL};

	if (! PyArg_ParseTupleAndKeywords(args, kwds, "c|L", kwlist,
			      &arg_freq, &arg_time))
		return -1;

	if (arg_freq)
	{
		/* Do frequency conversion based on a character */
		self->freq = 10;
	}

	if (arg_time)
	{
		self->time = arg_time;
	}

	return 0;
}

/* The Print function */
static PyObject *
timedelta64_str(timedelta64 *self)
{
	return PyString_FromFormat("<timedelta64: --time: %ld --freq: %d>", 
					            self->time, self->freq);
}

/* The deallocation function */
static void
timedelta64_dealloc(PyObject* self)
{
	PyObject_Del(self);
}

/* Tells Python what methods we can use on timedelta64 object */
static PyMethodDef timedelta64_methods[] = {
	{NULL, NULL, 0, NULL}
};

/************* timedelta64 Members *************/
static PyMemberDef timedelta64_members[] = {
	{"freq", T_INT, offsetof(timedelta64, freq), 0,
	 "frequency"},
	{"time", T_LONGLONG, offsetof(timedelta64, time), 0,
	 "64 bit representation of a time"},
	{NULL} /* Sentinel */
};

/************* The timedelta64 object type **************/
static PyTypeObject timedelta64Type = {
	PyObject_HEAD_INIT(NULL)
	0,			   			   /*ob_size*/
	"datetime.timedelta64", /*tp_name*/
	sizeof(timedelta64),       /*tp_basicsize*/
	0,                         /*tp_itemsize*/
    (destructor)timedelta64_dealloc,        /*tp_dealloc*/
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
    (reprfunc)timedelta64_str, /*tp_str*/
    0,                         /*tp_getattro*/
    0,                         /*tp_setattro*/
    0,                         /*tp_as_buffer*/
    Py_TPFLAGS_DEFAULT,        /*tp_flags*/
    "timedelta64 objects",     /*tp_doc*/
    0,                         /*tp_traverse*/
    0,                         /*tp_clear*/
    0,                         /*tp_richcompare*/
    0,                         /*tp_weaklistoffset*/
    0,                         /*tp_iter*/
    0,                         /*tp_iternext*/
    timedelta64_methods,       /*tp_methods*/
    timedelta64_members,       /*tp_members*/
    0,                         /*tp_getset*/
    0,                         /*tp_base*/
    0,                         /*tp_dict*/
    0,                         /*tp_descr_get*/
    0,                         /*tp_descr_set*/
    0,                         /*tp_dictoffset*/
    (initproc)timedelta64_init,/*tp_init*/
    0,                         /*tp_alloc*/
    timedelta64_new            /*tp_new*/
};


/* The initialization of timedelta64 object */
PyMODINIT_FUNC
inttimedelta64(void)
{
	PyObject *date_object;

	/* Default new object creation */
	timedelta64Type.tp_new = PyType_GenericNew;

	/* Initilize the timedelta64Type */
	if (PyType_Ready(&timedelta64Type) < 0)
		return;

	/* Create a new module object based on a name and table of functions, 
	   returning the module object */
	date_object = Py_InitModule3("timedelta64", timedelta64_methods,
				  "timedelta64 module that creates a timedelta64 object");

	/* Increment the reference count for this object */	
	Py_INCREF(&timedelta64Type);

	/* Adds the type to the module dictionary */
	PyModule_AddObject(date_object, "timedelta64", (PyObject *)&timedelta64Type);
}
