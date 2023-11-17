def meal_time(time):
  a, b = time.split(":")
  total = int(a)*60 + int(b) 
  if total <= 480 and total >= 420:
    return "breakfast"
  elif total <= 780 and total >= 720:
    return "lunch"
  elif total <= 1140 and total >= 1080:
    return "dinner"
  else:
    return "nothing right now"
  
def get_filename_extension(filename):
  file, extention = filename.split(".")
  return extention

def is_image_file(filename):
  type = get_filename_extension(filename)
  if type == "jpeg" or type == "jpg" or type == "png" or type == "gif" or type == "tiff":
    return True
  else:
    return False