import os
import time


def take_screenshot(driver, test_name):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_name = f"screenshots/{test_name}_{timestamp}.png"

    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot(screenshot_name)

    return screenshot_name
