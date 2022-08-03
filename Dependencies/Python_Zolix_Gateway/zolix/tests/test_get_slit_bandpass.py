from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_slit_bandpass()
    test_common.print_result('GetSlitBandpass(1)', m)


if __name__ == '__main__':
    test()
