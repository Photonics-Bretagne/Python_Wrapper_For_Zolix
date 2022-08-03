from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.store_data(352, 2)
    test_common.print_result('StoreData(352, 2)', m)


if __name__ == '__main__':
    test()
