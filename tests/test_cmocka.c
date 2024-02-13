#include <stdarg.h>
#include <stddef.h>
#include <setjmp.h>
#include <cmocka.h>
#include "operations.h"

double __wrap_add(double a, double b) {
    return mock_type(double);
}

static void test_multiply(void **state) {
    
    will_return(__wrap_add, 8);
    assert_int_equal(multiply(3,5), 15);

    will_return(__wrap_add, 5);
    assert_int_equal(multiply(0,5), 0);

    will_return(__wrap_add, 2);
    assert_int_equal(multiply(-3,5), -15);

    will_return(__wrap_add, -1);
    assert_int_equal(multiply(2,-3), -6);
}

static void test_divide(void **state) {
    assert_int_equal(divide(10, 2), 5);
    assert_int_equal(divide(-10, 2), -5);
    assert_int_equal(divide(10, -2), -5);
    assert_int_equal(divide(-10, -2), 5);
    assert_null(divide(10, 0));
    assert_int_equal(divide(0, 10), 0);
    assert_int_equal(divide(0, -10), 0);
    assert_null(divide(0, 0));
}

static void test_add(void **state) {
    assert_int_equal(add(3,7), 10);
    assert_int_equal(add(-3,7), 4);
    assert_int_equal(add(3,-7), -4);
    assert_int_equal(add(-3,-7), -10);
}

static void test_subtract(void **state) {
    assert_int_equal(subtract(1,1), 0);
    assert_int_equal(subtract(2,1), 1);
    assert_int_equal(subtract(1,2), -1);
    assert_int_equal(subtract(-1,-1), 0);
    assert_int_equal(subtract(-1, 1), -2);
}

int main(void) {
    const struct CMUnitTest tests[] = {
        cmocka_unit_test(test_divide),
        cmocka_unit_test(test_add),
        cmocka_unit_test(test_subtract),
        cmocka_unit_test(test_multiply),
    };
    return cmocka_run_group_tests(tests, NULL, NULL);
}