#

import time
import requests

class OpenWeather :
    def __init__ (self ,
                  display ,
                  latitude ,
                  longitude ,
                  token = None) :
        #import requests
        #print ("__init__", latitude, longitude, token)
        self.display = display
        self.latitude = latitude
        self.longitude = longitude
        self.token = token
        self.current_weather = None
        self.current_weather_description = None
        self.forcast_min_idx = 1
        self.forcast_max_idx = self.forcast_min_idx + 4  # 5 entries
        self.pressure_last = None
        self.utc_offset = 0
        self.day_of_week = [
            "Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"
            ]
        self.date_format = "{year:4d}/{month:02d}/{day:02d}"
        self.time_format = "{hour:02d}:{minute:02d}:{second:02d}"
        self.http_request = "https://api.openweathermap.org/data/3.0/onecall" \
                            "?lat={lat}&lon={lon}&exclude=minutely,hourly&units=imperial&appid={appid}"

    def access_weather_data (self) :
        url = self.http_request.format (lat = self.latitude ,
                                        lon = self.longitude ,
                                        appid = self.token
                                        )
        #print ("URL:", url)
        try :
            self.current_weather = requests.get (url = url).json ()
            if self.utc_offset != self.current_weather ["timezone_offset"] :
                self.utc_offset = self.current_weather ["timezone_offset"]
        except :
            print ("OpenWeather: access failed")

    def get_current_weather (self) :
        if True :
            self.access_weather_data ()
        else :
            with open('OpenWeather.json', 'rb') as json_file:  # For testing
                self.current_weather = json.loads (json_file.read ())
            self.utc_offset = self.current_weather ["timezone_offset"]
        if self.current_weather is None :
            return
        pressure_direction = " "         # '+' UP, '-' DOWN
        if self.pressure_last is None :
            self.pressure_last = self.current_weather ["current"]["pressure"]
        if self.current_weather ["current"]["pressure"] != self.pressure_last :
            if self.current_weather ["current"]["pressure"] > self.pressure_last :
                pressure_direction = "+"
            else :
                pressure_direction = "-"
            self.pressure_last = self.current_weather ["current"]["pressure"]
        wind_speed = int (self.current_weather ["current"]["wind_speed"] + 0.5)
        wind_degrees = self.current_weather ["current"]["wind_deg"]
        wind_direction = self.format_wind_direction (wind_speed,
                                                     self.current_weather ["current"]["wind_deg"])
        daily_forcast = []
        for day_idx, day in enumerate (self.current_weather ["daily"]) :
            if day_idx < self.forcast_min_idx :
                continue
            if day_idx > self.forcast_max_idx :
                break
            wind_speed = int (day ["wind_speed"] + 0.5)
            day_forcast = {
                "date" : self.format_date (day ["dt"]) ,
                "day_of_week" : self.format_day_of_week (day ["dt"]) ,
                "high_f" : int (day ["temp"]["max"] + 0.5) ,
                "low_f" : int (day ["temp"]["min"] + 0.5) ,
                "pressure_m" : day ["pressure"] ,
                "pressure_i" : round (day ["pressure"] * 0.029529980, 2) ,
                "humidity" : day ["humidity"] ,
                "wind_speed" : wind_speed ,
                "wind_direction" : self.format_wind_direction (wind_speed, day ["wind_deg"])
                }
            daily_forcast.append (day_forcast)
            #print (self.format_date (day ["dt"]))
        #print (daily_forcast)
        return {
            "date" : self.format_date (self.current_weather ["current"]["dt"]) ,
            "time" : self.format_time (self.current_weather ["current"]["dt"]) ,
            "temperature_f" : int (round (self.current_weather ["current"]["temp"], 0)) ,
            "pressure_m" : self.current_weather ["current"]["pressure"] ,
            "pressure_i" : round (self.current_weather ["current"]["pressure"] * 0.029529980, 2) ,
            "pressure_direction" : pressure_direction ,
            "humidity" : self.current_weather ["current"]["humidity"] ,
            "wind_speed" : wind_speed ,
            "wind_degrees" : wind_degrees ,
            "wind_direction" : wind_direction ,
            "weather_description" : self.current_weather ["current"]["weather"][0]["description"] ,
            "daily_forcast" : daily_forcast
            }

    def format_date (self, utc_time) :
        local_time = time.localtime (utc_time + self.utc_offset)
        return self.date_format.format (year = local_time [0] ,
                                        month = local_time [1] ,
                                        day = local_time [2]
                                        )

    def format_time (self, utc_time) :
        local_time = time.localtime (utc_time + self.utc_offset)
        return self.time_format.format (hour = local_time [3] ,
                                        minute = local_time [4] ,
                                        second = local_time [5])

    def format_day_of_week (self, utc_time) :
        local_time = time.localtime (utc_time + self.utc_offset)
        return self.day_of_week [local_time [6]]

    def format_wind_direction (self, wind_speed, wind_degrees) :
        wind_direction = ""
        if wind_speed > 0 :
            if wind_degrees >= 352 or wind_degrees <= 14 :
                wind_direction = "N"        # North
            elif wind_degrees <= 36 :
                wind_direction = "NNE"
            elif wind_degrees <= 59 :
                wind_direction = "NE"
            elif wind_degrees <= 81 :
                wind_direction = "ENE"
            elif wind_degrees <= 104 :
                wind_direction = "E"        # East
            elif wind_degrees <= 126 :
                wind_direction = "ESE"
            elif wind_degrees <= 149 :
                wind_direction = "SE"
            elif wind_degrees <= 171 :
                wind_direction = "SSE"
            elif wind_degrees <= 194 :
                wind_direction = "S"        # South
            elif wind_degrees <= 216 :
                wind_direction = "SSW"
            elif wind_degrees <= 239 :
                wind_direction = "SW"
            elif wind_degrees <= 261 :
                wind_direction = "WSW"
            elif wind_degrees <= 284 :
                wind_direction = "W"        # West
            elif wind_degrees <= 306 :
                wind_direction = "WNW"
            elif wind_degrees <= 329 :
                wind_direction = "NW"
            elif wind_degrees <= 351 :
                wind_direction = "NNW"
        return wind_direction

    def update (self) :
        current_weather = self.get_current_weather ()
        if current_weather is None :
            return
        self.display.update_area (area_id = "c_temperature" ,
                             text = "{: 4d}".format (current_weather["temperature_f"]))
        self.display.update_area (area_id = "c_wind" ,
                             text = "{: 3d} {}".format (current_weather["wind_speed"],
                                                        current_weather["wind_direction"]))
        self.display.update_area (area_id = "c_pressure" ,
                             text = "{:2.2f} {}".format (current_weather["pressure_i"] ,
                                                         current_weather["pressure_direction"]))
        for day_idx, day in enumerate (current_weather ["daily_forcast"]) :
            #print (day)
            self.display.update_area (area_id = "w_dow_{}".format (day_idx) ,
                                        text = day ["day_of_week"])
            self.display.update_area (area_id = "w_temp_high_{}".format (day_idx) ,
                                        text = "{:4d}".format (day ["high_f"]))
            self.display.update_area (area_id = "w_temp_low_{}".format (day_idx) ,
                                        text = "{:4d}".format (day ["low_f"]))
            self.display.update_area (area_id = "w_wind_direction_{}".format (day_idx) ,
                                        text = "{: 3d} {}".format (day ["wind_speed"],
                                                                day ["wind_direction"]))
            self.display.update_area (area_id = "w_pressure_{}".format (day_idx) ,
                                        text = "{:2.2f}".format (day ["pressure_i"]))

        if current_weather["weather_description"] != self.current_weather_description :
            self.current_weather_description = current_weather["weather_description"]
            status_text = self.current_weather_description
            if len (status_text) > 25 :
                status_text = status_text [0:25]
            self.display.update_area (area_id = "status" ,
                                      text = self.current_weather_description)

## end OpenWeather ##

if __name__ == "__main__" :
    pass
