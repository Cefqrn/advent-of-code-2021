import os

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    algo, image = f.read().split('\n\n')

    algo = algo
    *image, = image.splitlines()

def use_algo(image, step):
    offset = 1
    nrlen = len(image[0]) + offset*2
    new_image = [list("." * nrlen), *map(lambda x: list(f".{x}."), image), list("." * nrlen)]
    for y, row in enumerate(new_image):
        for x, _ in enumerate(row):
            value = 0
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if y + dy < offset or x + dx < offset:
                        value += step % 2
                        value <<= 1
                        continue
                    try:
                        value += image[y+dy-offset][x+dx-offset] == "#"
                    except:
                        value += step % 2
                    value <<= 1
            value >>= 1
            new_image[y][x] = algo[value]
    if step == 1:
        return list(map(lambda x: ''.join(x), new_image))
    return use_algo(list(map(lambda x: ''.join(x), new_image)), step-1)

print(sum(map(lambda x: x.count("#"), use_algo(image, 2))))
print(sum(map(lambda x: x.count("#"), use_algo(image, 50))))