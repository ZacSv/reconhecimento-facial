import cv2
import face_recognition as fr
import os
import shutil

img_base = fr.load_image_file('123456.jpg')# Carregue sua foto base para o reconhecimento
img_base = cv2.cvtColor(img_base, cv2.COLOR_BGR2RGB)
faceLoc = fr.face_locations(img_base)[0]
encodeBase = fr.face_encodings(img_base)[0]


directory_base = 'C:/Users/isacv/OneDrive/Área de Trabalho/Teste'# Diretorio origem que o algoritimo ira percorrer
directory_dest = 'C:/Users/isacv/OneDrive/Área de Trabalho/fotos-mae' # Diretorio para qual as fotos  compatíveis com a base serão enviadas
count = 0

#Percorre diretório raiz
for pic_name in os.listdir(directory_base):
    pic_in_path = os.path.join(directory_base, pic_name)
    # Carrega a foto para o Fr
    pic_act = fr.load_image_file(pic_in_path)

    # Codifica o rosto atual
    try:
        pic_act_encode = fr.face_encodings(pic_act)[0]
    except IndexError:
        print('Não consegui localizar um rosto')
        continue

    compare_pic = fr.compare_faces([encodeBase], pic_act_encode) #Compara a foto atual com a foto base

    if compare_pic[0]: #Se p resultado da comparação acima retornar "true", move a foto para o novo diretorio
        shutil.move(pic_in_path, directory_dest)
        print('Foto compatível, movendo para o novo diretório...')
    else:
        print('Foto não corresponde a base')

    count += 1
    print(str(count) + " foto(s) analizada(s)")


cv2.waitKey(0)
