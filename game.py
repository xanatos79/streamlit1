#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 17:40:14 2023

@author: gunterkraling
"""

import streamlit as st
import random
from PIL import Image

def main():
    st.title("Würfel-Werfer")

    # Sidebar-Titel
    st.sidebar.title("Steuerung")

    # Würfeln-Knopf in der Sidebar
    if st.sidebar.button('Würfeln'):
        # Zufällige Zahl zwischen 1 und 6 auswählen
        dice_value = random.randint(1, 6)
        
        # Das entsprechende Bild laden
        image_path = f"die_face_{dice_value}.jpg"
        image = Image.open(image_path)

        # Bildgröße auf 25% reduzieren
        width, height = image.size
        image = image.resize((int(width * 0.25), int(height * 0.25)))
        
        # Bild in der Sidebar anzeigen
        st.sidebar.image(image, caption=f"Sie haben eine {dice_value} geworfen!")

if __name__ == '__main__':
    main()
