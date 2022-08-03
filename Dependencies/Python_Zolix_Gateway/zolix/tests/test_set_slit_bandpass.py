from zolix.tests import test_common


def test():
    test_common.zolix_gateway.set_slit_bandpass()
    test_common.print_result('SetSlitBandpass(1, 0)', m)


if __name__ == '__main__':
    test()
