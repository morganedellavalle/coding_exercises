######### DAY 8 ##########

filename = "data/day8.txt"

class Image:
    def __init__(self, width, height, code):
        self.width = width
        self.height = height
        self.pixels = list(code)
        self.n_layers = int(len(code) / (width*height))
        self.layers = {}

    def split_layers(self):
        start_index = 0
        for i in range(self.n_layers):
            end_index = start_index + self.width * self.height
            self.layers[i] = self.pixels[start_index:end_index]
            start_index = end_index 

    
    def find_number_occurences(self, layer, digit):
        return self.layers[layer].count(digit)

    def solve_part_1(self):
        min_zeros = 1000
        min_layer = -1
        
        for i in range(self.n_layers):
            zeros = self.find_number_occurences(i, "0")
            if zeros < min_zeros:
                min_zeros = zeros
                min_layer = i

        return self.find_number_occurences(min_layer, "1") * self.find_number_occurences(min_layer, "2")
        

if __name__ == "__main__":
    with open(filename) as f:
        encoding = f.readlines()[0].strip()

    image = Image(25, 6, encoding)
    image.split_layers()
    print(image.solve_part_1())