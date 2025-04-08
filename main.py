import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

chrome_driver_path = r"D:\Workspace\Python\chromedriver.exe"

# Cấu hình tài khoản
accounts = [
    {
        "name": "thanhgiangbmt",
        "chrome_path": "D:\\Accounts\\Upload Video Accounts\\thanhgiangbmt\\GoogleChromePortable\\GoogleChromePortable.exe",
        "user_data_dir": "D:\\Accounts\\Upload Video Accounts\\thanhgiangbmt\\GoogleChromePortable\\Data\\profile\\Default",
    },
]

# Cấu hình driver
def init_driver(account):
    options = uc.ChromeOptions()
    options.binary_location = account["chrome_path"]
    driver = uc.Chrome(
        use_subprocess=True,
        options=options,
        version_main=131,
        user_data_dir=account["user_data_dir"]
    )
    return driver


def perform_task(account):
    print(f"Bắt đầu spam bằng tài khoản: {account['name']}")
    driver = init_driver(account)

    try:
        driver.get("https://beta.publicai.io/vote?lang=en-US")
        time.sleep(15)

        # 7️⃣ Tìm và click thẻ div có text "Go"
        go_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Go')]"))
        )
        go_button.click()
        time.sleep(2)

        while True:
            try:
                # 1️⃣ Tìm và click thẻ div có chứa text "Pts to Start"
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'text-purple-300') and contains(text(), 'Stake')]"))
                )
                element.click()
                time.sleep(2)

                # 2️⃣ Tìm và click nút play trong thẻ audio
                audio_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//audio"))
                )
                audio_button.click()
                time.sleep(5)

                # 3️⃣ Tìm và click thẻ div có class "bg-white"
                bg_white_div = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "bg-white"))
                )
                bg_white_div.click()
                time.sleep(4)

                # 4️⃣ Tìm và click thẻ div có text "Confirm"
                confirm_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Confirm')]"))
                )
                confirm_button.click()
                time.sleep(3)

                # 5️⃣ Click điểm bất kì
                confirm_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'animate-flip-in-x')]"))
                )
                confirm_button.click()
                time.sleep(3)
 
                # 6️⃣ Click vào "Next Question"
                next_question_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Next Vote')]"))
                )
                next_question_button.click()
                print("✅ Đã click 'Next Question' - Kết thúc một vòng lặp")
                time.sleep(3)

            except Exception as loop_error:
                print(f"Lỗi trong vòng lặp: {loop_error}")
                break  # Thoát vòng lặp nếu gặp lỗi

    except Exception as e:
        print(f"Lỗi trong quá trình thực thi: {e}")

    finally:
        print(f"Spam xong tài khoản: {account['name']}")
        driver.quit()
        print("Driver đã đóng.")

# Thực thi
for account in accounts:
    perform_task(account)