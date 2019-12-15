# pip install pytelegrambotapi
# pip install requests
import os
import requests
import telebot
import smtplib
import json
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

bot = telebot.TeleBot('1060156598:AAFIcHk7n6Qwc1wgalBhBz1eX3UE2jvL8hY')

def save_bytes_to_image(bytes_array, filepath="passport.png"):
  with open(filepath, "wb") as f:
    f.write(bytes_array)
  return filepath

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
  # try:
  file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
  print(file_info)
  image = bot.download_file(file_info.file_path)
  image_path = save_bytes_to_image(image)

  # get user input
  # input sender email address and password:
  from_addr = 'govrie_bot@mail.ru'  #insert your real e-mail address in mail-ru
  password = 'XXX' #insert your real password for from_addr
  # input receiver email address.
  to_addr = 'baishevgavriil@mail.ru'  #insert your real e-mail address in mail-ru
  # input smtp server ip address:
  smtp_server = smtplib.SMTP_SSL('smtp.mail.ru', 465)

  # email object that has multiple part:
  msg = MIMEMultipart()
  msg['From'] = from_addr
  msg['To'] = to_addr
  msg['Subject'] = 'message subject'

  # attache a MIMEText object to save email content
  msg_content = MIMEText('send with attachment...', 'plain', 'utf-8')
  msg.attach(msg_content)

  # to add an attachment is just add a MIMEBase object to read a picture locally.
  filepath = image_path
  f = open(filepath, mode = 'r')
  print('downloaded_file open!!!')
  # set attachment mime and file name, the image type is png
  mime = MIMEBase('image', 'png', filename='img1.png')
  print('downloaded_file')
  # add required header data:
  mime.add_header('Content-Disposition', 'attachment', filename='img1.png')
  mime.add_header('X-Attachment-Id', '0')
  mime.add_header('Content-ID', '<0>')
  # read attachment file content into the MIMEBase object
  mime.set_payload(image)
  # encode with base64
  encoders.encode_base64(mime)
  # add MIMEBase object to MIMEMultipart object
  msg.attach(mime)
  bot.reply_to(message,"Фото добавлено")
  print("we here")

  smtp_server.set_debuglevel(1)
  smtp_server.login(from_addr, password)
  smtp_server.sendmail(from_addr, [to_addr], msg.as_string())
  smtp_server.quit()

bot.polling(none_stop=True, interval=0)
