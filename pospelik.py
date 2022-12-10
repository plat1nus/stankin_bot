class Pospelik:
    def __init__(self):

        self.get_info_from_file()

    def get_info_from_file(self):
        with open("pospelik_info.txt", "r") as f:
            data = f.readline().split()
            self.saturation = int(data[0])
            self.money = int(data[1])
            self.body_path = data[2]
            self.eyes_path = data[3]
            self.glasses_path = data[4]
            self.smile_path = data[5]

    def put_info_to_file(self):
        with open("pospelik_info.txt", "rw") as f:
            f.truncate(0)
            f.write(f"{self.saturation} {self.body_path} {self.eyes_path} {self.glasses_path} {self.smile_path}")

    def update_body(self, upd_body):
        self.body_path = upd_body

    def update_glasses(self, upd_glasses):
        self.glasses_path = upd_glasses

    def update_smile(self, upd_smile):
        self.smile_path = upd_smile

    def update_eyes(self, upd_eyes):
        self.eyes_path = upd_eyes

    def update_money(self, upd_money):
        self.money = upd_money