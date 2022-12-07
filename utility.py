import cv2
import numpy as np
import constants as const

def process_image(image):
    file = "static/uploads/" + image
    print(file, "\n\n\n\n\n")
    z = cv2.imread(file)
    k = cv2.resize(z,(67,48))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    INPUT_IMAGE = np.array(k)
    INPUT_IMAGE_F = INPUT_IMAGE.flatten()
    Hue_value1=[]
    Sat_value1=[]
    Val_value1=[]
    Hue_value1.append(INPUT_IMAGE_F[0::3])
    Sat_value1.append(INPUT_IMAGE_F[1::3])
    Val_value1.append(INPUT_IMAGE_F[2::3])
    const.Hue_value = np.array(Hue_value1)
    const.Sat_value = np.array(Sat_value1)
    const.Val_value = np.array(Val_value1)

def isPorcelain(image):
    process_image(image)
    Porcelian_Range_H1=0
    x111=0
    x1=[]
    for m in const.Porcelian_Range_H:
        x1=np.where(const.Hue_value==m)
        x11=np.array(x1)
        z11=x11.size
        if z11>1:
            x111+=1
        if (x111==4):
            Porcelian_Range_H1+=4

    x222=0
    x2=[]
    for m in const.Porcelian_Range_S:
        x2=np.where(const.Sat_value==m)
        x22=np.array(x2)
        z22=x22.size
        if z22>1:
            x222+=1
        if (x222==31):
            Porcelian_Range_H1+=31    

    x333=0
    x3=[]
    for m in const.Porcelian_Range_V:
        x3=np.where(const.Val_value==m)
        x33=np.array(x3)
        z33=x33.size
        if z33>1:
            x333+=1    
        if (x333==33):
            Porcelian_Range_H1+=33

    print(Porcelian_Range_H1)        
            
    if Porcelian_Range_H1==68:
       return "Porcelian"
    return isIvoryNuetral(image)

def isIvoryNuetral(image):
    ivory_neutral_Range_H1=0
    process_image(image)
    x111=0
    x1=[]
    for m in const.ivory_neutral_Range_H:
        x1=np.where(const.Hue_value==m)
        x11=np.array(x1)
        z11=x11.size
        if z11>1:
            x111+=1   
        if (x111==2):
            ivory_neutral_Range_H1+=2

    x222=0
    x2=[]
    for m in const.ivory_neutral_Range_S:
        x2=np.where(const.Sat_value==m)
        x22=np.array(x2)
        z22=x22.size
        if z22>1:
            x222+=1   
        if (x222==21):
            ivory_neutral_Range_H1+=21    
    x333=0
    x3=[]
    for m in const.ivory_neutral_Range_V:
        x3=np.where(const.Val_value==m)
        x33=np.array(x3)
        z33=x33.size
        if z33>1:
            x333+=1
        if (x333==34):
            ivory_neutral_Range_H1+=34

            
    print(ivory_neutral_Range_H1)        
            
    if ivory_neutral_Range_H1==57:
        return("ivory_neutral")
    return isIvoryWarm(image)
        
def isIvoryWarm(image):
    process_image(image)
    warm_ivory_Range_H1=0
    x111=0
    x1=[]
    for m in const.warm_ivory_Range_H:
        x1=np.where(const.Hue_value==m)
        x11=np.array(x1)
        z11=x11.size
        if z11>1:
            x111+=1   
        if (x111==3):
            warm_ivory_Range_H1+=3
    x222=0
    x2=[]
    for m in const.warm_ivory_Range_S:
        x2=np.where(const.Sat_value==m)
        x22=np.array(x2)
        z22=x22.size
        if z22>1:
            x222+=1   
        if (x222==16):
            warm_ivory_Range_H1+=16    
    x333=0
    x3=[]
    for m in const.warm_ivory_Range_V:
        x3=np.where(const.Val_value==m)
        x33=np.array(x3)
        z33=x33.size
        if z33>1:
            x333+=1
        if (x333==16):
            warm_ivory_Range_H1+=16

            
    print(warm_ivory_Range_H1)    

    if warm_ivory_Range_H1==35:
        return("warm ivory")
    return isSandIvory(image)  

def isSandIvory(image):
  sand_neutral_Range_H1=0
  x111=0
  x1=[]
  for m in const.sand_neutral_Range_H:
      x1=np.where(const.Hue_value==m)
      x11=np.array(x1)
      z11=x11.size
      if z11>1:
          x111+=1   
      if (x111==2):
          sand_neutral_Range_H1+=2

  x222=0
  x2=[]
  for m in const.sand_neutral_Range_S:
      x2=np.where(const.Sat_value==m)
      x22=np.array(x2)
      z22=x22.size
      if z22>1:
          x222+=1   
      if (x222==13):
          sand_neutral_Range_H1+=13    
  x333=0
  x3=[]
  for m in const.sand_neutral_Range_V:
      x3=np.where(const.Val_value==m)
      x33=np.array(x3)
      z33=x33.size
      if z33>1:
          x333+=1
      if (x333==23):
          sand_neutral_Range_H1+=23

          
  print(sand_neutral_Range_H1)        
          
  if sand_neutral_Range_H1==38:
      return("sand neutral Range")
  return isBeigeWarm(image)

def isBeigeWarm(image):
  beige__warm_beige_Range_H1=0


  x111=0
  x1=[]
  for m in const.beige__warm_beige_Range_H:
      x1=np.where(const.Hue_value==m)
      x11=np.array(x1)
      z11=x11.size
      if z11>1:
          x111+=1   
      if (x111==2):
          beige__warm_beige_Range_H1+=2

  x222=0
  x2=[]
  for m in const.beige__warm_beige_Range_S:
      x2=np.where(const.Sat_value==m)
      x22=np.array(x2)
      z22=x22.size
      if z22>1:
          x222+=1   
      if (x222==28):
          beige__warm_beige_Range_H1+=28    
  x333=0
  x3=[]
  for m in const.beige__warm_beige_Range_V:
      x3=np.where(Val_value==m)
      x33=np.array(x3)
      z33=x33.size
      if z33>1:
          x333+=1
      if (x333==23):
          beige__warm_beige_Range_H1+=23

          
  print(beige__warm_beige_Range_H1)        
          
  if beige__warm_beige_Range_H1==53:
      return("warm beige")
  else:
      return("not")