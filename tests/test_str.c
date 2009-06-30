#include "../c_datetime.c"
#include <assert.h>

void test_basic_creation()
{
	assert(str_to_date("1-1-1970", 1) == 0); 
}

int main()
{
	test_basic_creation();
}
