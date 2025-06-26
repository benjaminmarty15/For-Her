import streamlit as st

# Judul & Header
st.title("💌 A Little Message Just for You")
st.header("🌷 From Someone Who Deeply Loves You")

# Isi pesan
st.markdown("""
> **Grace Monalisa Sihombing**,  
>
> Awalnya kita cuma ketemu di TikTok,  
> eh ternyata kamu teman SD-ku sendiri.  
> Dunia memang kecil, tapi hatiku langsung penuh saat sadar —  
> kamu yang selama ini aku cari. ✨  
>
> Aku mulai nge-chat kamu dengan niat iseng PDKT,  
> tapi semua berubah jadi **cinta pandangan pertama**.  
> Kamu membuka hatimu dengan mudahnya,  
> padahal aku sadar, tampangku biasa aja 😅  
>
> Kita dulu HTSan, dan akhirnya pada **23 Juli**,  
> kita resmi jadian... WKWKWK 😄  
>
> Sejak awal aku kenal kau, hari-hariku berubah total.  
> Dulu aku sering pulang ke kosan dengan hati kosong,  
> tapi semenjak ada kamu, hidupku jadi penuh warna. 🌈  
> Aku selalu menantikan telepon dan chat darimu,  
> aku selalu berusaha fast respon karena aku se-excited itu buat kamu. 💬💖  
>
> Aku tahu kamu kadang sibuk,  
> tapi please jangan cuek sama pesanku ya...  
> cukup kasih kabar, supaya aku gak terus merasa kecarian.  
> Kedatanganmu bener-bener bikin hidupku gak kosong lagi.  
>
> Terima kasih sudah hadir,  
> sudah nerima aku yang kadang lebay,  
> dan tetap di sini buat aku.  
> Aku ga bisa mendefenisikan seberapa besar
> rasa cintaku samamu, 
> Maafin kalau aku terlalu Bucin 
> tapi inilah diriku:)
>
> Kamu bukan cuma pacarku,  
> **kamu adalah rumah** tempat hatiku selalu pulang. 🏡❤️  
>
> Love you always,  
> **Your Lucky Boy.** 💫
""")

# Video (tanpa gambar)
video_file = open('Her.Mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
