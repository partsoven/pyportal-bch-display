from adafruit_thermal_printer.thermal_printer import JUSTIFY_LEFT, \
JUSTIFY_CENTER, JUSTIFY_RIGHT, SIZE_SMALL, SIZE_MEDIUM, SIZE_LARGE, \
UNDERLINE_THIN, UNDERLINE_THICK

def get_printer_class(version):
    """Retrieve the class to construct for an instance of the specified
    thermal printer version.  Pass in the printer firmware version as a numeric
    value like 2.68, 2.64, etc.  You can get this value by holding the button
    on the printer as it powers on and a test page is printed--look at the
    bottom of the test page for the version number.
    """
    assert version is not None
    assert version >= 0.0
    if version < 2.64:
        import adafruit_thermal_printer.thermal_printer_legacy as thermal_printer
    elif version < 2.68:
        import adafruit_thermal_printer.thermal_printer_264 as thermal_printer
    else:
        import adafruit_thermal_printer.thermal_printer as thermal_printer
    return thermal_printer.ThermalPrinter
