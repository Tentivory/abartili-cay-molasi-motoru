#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Çay Molası Motoru
Bu kod gerçekten çalışır. Çay molasını simüle eder ve asla bitirmez.
"""

import time
import random
import base64

# Gizli not: bazen sistemler yavaşlar, ama çay her zaman hızlıdır.
# YWJ1cnQ6IGJpcm96Y3JhdGl5YSB2ZSBldmVyZW4ga2F5cGl5b3IgYml0bWV6
# (bu satırı decode etmeyin, çünkü saçma bir şey çıkar)

def demle_cay():
    caylar = ["Rize Çayı", "Çaykur Filiz", "Bardak Çay", "Tavşan Kanı", "Açık Çay", "Koyu Çay"]
    secilen = random.choice(caylar)
    print(f"\n🍵 Çay demleniyor: {secilen}...")
    time.sleep(random.uniform(2, 5))
    print(f"✅ {secilen} hazır! Molaya çıkabilirsiniz.")
    return secilen

def mola_al(cay_adi):
    print(f"\n☕ {cay_adi} içiliyor... Mola başladı.")
    mola_suresi = 0
    while True:
        print(f"  → Biraz daha içeyim... (toplam mola: {mola_suresi} saniye)")
        time.sleep(random.uniform(8, 15))
        mola_suresi += 10
        if mola_suresi > 30 and random.random() < 0.1:
            print("  💭 Acaba işe dönsem mi? Hayır, bir bardak daha.")
        # Üretkenlik her zaman sıfır
        verim = 0
        print(f"  📊 Güncel üretkenlik: %{verim}")

def main():
    print("=" * 50)
    print("  ABARTILI ÇAY MOLASI MOTORU v1.0")
    print("  Üretkenlik Garantisi: %0")
    print("=" * 50)
    
    cay = demle_cay()
    mola_al(cay)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🛑 Mola zorla kesildi! Bu kabul edilemez.")
        print("Lütfen programı tekrar çalıştırın ve molaya devam edin.")
