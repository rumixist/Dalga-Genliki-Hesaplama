# Lazer ablatif itme sistemi parametreleri

# Lazer parametreleri
lazer_gucu = 100000  # Watt
lazer_dalga_boyu = 1e-6  # metre
odak_nokta_capi = 0.01  # metre
lazer_aci = 45  # derece

# Malzeme parametreleri
polikapton_yogunlugu = 1.2  # gram/cm^3

# Ablasyon parametreleri
ablatif_hiz = 100  # mm^3/saniye

# Plazma parametreleri
iyon_orani = 0.7
elektron_orani = 1 - iyon_orani

# Sistem parametreleri
isi_iletkenligi = 10  # Watt/(metre*Kelvin)

# Hesaplamalar

# Işın alanı
alan = math.pi * (odak_nokta_capi / 2)**2

# Işın gücü yoğunluğu
isin_gucu_yogunlugu = lazer_gucu / alan

# Ablasyon kütlesi
ablatif_kutle = ablatif_hiz * alan * polikapton_yogunlugu

# Plazma hızı
plazma_hizi = (2 * isin_gucu_yogunlugu / (polikapton_yogunlugu * ablatif_hiz * iyon_orani))**0.5

# Plazma kinetik enerjisi
plazma_kinetik_enerjisi = 0.5 * ablatif_kutle * plazma_hizi**2

# Elektron ısı akışı
elektron_isi_akisi = isin_gucu_yogunlugu * elektron_orani

# Isı kaybı
isi_kaybi = isi_iletkenligi * alan * elektron_isi_akisi

# Diğer kayıplar
diger_kayiplar = 0.2 * plazma_kinetik_enerjisi

# Rezonans enerjisi
rezonans_enerjisi = plazma_kinetik_enerjisi + isi_kaybi + diger_kayiplar

# Sonuçları yazdırma
print("Işın alanı:", alan, "cm^2")
print("Işın gücü yoğunluğu:", isin_gucu_yogunlugu, "kW/cm^2")
print("Ablasyon kütlesi:", ablatif_kutle, "gram/saniye")
print("Plazma hızı:", plazma_hizi, "m/saniye")
print("Plazma kinetik enerjisi:", plazma_kinetik_enerjisi, "Joule")
print("Isı kaybı:", isi_kaybi, "Joule")
print("Diğer kayıplar:", diger_kayiplar, "Joule")
print("Rezonans enerjisi:", rezonans_enerjisi, "Joule")
