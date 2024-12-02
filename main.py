import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = r"C:\Workspace\Python\chromedriver.exe"

# Cấu hình tài khoản
accounts = [
    {
        "name": "legiangbmt017",
        "chrome_path": "D:\\Accounts\\Facebook Accounts\\legiangbmt017\\GoogleChromePortable\\GoogleChromePortable.exe",
        "user_data_dir": "D:\\Accounts\\Facebook Accounts\\legiangbmt017\\GoogleChromePortable\\Data\\profile\\Default",
    },
    {
        "name": "n17dcqt014",
        "chrome_path": "D:\\Accounts\\Facebook Accounts\\n17dcqt014\\GoogleChromePortable\\GoogleChromePortable.exe",
        "user_data_dir": "D:\\Accounts\\Facebook Accounts\\n17dcqt014\\GoogleChromePortable\\Data\\profile\\Default",
    },
    {
        "name": "caytienbmt05",
        "chrome_path": "D:\\Accounts\\Facebook Accounts\\caytienbmt05\\GoogleChromePortable\\GoogleChromePortable.exe",
        "user_data_dir": "D:\\Accounts\\Facebook Accounts\\caytienbmt05\\GoogleChromePortable\\Data\\profile\\Default",
    },
    {
        "name": "caytienbmt02", 
        "chrome_path": "D:\\Accounts\\Facebook Accounts\\caytienbmt02\\GoogleChromePortable\\GoogleChromePortable.exe",
        "user_data_dir": "D:\\Accounts\\Facebook Accounts\\caytienbmt02\\GoogleChromePortable\\Data\\profile\\Default",
    },
    {
        "name": "thanhtruong1691",
        "chrome_path": "D:\\Accounts\\Facebook Accounts\\thanhtruong1691\\GoogleChromePortable\\GoogleChromePortable.exe",
        "user_data_dir": "D:\\Accounts\\Facebook Accounts\\thanhtruong1691\\GoogleChromePortable\\Data\\profile\\Default",
    },
    {
        "name": "caytienbmt09",
        "chrome_path": "D:\\Accounts\\Facebook Accounts\\caytienbmt09\\GoogleChromePortable\\GoogleChromePortable.exe",
        "user_data_dir": "D:\\Accounts\\Facebook Accounts\\caytienbmt09\\GoogleChromePortable\\Data\\profile\\Default",
    },
    {
        "name": "lttskda",
        "chrome_path": "D:\\Accounts\\Facebook Accounts\\lttskda\\GoogleChromePortable\\GoogleChromePortable.exe",
        "user_data_dir": "D:\\Accounts\\Facebook Accounts\\lttskda\\GoogleChromePortable\\Data\\profile\\Default",
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
    # Có thể chạy headless, nhưng muốn reset để có thể mở GUI thì cần xóa hết Chrome session
    options.add_argument("--headless")
    options.add_argument("--disable-gpu") # Tắt GPU (tăng hiệu năng khi chạy headless)
    options.add_argument("--disablce-software-rasterizer")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-prompt-on-repost")
    options.add_argument("--disable-sync")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-translate")
    options.add_argument("--disable-hang-monitor")
    options.add_argument("--disable-client-side-phishing-detection")
    options.add_argument("--disable-component-update")
    options.add_argument("--memory-model=low")
    options.add_argument("--disable-backing-store-limit")

    # Sử dụng webdriver-manager để tự động tải ChromeDriver
    service = Service(chrome_driver_path)
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
        divs = driver.find_elements(By.XPATH, "//div[contains(@class, 'x14yjl9h xudhj91 x18nykt9 xww2gxu x1iorvi4 x150jy0e xjkvuk6 x1e558r4 x1a2a7pz')]")
        second_div = divs[1]
        second_div.click()
        print("Clicked the second button in the second div.")
    except Exception as e:
        print(f"Error during button click: {e}")
        pass

# Vòng lặp chính
def perform_task(account):
    print(f"Bắt đầu nuôi tài khoản: {account['name']}")
    driver = init_driver(account)

    try:
        # Truy cập Facebook
        driver.get("https://www.facebook.com/")
        print("Truy cập Facebook")
        random_time = random.randint(3, 7) * 60  # Random từ 5 đến 10 phút
        random_scroll_value = random.randint(200, 1000)  # Random giá trị scroll trong khoảng 50 đến 150
        scroll_page(driver, random_scroll_value, 5, random_time)  # Scroll mỗi 5s trong thời gian random

        # Truy cập Facebook Watch
        driver.get("https://www.facebook.com/watch")
        print("Truy cập Facebook Watch")
        random_time = random.randint(3, 7) * 60  # Random từ 5 đến 10 phút
        random_scroll_value = random.randint(300, 1000)  # Random giá trị scroll trong khoảng 500 đến 900
        scroll_page(driver, random_scroll_value, 60, random_time)  # Scroll mỗi 1 phút trong thời gian random

        # Truy cập Facebook Live Watch
        driver.get("https://www.facebook.com/watch/live/?ref=watch")
        print("Truy cập Facebook Live Watch")
        random_time = random.randint(3, 7) * 60  # Random từ 5 đến 10 phút
        random_scroll_value = random.randint(300, 1000)  # Random giá trị scroll trong khoảng 500 đến 900
        scroll_page(driver, random_scroll_value, 60, random_time)  # Scroll mỗi 1 phút trong thời gian random

        # Truy cập Facebook Reel
        driver.get("https://www.facebook.com/reel/")
        print("Truy cập Facebook Reel")
        random_time = random.randint(5, 15) * 60  # Random từ 5 đến 10 phút
        start_time = time.time()
        while time.time() - start_time < random_time:  # Trong thời gian random
            random_sleep = random.randint(30, 55)
            time.sleep(random_sleep)  # Chờ 50 giây
            click_second_button(driver)  # Click vào nút thứ 2 trong thẻ div phù hợp
    except Exception as e:
        print(f"Error during task: {e}")
        pass
    finally:
        print(f"Nuôi xong tài khoản: {account['name']}")
        driver.quit()
        print("Driver closed.")

# Thực thi
for account in accounts:
    perform_task(account)
