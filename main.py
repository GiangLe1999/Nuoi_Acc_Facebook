import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Cấu hình tài khoản
accounts = [
    {
        "name": "D17CQQT01",
        "chrome_path": "C:\\Others\\Facebook Accounts\\n17dcqt014\\GoogleChromePortable\\GoogleChromePortable.exe",
        "user_data_dir": "C:\\Others\\Facebook Accounts\\n17dcqt014\\GoogleChromePortable\\Data\\profile\\Default",
    },
]

# Cấu hình driver
def init_driver(account):
    options = webdriver.ChromeOptions()
    options.binary_location = account["chrome_path"]
    options.add_argument(f"--user-data-dir={account['user_data_dir']}")  # Thư mục dữ liệu riêng
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument(f"--remote-debugging-port=9300")  # Cổng Debug riêng

    # Sử dụng webdriver-manager để tự động tải ChromeDriver
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

# Scroll trang web
def scroll_page(driver, pixels, interval, duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        driver.execute_script(f"window.scrollBy(0, {pixels});")
        time.sleep(interval)

# Tìm và click vào thẻ div
def click_second_button(driver):
    try:
        # Tìm tất cả các thẻ div với class yêu cầu
        divs = driver.find_elements(By.CLASS_NAME, "x14yjl9h.xudhj91.x18nykt9.xww2gxu.x1iorvi4.x150jy0e.xjkvuk6.x1e558r4.x1a2a7pz")
        buttons = divs[1].find_elements(By.TAG_NAME, "button")
        buttons[1].click()
        print("Clicked the second button in the second div.")
    except Exception as e:
        print(f"Error during button click: {e}")
        pass

# Vòng lặp chính
def perform_task(account):
    print(f"Initializing task for account: {account['name']}")
    driver = init_driver(account)

    try:
        # Truy cập Facebook
        driver.get("https://www.facebook.com/")
        scroll_page(driver, 700, 30, 5 * 60)  # Scroll mỗi 30s trong 5 phút

        # Truy cập Facebook Watch
        driver.get("https://www.facebook.com/watch")
        scroll_page(driver, 700, 60, 5 * 60)  # Scroll mỗi 1 phút trong 5 phút

        # Truy cập Facebook Live Watch
        driver.get("https://www.facebook.com/watch/live/?ref=watch")
        scroll_page(driver, 700, 60, 5 * 60)  # Scroll mỗi 1 phút trong 5 phút

        # Truy cập Facebook Reel
        driver.get("https://www.facebook.com/reel/")
        start_time = time.time()
        while time.time() - start_time < 5 * 60:  # Trong 5 phút
            time.sleep(50)  # Chờ 50 giây
            click_second_button(driver)  # Click vào nút thứ 2 trong thẻ div phù hợp
    except Exception as e:
        print(f"Error during task: {e}")
    finally:
        driver.quit()
        print("Driver closed.")

# Thực thi
for account in accounts:
    perform_task(account)
