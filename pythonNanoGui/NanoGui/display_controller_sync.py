# ePaper2in9_test_sync.py Demo of synchronous code on 2.9" EPD display

# Released under the MIT License (MIT). See LICENSE.
# Copyright (c) 2020 Peter Hinch

# color_setup must set landcsape True, asyn False and must not set demo_mode

from color_setup import ssd
from gui.core.writer import Writer
from gui.core.nanogui import refresh
from gui.widgets.label import Label

# Fonts
import gui.fonts.arial10 as arial10
import gui.fonts.freesans20 as large

wri = Writer(ssd, arial10, verbose=False)
wri.set_clip(False, False, False)

wri_large = Writer(ssd, large, verbose=False)
wri_large.set_clip(False, False, False)
# Label(wri_large, x, y, 'Label')
    
def main():
    # Label(wri, x, y, 'Label')
    # Label(wri_large, x, y, 'Label')
    # ssd.fill(0)  # White screen
    # ssd.fill(1)  # Black screen
    # refresh(ssd)  # Show Text
    # ssd.wait_until_ready()  # Wait for display to be ready
    # ssd._full = False  # Partial updates
    # ssd._full = True   # Full updates


main()
    
