class File:
    def __init__(self, path):
        self.input)file = path
        self.output_file = path[:-2]+'out'
    def open_in(self):
        return open(self.input_file, 'r')
    def open_out(self):
        return open(self.output_file, 'w')
    def cases(self):
        input_file = self.open_in()
        no_of_cases = int(input_file.readline())
        for n in range(no_of_cases):
            pass






