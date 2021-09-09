from math import sqrt


def get_base_classes(cls):
    r = [cls]
    for b in cls.__bases__:
        if b.__name__ != 'object':
            r.extend(get_base_classes(b))
    return r


def get_methods_in(*classes):
    r = []
    for cls in classes:
        methods = [(key, f) for key, f in cls.__dict__.items() if callable(f)]
        r.extend(methods)
    return r


def hex_to_rgb(hex_code):
    h = hex_code.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(*rgb_components):
    r, g, b = rgb_components
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def color_dist(a, b):
    dr = b[0] - a[0]
    dg = b[1] - a[1]
    db = b[2] - a[2]
    return sqrt(dr * dr + dg * dg + db * db)
