import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

class QRGenerator:
    def generate(self):
        #inp = input('qr코드로 만들 데이터: ')
        #filename = input('파일 이름: ')
        #img = qrcode.make(inp)
        #type(img)  # qrcode.image.pil.PilImage
        #img.save(f'{filename}.png')
        
        with open('qr_list.txt', 'r') as file:
            for txt in file:
                print(txt)
                tokens = txt.split('=')
                filename = tokens[0]
                data = tokens[1]
                self.__create_qr(data, filename)
                

    
    def __create_qr(self, data, filename):
        # img = qrcode.make(data)
        # type(img)  # qrcode.image.pil.PilImage
        # img.save(f'{filename}.png')
        
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
        qr.add_data(data)
        img = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
        img.save(f'{filename}.png')
        
        #img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
        #img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())

           