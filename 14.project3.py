#import modul
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def kirim_email(pengirim, penerima, subject, html_content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(pengirim, 'cbqr tqjv powl vtgj')
    
    msg = MIMEMultipart()
    msg['From'] = pengirim
    msg['To'] = penerima
    msg['Subject'] = subject
    
    msg.attach(MIMEText(html_content, 'html'))
    server.send_message(msg)
    server.quit()

html_template = """
<html>
<head>
    <title>Sistem Email Otomatis</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            color: #333;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            width: 100%;
            max-width: 600px;
            margin:0 auto;
            background-color: #fff;
            padding: 20px;
            border_radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border: ipx solid #ddd;
        }
        h1 {
            font-size: 24px;
            color: #333;
            margin-bottom: 10px;
            text-align: center;
        }
        hr {
            border: 0;
            border-top: 1px solid #ddd;
            margin: 20px 0;
            }
        p {
            font-size: 16px;
            line-height: 1.5;
            margin: 0 0 20px;
        }
        .button-container {
            text-align: center;
            margin-top: 20px;
        }
        .button-container a {
            color: white;
        }
        .button {
            background-color: #6a0dad;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            font-size: 16px;
            display: inline-block;
        }
        .button:hover {
            background-color: #5a0bb5;
        }
        .footer {
            font-size: 14px;
            color: #888;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head >
<body>
    <div class="container">
        <h1>MENCOBA SISTEM EMAIL OTOMATIS</h1>
        <p>Sistem emal otomatis memudahkan pengirim pesan secara efisien dan terjadwal Kita bisa mendapatkan notifikasi otomatis dan hemat waktu dengan fitur fitur canggih</p>
        <p>keuntungan sistem ini termasuk penghematan waktu, pengurangan kesalahan manual, dan memudahkan penjadwalan email</p>
        <div class="button-container">
            <a href = "#" class="button">pelajari lebih lanjut</a>
        </div>
        <div class="footer">
        &copy; 2024 Hak cipta dilindungi.
        </div>
    </div>
</body>
</html>
"""

pengirim = 'akhdanrafa840@gmail.com'
penerima = 'sadiyah.rpl@gmail.com'
subject = 'Surat otomatis dari sistem kami'
kirim_email(pengirim, penerima, subject, html_template)
print('email berhasil dikirim!!')