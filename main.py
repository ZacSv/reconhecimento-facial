import cv2
import face_recognition as fr
import os
import shutil

img_base = fr.load_image_file('123456.jpg')
img_base = cv2.cvtColor(img_base, cv2.COLOR_BGR2RGB)
faceLoc = fr.face_locations(img_base)[0]
encodeBase = fr.face_encodings(img_base)[0]


directory_base = 'C:/Users/isacv/OneDrive/Área de Trabalho/Teste'
directory_dest = 'C:/Users/isacv/OneDrive/Área de Trabalho/fotos-mae'

#Percorre diretório raiz
for pic_name in os.listdir(directory_base):
    pic_in_path = os.path.join(directory_base, pic_name)
    # Carrega a foto para o Fr
    pic_act = fr.load_image_file(pic_in_path)

    # Codifica o rosto atual
    try:
        pic_act_encode = fr.face_encodings(pic_act)[0]
    except IndexError:
        print('I not find a face')
        continue

    compare_pic = fr.compare_faces([encodeBase], pic_act_encode)

    if compare_pic[0]:
        shutil.move(pic_in_path, directory_dest)
        print('Picture moved')
    else:
        print('Foto não corresponde a base')
cv2.waitKey(0)
