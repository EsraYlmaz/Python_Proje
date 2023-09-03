import sys
from PyQt5.QtWidgets import *
from giris_ui import Ui_Giris
from AnaEkran_ui import Ui_AnaEkran
import veritabani_6 as baglanti

class GirisPenceresi(QWidget,Ui_Giris):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sifreText.setEchoMode(QLineEdit.Password)
        self.girisbutonu.clicked.connect(self.fGirisKontrol)

    def fGirisKontrol(self):
        self.mesajlabel.setText("Giriş Butonu Tıklandı")
        eposta=self.epostaText.text()
        sifre=self.sifreText.text()
        k_id = baglanti.k_giris(eposta,sifre)
        if k_id ==0:
            self.mesajlabel.setText("Hatalı Giriş Yapıldı")
        else:
            self.mesajlabel.setText ("Giriş onaylandı")
            self.close
            self.ype =Ui_AnaEkran(k_id)
            self.ype.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = GirisPenceresi()
    pencere.show()
    sys.exit(app.exec_())


    
