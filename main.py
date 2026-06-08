
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time

# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")

# Wait for page to load just in case
sleep(5)

# Dismiss the language selection

# Wait for the language selection to finish
sleep(3)

# Find the big cookie to click

# Set timers
# Set time for upgrade interval
upgrade_interval = 5
upgrade_time = time.time() + upgrade_interval

# Set time to stop program execution
stop_time = time.time() + 300


# Click to the big cookie constantly for 5 minutes   by using a while loop
    # Every 5 seconds (time.time()>=upgrade_time), try to buy the most expensive item we can afford
    # If enabled products exists, click on all enabled product starting from the last item (most expensive).
      # Technically, more expensive item can appear earlier in the list but
      # that's unlikely based on the bot executes its logic.
      # Reset upgrade interval
    # Stop program execution

# Print out cookies per second

# uncomment after you see the code works
# driver.quit()




