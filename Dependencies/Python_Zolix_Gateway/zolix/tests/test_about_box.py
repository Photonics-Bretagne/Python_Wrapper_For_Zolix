from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.about_box()
    test_common.print_result('AboutBox', m)


if __name__ == '__main__':
    test()
