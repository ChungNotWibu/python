class GiaoVien:
    def __init__(self, ten, nam_sinh, nam_bat_dau_cong_tac, mon_day, lop_day, truong_cong_tac, he_so_luong):
        self.ten = ten
        self.nam_sinh = nam_sinh
        self.nam_bat_dau_cong_tac = nam_bat_dau_cong_tac
        self.mon_day = mon_day
        self.lop_day = lop_day
        self.truong_cong_tac = truong_cong_tac
        self.he_so_luong = he_so_luong
        self.luong_co_ban = 1000  # $

    def information(self):
        print(f'Tên: {self.ten}\nNăm sinh: {self.nam_sinh}\nNăm bắt đầu công tác: {self.nam_bat_dau_cong_tac}\nMôn dạy: {self.mon_day}\nLớp dạy: {self.lop_day}\nTrường công tác: {self.truong_cong_tac}\nHệ số lương: {self.he_so_luong}')

    def age(self):
        tuoi_doi = 2024 - self.nam_sinh
        tuoi_nghe = 2024 - self.nam_bat_dau_cong_tac
        luong = self.he_so_luong * self.luong_co_ban
        print(f'Tuổi đời: {tuoi_doi}\nTuổi nghề: {tuoi_nghe}\nLương: {luong} đô')

giao_vien_hanh = GiaoVien(ten='Nguyễn Thị Hạnh', nam_sinh=1988, nam_bat_dau_cong_tac=2008,mon_day='Lý', lop_day=12, truong_cong_tac='THPT chuyên Hà Nội', he_so_luong=2.3)

giao_vien_hanh.information()
giao_vien_hanh.age()
