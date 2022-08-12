# This is a sample Python script.

# Press Alt+Shift+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask, ImageColorMask


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
    )
    qr.add_data('https://ya-kraina.taplink.ws/')

    img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
    img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
    img_3 = qr.make_image(image_factory=StyledPilImage,
                          module_drawer=RoundedModuleDrawer(),
                          color_mask=ImageColorMask(color_mask_path="mask.png"),
                          embeded_image_path="image_2.jpg")

    img_1.save("some_file1.png")
    img_2.save("some_file2.png")
    img_3.save("some_file3.png")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
