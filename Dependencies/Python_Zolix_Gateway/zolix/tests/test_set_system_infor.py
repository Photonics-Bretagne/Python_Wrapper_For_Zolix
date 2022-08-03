from zolix.tests import test_common

def test():
    subtest("Zolix", "Omni200", "19007", "20190313")
    subtest("Random1", "Random2", "Random3", "Random4")


def subtest(p1, p2, p3, p4):
    test_common.zolix_gateway.set_system_infor(p1, p2, p3, p4)
    m1 = test_common.zolix_gateway.get_system_manufacturer()
    m2 = test_common.zolix_gateway.get_system_model()
    m3 = test_common.zolix_gateway.get_system_serials_number()
    m4 = test_common.zolix_gateway.get_system_factory_time()
    test_common.print_assert(f'GetFilter', p1, m1)


if __name__ == '__main__':
    test()
