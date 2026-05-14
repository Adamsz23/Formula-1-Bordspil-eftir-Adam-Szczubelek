import utime
from lcd_api import LcdApi

class I2cLcd(LcdApi):
    def __init__(self, i2c, i2c_addr, num_lines, num_columns):
        self.i2c = i2c
        self.i2c_addr = i2c_addr
        self.i2c.writeto(self.i2c_addr, bytearray([0]))
        utime.sleep_ms(20)
        self.hal_write_command(0x03)
        utime.sleep_ms(5)
        self.hal_write_command(0x03)
        utime.sleep_ms(5)
        self.hal_write_command(0x03)
        utime.sleep_ms(5)
        self.hal_write_command(0x02)
        self.hal_write_command(0x28)
        self.hal_write_command(0x0c)
        self.hal_write_command(0x06)
        self.clear()

    def hal_write_init_nibble(self, nibble):
        byte = ((nibble << 4) & 0xF0) | 0x08
        self.i2c.writeto(self.i2c_addr, bytearray([byte | 0x04]))
        self.i2c.writeto(self.i2c_addr, bytearray([byte]))

    def hal_write_command(self, cmd):
        self.hal_write_init_nibble(cmd >> 4)
        self.hal_write_init_nibble(cmd & 0x0F)

    def hal_write_data(self, data):
        byte = (data & 0xF0) | 0x08 | 0x01
        self.i2c.writeto(self.i2c_addr, bytearray([byte | 0x04]))
        self.i2c.writeto(self.i2c_addr, bytearray([byte]))
        byte = ((data << 4) & 0xF0) | 0x08 | 0x01
        self.i2c.writeto(self.i2c_addr, bytearray([byte | 0x04]))
        self.i2c.writeto(self.i2c_addr, bytearray([byte]))
