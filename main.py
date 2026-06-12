
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time
from selenium.common.exceptions import NoSuchElementException

# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")

# Wait for page to load just in case
sleep(5)

# Dismiss the language selection
# id="langSelect-EN"
try:
    language_button = driver.find_element(By.ID, value="langSelect-EN")
    # print(language_button.text)
    language_button.click()
    # Wait for the language selection to finish
    sleep(3)
except NoSuchElementException:
    print("Language selection not found")

# Find the big cookie to click
# <button id="bigCookie"></button>
big_cookie_button = driver.find_element(By.ID, value="bigCookie")
# print(big_cookie_button)


# Set timers
# print(time())
# Set time for upgrade interval
upgrade_interval = 5
upgrade_time = time() + upgrade_interval
# print(upgrade_time)

# Set time to stop program execution
stop_time = time() + 300
# print(stop_time)

# Click to the big cookie constantly for 5 minutes   by using a while loop
#CONTINUE FROM HERE:

while True:
    big_cookie_button.click()
    # Every 5 seconds (time.time()>=upgrade_time), try to buy the most expensive item we can afford
    if time() >= upgrade_time:
#         # Get all enabled products
#         #  use driver.find_elements here
#         # < div class ="product unlocked enabled" onmouseout="Game.tooltip.shouldHide=1;" onmouseover="Game.tooltip.dynamic=1;Game.tooltip.draw(this,function(){return Game.ObjectsById[5].tooltip();},'store');Game.tooltip.wobble();" id="product5" > < div class ="icon off" id="productIconOff5" style="background-position: -64px -384px;" > < / div > < div class ="icon" id="productIcon5" style="background-position: 0px -384px;" > < / div > < div class ="content" > < div class ="lockedTitle" > ??? < / div > < div class ="title productName" id="productName5" > Bank < / div > < span class ="priceMult" id="productPriceMult5" > < / span > < span class ="price" id="productPrice5" > 1.61 million < / span > < div class ="title owned" id="productOwned5" > 1 < / div > < / div > < / div >
#         # class ="product unlocked enabled"
        products = driver.find_elements(By.CSS_SELECTOR, "#products .product.enabled")
        print(products)



#         # If enabled products exists, click on all enabled product starting from the last item (most expensive).
#         # Technically, more expensive item can appear earlier in the list but
#         # that's unlikely based on the bot executes its logic.
        if products:
            b = products[len(products) - 1]
            b.click()

        # Reset upgrade interval
        upgrade_time = time() + upgrade_interval
        print(upgrade_time)

    # Stop program execution
    if time() >= stop_time:
        break

# Print out cookies per second
cookies_per_second = driver.find_element(By.ID, value="cookiesPerSecond")
# print(cookies_per_second.text)

# uncomment after you see the code works
# driver.quit()






