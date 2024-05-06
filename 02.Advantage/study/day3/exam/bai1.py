class HinhChuNhat:
    def __init__(self, chieudai, chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong

    def tinhchuvi(self):
        chuvi = 2 * (self.chieudai + self.chieurong)
        return chuvi

    def tinhdientich(self):
        dientich = self.chieudai * self.chieurong
        return dientich


hcn = HinhChuNhat(5, 4)

chuvi_hcn = hcn.tinhchuvi()
dien_tich_hcn = hcn.tinhdientich()
print("Chu vi hình chữ nhật:", chuvi_hcn, "m")
print("Diện tích hình chữ nhật:", dien_tich_hcn, "m²")
