import utime

class LcdApi:
    def __init__(self, num_lines, num_columns):
        self.num_lines = num_lines
        self.num_columns = num_columns
        self.cursor_x = 0
        self.cursor_y = 0
        self.backlight = True
        self.display_on = True

    def clear(self):
        self.hal_write_command(0x01)
        utime.sleep_ms(2)

    def putstr(self, string):
        for char in string:
            if char == '\n':
                self.cursor_x = 0
                self.cursor_y += 1
            else:
                self.hal_write_data(ord(char))

    def hal_write_command(self, cmd):
        raise NotImplementedError

    def hal_write_data(self, data):
        raise NotImplementedError
