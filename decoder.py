from pyzbar.pyzbar import _pixel_data, _symbols_for_image, _decode_symbols
import cv2
from contextlib import contextmanager
from pyzbar.pyzbar_error import PyZbarError
from pyzbar.wrapper import (
    zbar_image_scanner_set_config,
    zbar_image_scanner_create, zbar_image_scanner_destroy,
    zbar_image_create, zbar_image_destroy, zbar_image_set_format,
    zbar_image_set_size, zbar_image_set_data, zbar_scan_image,
    zbar_image_first_symbol, zbar_symbol_get_data_length,
    zbar_symbol_get_data, zbar_symbol_get_orientation,
    zbar_symbol_get_loc_size, zbar_symbol_get_loc_x, zbar_symbol_get_loc_y,
    zbar_symbol_get_quality, zbar_symbol_next, ZBarConfig, ZBarOrientation,
    ZBarSymbol, EXTERNAL_DEPENDENCIES,
)
from ctypes import cast, c_void_p, string_at

_FOURCC = {
    'L800': 808466521,
    'GRAY': 1497715271
}

@contextmanager
def _image():
    """A context manager for `zbar_image`, created and destoyed by
    `zbar_image_create` and `zbar_image_destroy`.

    Yields:
        POINTER(zbar_image): The created image

    Raises:
        PyZbarError: If the image could not be created.
    """
    image = zbar_image_create()
    if not image:
        raise PyZbarError('Could not create zbar image')
    else:
        try:
            yield image
        finally:
            zbar_image_destroy(image)


@contextmanager
def _image_scanner():
    """A context manager for `zbar_image_scanner`, created and destroyed by
    `zbar_image_scanner_create` and `zbar_image_scanner_destroy`.

    Yields:
        POINTER(zbar_image_scanner): The created scanner

    Raises:
        PyZbarError: If the decoder could not be created.
    """
    scanner = zbar_image_scanner_create()
    if not scanner:
        raise PyZbarError('Could not create image scanner')
    else:
        try:
            yield scanner
        finally:
            zbar_image_scanner_destroy(scanner)

# 画像を読み込む
image_path = "./data/google.com.png"
image_path = "./data/images.jpg"
image = cv2.imread(image_path)

# 画像のピクセルデータを取得
pixels, width, height = _pixel_data(image)
# print(pixels, width, height)

results = []
with _image_scanner() as scanner:
    with _image() as img:
        zbar_image_set_format(img, _FOURCC['L800'])
        zbar_image_set_size(img, width, height)
        zbar_image_set_data(img, cast(pixels, c_void_p), len(pixels), None)
        decoded = zbar_scan_image(scanner, img)
        if decoded < 0:
            raise PyZbarError('Unsupported image format')
        else:
            symbols = _symbols_for_image(img)
            
            results.extend(_decode_symbols(symbols))

# print(results)

