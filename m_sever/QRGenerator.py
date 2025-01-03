import io
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

class QRGenerator:
    def generate(self, data):
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
        qr.add_data(data)
        img = qr.make_image(image_factory=StyledPilImage
                            , color_mask=RadialGradiantColorMask())
        # img.save(f'{filename}.png')
        # 여기에 파일로 쓰는 대신에 메모리 상에서 조작 가능
        img_bytes = io.BytesIO()
        img.save(img_bytes)
        img_bytes.seek(0)
        return img_bytes.read()

        # 아까는 file 읽어온 데이터를 bytesIO에 썼는데,
        # 이번에는 QR 코드를 만든다음에, 메모리 상에 있는 QR코드를 bytesIO에 써줘 ㅇㅇ
        # 데이터를 클라이언트 소켓으로 전달할 수 있도록!
        # offset 0으로 맞춰놓고 들어온 데이터 다 읽으면 되잖아.
        # (저장된 qr데이터를 img_bytes에 저장해서 .read로 읽어오는 것)
