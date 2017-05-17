import lcddriver
import pywapi
import time


display = lcddriver.lcd()

try:
    while True:
    local_weather_for_table = pywapi.get_weather_from_weather_com('USNC0015')
    print("Trying to Write to LCD Display....")
    display.lcd_display_string(weather_com_result['current_conditions']['text'].lower(), 1)
    display.lcd_display_string("and " + weather_com_result['current_conditions']['temperature'] + "° in Apex", 2)
    time.sleep(5)
    display.lcd_clear()
    display.lcd_display_string("Have a nice day!", 1)
    time.sleep(3)
    display.lcd_clear()
    
    except KeyboardInterrupt:
        print("Clearing Screen...")
        display.lcd_clear()
    
