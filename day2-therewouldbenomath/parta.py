    
def calculate_wrapping(length, width, height):
    surfaceArea = 2 * length * width + 2 * width * height + 2 * height * length
    smallest_side = min(length * width, width * height, height * length)
    return surfaceArea + smallest_side

