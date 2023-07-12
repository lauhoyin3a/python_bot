import pyautogui
import time
from PIL import Image, ImageChops

timer_top_left_x = 1780
timer_top_left_y = 272
timer_bottom_right_x = 1850
timer_bottom_right_y = 290

timer_image_path = "C:/Users/user/Downloads/cheat/compare.png"
timer_image = Image.open(timer_image_path)
timer_image = timer_image.convert('L')

print(timer_image_path)
while True:
    # Capture a screenshot of the timer area
    timer_screenshot = pyautogui.screenshot(region=(timer_top_left_x, timer_top_left_y, timer_bottom_right_x - timer_top_left_x, timer_bottom_right_y - timer_top_left_y))
    timer_screenshot=timer_screenshot.convert('L')
    timer_screenshot.save('temp.png')
    timer_screenshot.save('compare.png')
    print('temp.png')
    time.sleep(2)
    # Calculate the difference between the screenshot and the reference image
    diff = ImageChops.difference(timer_screenshot, timer_image)
    
    # Get the bounding box of the non-zero regions in the difference image
    bbox = diff.getbbox()

    # If the bounding box is empty, the two images are identical
    if not bbox:
        print('Game started')
        
    else:
        print('game started')
        # Update the reference image
        timer_image = timer_screenshot.copy()
        

    area = (timer_bottom_right_x - timer_top_left_x) * (timer_bottom_right_y - timer_top_left_y)
    similarity = (area - diff.crop(bbox).getbbox()[2] * diff.crop(bbox).getbbox()[3]) / area * 100
    print(f"Similarity percentage: {similarity:.2f}%")
   

    # Wait for a short period before checking again
    time.sleep(1)