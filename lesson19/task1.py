import pyowm


class ContextManager:

    def __init__(self, file_name: str, act: str):
        self.act = act
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, self.act)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.file_name)
        self.file.close()

    @staticmethod
    def _weather_diary():
        owm = pyowm.OWM('74079691aea441d2d19028bb5058777e')
        wman = owm.weather_manager()
        observation = wman.weather_at_place('Mykolaiv')
        w = observation.weather
        y = int((int(w.temperature("celsius")["temp_min"]) + int(w.temperature("celsius")["temp_max"])) / 2)
        return f'Средняя температура в Николаеве = {str(y)} градусов по Цельсию!'


cm = ContextManager('diary.txt', 'w')
if __name__ == '__main__':
    with cm as file:
        cm.file.write(cm._weather_diary())
    print(cm._weather_diary())
