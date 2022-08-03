from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_synchro_mode()
    test_common.print_result('GetSynchroMode', m)


if __name__ == '__main__':
    test()
