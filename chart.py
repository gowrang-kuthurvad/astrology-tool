from flatlib.chart import Chart
from flatlib import const
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos


def generate_chart(date, time, latitude, longitude):
    """
    Generate basic astrological chart information.
    
    date format: 'YYYY/MM/DD'
    time format: 'HH:MM'
    latitude: float
    longitude: float
    """

    datetime = Datetime(date, time, '+00:00')
    position = GeoPos(str(latitude), str(longitude))

    chart = Chart(datetime, position)

    sun = chart.get(const.SUN)
    moon = chart.get(const.MOON)
    asc = chart.get(const.ASC)

    return {
        "Sun Sign": sun.sign,
        "Moon Sign": moon.sign,
        "Ascendant": asc.sign
    }
