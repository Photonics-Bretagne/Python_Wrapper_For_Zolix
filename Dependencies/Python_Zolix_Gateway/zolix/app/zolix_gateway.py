import socket
import time


class ZolixError(Exception):
    pass


def tobool(boolstring):
    if boolstring == 'True':
        return True
    elif boolstring == 'False':
        return False
    else:
        raise ZolixError(f"Conversion de {boolstring} en booléen impossible")


class ZolixGateway:

    def __init__(self, ip, port):
        """Constructeur"""
        self.ip = ip
        self.port = port
        self.client = None

    # Characteristics
    def get_comport(self):
        return int(self._send('GetComport'))

    def set_comport(self, comport):
        self._send(f'SetComport({comport})')

    def get_usb_serials(self):
        return self._send('GetUSBSerials')

    def set_usb_serials(self, usbserial):
        self._send(f'SetUSBSerials({usbserial})')

    def get_usb_mode(self):
        return tobool(self._send('GetUSBMode'))

    def set_usb_mode(self, usbmode):
        self._send(f'SetUSBMode({usbmode})')

    def get_is_open(self):
        return tobool(self._send('GetIsOpen'))

    def get_system_manufacturer(self):
        return self._send('GetSystemManuFacturer')

    def get_system_model(self):
        return self._send('GetSystemModel')

    def get_system_serials_number(self):
        return self._send('GetSystemSerialsNumber')

    def get_system_factory_time(self):
        return self._send('GetSystemFactoryTime')

    def get_firmware_version(self):
        return self._send('GetFirmwareVersion')

    def get_current_wave(self):
        return float(self._send('GetCurrentWave').replace(',', '.'))

    def get_synchro_mode(self):
        return tobool(self._send('GetSynchroMode'))

    # Operation Method

    def open(self):
        return self._send('Open')

    def close(self):
        return self._send('Close')

    def connect(self):
        return self._send('Connect')

    def disconnect(self):
        return self._send('DisConnect')

    def search_zolix_usb_device(self):
        return int(self._send('SearchZolixUSBDevice'))

    def get_zolix_usb_serial(self, deviceindex):
        return self._send(f'GetZolixUSBSerial({deviceindex})')

    def get_current_grating(self):
        return int(self._send('GetCurrentGrating'))

    def set_current_grating(self, currentgrating):
        self._send(f'SetCurrentGrating({currentgrating})')

    def grating_home(self):
        return self._send('GratingHome')

    def move_to_wave(self, wavelength):
        return tobool(self._send(f'MoveToWave({wavelength})'))

    def move_wave(self, wavelength):
        return tobool(self._send(f'MoveWave({wavelength})'))

    def refresh_current_wave(self):
        return self._send('RefreshCurrentWave')

    def stop(self):
        return self._send('Stop')

    def set_speed(self, index, nspeed):
        self._send(f'SetSpeed({index},{nspeed})')

    def get_speed(self, index):
        return int(self._send(f'GetSpeed({index})'))

    def set_filter(self, nfilter):
        self._send(f'SetFilter({nfilter})')

    def get_filter(self):
        return int(self._send('GetFilter'))

    def filter_home(self):
        return self._send('FilterHome')

    def set_exit_port(self, nport):
        self._send(f'SetExitPort({nport})')

    def get_exit_port(self):
        return int(self._send('GetExitPort'))

    def set_exit_side_pos(self, npos):
        self._send(f'SetExitSidePos({npos})')

    def get_exit_side_pos(self):
        return int(self._send('GetExitSidePos'))

    def get_port_input(self):
        return int(self._send('GetPortInput'))

    def set_port_output(self, nvalue):
        self._send(f'SetPortOutput({nvalue})')

    def show_port_test(self):
        self._send('ShowPortTest')

    def reload_peripheral(self):
        self._send('ReloadPeripheral')

    def get_peripheral_count(self):
        return int(self._send('GetPeripheralCount'))

    def set_peripheral(self, index, peripheralname):
        self._send(f'SetPeripheral({index},{peripheralname})')

    def add_peripheral(self, peripheralname):
        return self._send(f'AddPeripheral({peripheralname})')

    def get_peripheral_name(self, index):
        return self._send(f'GetPeripheralName({index})')

    def set_peripheral_string(self, peripheralstring):
        self._send(f'SetPeripheralString({peripheralstring})')

    def motor_home(self, index):
        self._send(f'MotorHome({index})')

    def move_motor_to(self, index, steps):
        self._send(f'MoveMotorTo({index},{steps})')

    def get_motor_cur_pos(self, index):
        return int(self._send(f'GetMotorCurPos({index})'))

    def set_motor_speed(self, nmotorindex, nspeed):
        self._send(f'SetMotorSpeed({nmotorindex},{nspeed})')

    def get_motor_speed(self, nmotorindex):
        return int(self._send(f'GetMotorSpeed({nmotorindex})'))

    def set_motor_home_direction(self, nmotorindex, ndirection):
        self._send(f'SetMotorHomeDirection({nmotorindex},{ndirection})')

    def get_motor_home_direction(self, nmotorindex):
        return int(self._send(f'GetMotorHomeDirection({nmotorindex})'))

    def show_setting_dialog(self):
        self._send('ShowSettingDialog')

    def send_command(self, cmd):
        self._send(f'SendCommand({cmd})')

    def get_receive_string(self):
        return self._send('GetReceiveString')

    def store_data(self, naddress, bytedata):
        self._send(f'StoreData({naddress},{bytedata})')

    def load_data(self, naddress):
        return int(self._send(f'LoadData({naddress})'))

    def backup(self):
        self._send('Backup')

    def restore(self):
        self._send('Restore')

    def initialize(self):
        self._send('Initialize')

    def reload_system_infor(self):
        self._send('ReloadSystemInfor')

    def set_system_infor(self, manufacturer, model, serialsnumber, factorydate):
        self._send(f'SetSystemInfor({manufacturer},{model},{serialsnumber},{factorydate})')

    def reload_total_steps(self):
        self._send('ReloadTotalSteps')

    def get_total_steps(self):
        return int(self._send('GetTotalSteps'))

    def set_total_steps(self, totalsteps):
        self._send(f'SetTotalSteps({totalsteps})')

    def reload_turret(self):
        self._send('ReloadTurret')

    def get_turret(self):
        return int(self._send('GetTurret'))

    def set_turret(self, index):
        self._send(f'SetTurret({index})')

    def reload_rom_infor(self):
        self._send('ReloadRomInfor')

    def get_zero_pos(self, grating):
        return int(self._send(f'GetZeroPos({grating})'))

    def set_zero_pos(self, grating, zeropos):
        self._send(f'SetZeroPos({grating}, {zeropos})')

    def get_adjust_coefficient(self, grating, standwave, testwave):
        return float(self._send(f'GetAdjustCoefficient({grating},{standwave},{testwave})').replace(',', '.'))

    def get_coefficient(self, grating):
        return float(self._send(f'GetCoefficient({grating})').replace(',', '.'))

    def get_grating_wave_range_max(self, grating):
        return float(self._send(f'GetGratingWaveRangeMax({grating})').replace(',', '.'))

    def set_adjustment(self, grating, coefficient):
        self._send(f'SetAdjustment({grating},{coefficient})')

    def calibrate(self, grating, standwave, currentwave):
        return self._send(f'Calibrate({grating},{standwave},{currentwave})')

    def reload_init_wave(self):
        self._send('ReloadInitWave')

    def get_init_wave(self, grating):
        return float(self._send(f'GetInitWave({grating})').replace(',', '.'))

    def set_init_wave(self, grating, initwavepos):
        self._send(f'SetInitWave({grating}, {initwavepos})')

    def reload_gratings_param(self):
        self._send('ReloadGratingsParam')

    def set_grating_param(self, ngrating, ngroove, nblaze):
        self._send(f'SetGratingParam({ngrating},{ngroove},{nblaze})')

    def get_grating_param(self, ngrating):
        reponse = self._send(f'GetGratingParam({ngrating})')
        valeurs_string = reponse.split(",")

        return int(valeurs_string[0]), int(valeurs_string[1])

    def wave_to_steps(self, grating, wavelength):
        return int(self._send(f'WaveToSteps({grating}, {wavelength})'))

    def reload_current_grating(self):
        self._send('ReloadCurrentGrating')

    def reload_power_grating(self):
        self._send('ReloadPowerGrating')

    def set_power_grating(self, grating):
        self._send(f'SetPowerGrating({grating})')

    def get_power_grating(self):
        return int(self._send('GetPowerGrating'))

    def about_box(self):
        self._send('AboutBox')

    def slit_home(self, index):
        return self._send(f'SlitHome({index})')

    def get_slit_zero_pos(self, nindex):
        return int(self._send(f'GetSlitZeroPos({nindex})'))

    def set_slit_zero_pos(self, nindex, pnpos):
        self._send(f'SetSlitZeroPos({nindex},{pnpos})')

    def set_slit_bandpass(self, nindex, dblbandpass):
        self._send(f'SetSlitBandpass({nindex},{dblbandpass})')

    def get_slit_bandpass(self, nindex):
        return float(self._send(f'GetSlitBandpass({nindex})').replace(',', '.'))

    def set_slit_width(self, nindex, nwidth):
        self._send(f'SetSlitWidth({nindex},{nwidth})')

    def get_slit_width(self, nindex):
        return int(self._send(f'GetSlitWidth({nindex})'))

    def set_slit_type(self, nslittype):
        self._send(f'SetSlitType({nslittype})')

    def get_slit_type(self):
        return int(self._send('GetSlitType'))

    def set_entrance_port(self, nport):
        self._send(f'SetEntrancePort({nport})')

    def get_entrance_port(self):
        return int(self._send('GetEntrancePort'))

    def set_motor_total_steps(self, nmotorindex, ntotalsteps):
        self._send(f'SetMotorTotalSteps({nmotorindex},{ntotalsteps})')

    def get_motor_total_steps(self, nmotorindex):
        return int(self._send(f'GetMotorTotalSteps({nmotorindex})'))

    def set_setup_info(self):
        self._send('SetSetupInfo(true)')

    def connect_to_server(self):
        addr = (self.ip, int(self.port))
        print("[LANCEMENT] Le client se connecte au serveur...")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(5)
        self.client.connect(addr)
        print(f"[CONNEXION] {addr} connecté.")

    def disconnect_from_server(self):
        print("[ARRET] Le client se déconnecte du serveur...")
        self.client.close()
        print("[ARRET] Déconnecté.")

    def _send(self, msg_to_send):
        full_msg_to_send = ''
        full_msg_to_receive = ''
        enchar = "\n"
        full_msg_to_send = msg_to_send + enchar
        self.client.sendall(bytes(full_msg_to_send.encode("ascii", "ignore")))
        time.sleep(0.5)
        self.client.settimeout(40)
        msg_to_receive = self.client.recv(1024)

        full_msg_to_receive += msg_to_receive.decode("utf-8")

        etat = full_msg_to_receive[0:2]
        if etat != "OK":
            raise ZolixError(f"Commmande Zolix {msg_to_send} échouée")

        # Retrait du saut de ligne \r\n et du préfixe OK:
        return full_msg_to_receive[3:-2]
