from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_grating_wave_range_max()
    test_common.print_result('GetGratingWaveRangeMax(1)', m)


if __name__ == '__main__':
    test()
