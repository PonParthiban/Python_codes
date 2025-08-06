import imageio as iio
import os

def get_image():
 filenames = []
 print("Enter the image filenames(press enter to finish)")
 
 while True:
   filename = input("Image file: ").strip()

   if os.path.exists(filename):
      filenames.append(filename)
      print("File appended")
   else:
       print("file not found")
       retry = input("Do you want to retry(y/n): ").lower
       if retry != 'y':
          continue
 return filenames

def get_gifsettings():
  gif_name = input("Enter the output Gif name(default:Output.gif): ").strip()
  if not gif_name:
     gif_name = "Output.gif"
   
  if not gif_name.endswith('.gif'):
     gif_name += '.gif'
    
  try:
        duration = int(input("Enter frame duration in milliseconds (default: 500): "))
  except ValueError:
        duration = 500
 
  return duration, gif_name
    
def main():
   print("-------Gif Maker---------")
   filenames = get_image()

   if(len(filenames) < 2):
      print("Atleast need two images to make a gif!")
      return
   duration,gif_name = get_gifsettings()

   print("\n Loading Image")
   images = []
   for filename in filenames:
      try:
         images.append(iio.imread(filename))
         print("Image Loaded")
      except:
         print("Error Loading")
    
   if not images:
      print("Image not Loaded sucessfully")
      return
   
   print(f"\nCreating GIF: {gif_name}")
  
   try:
        iio.imwrite(gif_name, images, duration=duration, loop=0)
        print(f"✅ GIF created successfully: {gif_name}")
   except Exception as e:
        print(f"❌ Error creating GIF: {e}")

if __name__ == "__main__":
    main()

    