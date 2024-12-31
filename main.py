import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = r"D:\Workspace\Python\chromedriver.exe"

# Cấu hình tài khoản
accounts = [
    {
        "name": "thanhgiangbmt",
        "chrome_path": "D:\\Accounts\\Facebook Accounts\\thanhgiangbmt\\GoogleChromePortable\\GoogleChromePortable.exe",
        "user_data_dir": "D:\\Accounts\\Facebook Accounts\\thanhgiangbmt\\GoogleChromePortable\\Data\\profile\\Default",
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

def replace_non_bmp_chars_with_placeholder(text):
    # Thay thế các ký tự ngoài BMP bằng một placeholder hoặc chuỗi rỗng
    return re.sub(r'[^\u0000-\uFFFF]', '', text)  # Loại bỏ non-BMP characters

def perform_task(account):
    print(f"Bắt đầu spam bằng tài khoản: {account['name']}")
    driver = init_driver(account)

    try:
        # Mở trang tìm kiếm nhóm Facebook
        driver.get("https://www.facebook.com/search/groups/?q=digital%20marketing")
        time.sleep(5) 

        # Scroll 700px mỗi 5s, lặp lại 10 lần
        for i in range(10):
            print("Scroll để lấy thêm danh sách nhóm")
            driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(5)  

        # Tìm tất cả các thẻ <a> với class xác định
        group_links = driver.find_elements(By.CSS_SELECTOR, "a.x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1sur9pj.xkrqix3.xzsf02u.x1pd3egz")
        
        print(f"Tìm thấy {len(group_links)} nhóm.")
        
        for idx, link in enumerate(group_links):
            # Lấy URL của thẻ <a>
            group_url = link.get_attribute("href")
            print(f"Nhóm {idx + 1}: {group_url}")
            
            # Mở URL trong tab mới
            driver.execute_script("window.open(arguments[0], '_blank');", group_url)
            driver.switch_to.window(driver.window_handles[-1])  # Chuyển sang tab mới
            time.sleep(5)  # Đợi trang nhóm tải

            try:
                # Tìm và nhấp vào div để mở form đăng bài
                post_button = driver.find_element(By.CSS_SELECTOR, "div.xi81zsa.x1lkfr7t.xkjl1po.x1mzt3pk.xh8yej3.x13faqbe")
                post_button.click()
                time.sleep(5)  # Đợi form đăng bài hiện lên

                # Tìm form nhập nội dung bằng contenteditable="true" và aria-describedby="placeholder-7qpiq"
                content_box = driver.find_element(By.XPATH, '//div[@contenteditable="true" and @aria-label="Tạo bài viết công khai..."]')
                content_box.click()
                time.sleep(2)

                # Nội dung bài viết với ký tự thay thế
                post_content = """
VỊ TRÍ TUYỂN DỤNG: CHUYÊN VIÊN Digital MARKETING tại Công ty TNHH GNF-JAPAN

Địa điểm: 
• Số 9/3 Đường Nguyễn Trường Tộ, Phường Eatam, Thành phố Buôn Ma Thuột, Tỉnh Đắk Lắk

Nhiệm vụ chính:
• Xác định và phát triển các ý tưởng mới cho chiến lược marketing.
• Phát triển và triển khai các chiến lược marketing toàn diện.
• Tạo và quản lý nội dung marketing mới bao gồm video, bài đăng, story, blog, v.v.
• Thực hiện nghiên cứu thị trường.
• Giám sát và đánh giá hiệu quả của các hoạt động marketing.
• Phân tích dữ liệu và báo cáo kết quả hiệu suất marketing hàng ngày.
• Quản lý và tối ưu hóa các chiến dịch quảng cáo trực tuyến.
• Tối ưu hóa công cụ tìm kiếm (SEO) cho website.
• Tối ưu hóa công cụ tìm kiếm (SEO) cho kênh YouTube, Facebook, TikTok, LinkedIn.
• Quản lý nội dung và tương tác trên các nền tảng mạng xã hội.
• Phân tích lưu lượng truy cập website và hành vi người dùng trên GMAJOR.

Yêu cầu:
• Tối thiểu 2 năm kinh nghiệm trong lĩnh vực Marketing Số.
• Kỹ năng giao tiếp tiếng Anh tốt.
• Hiểu biết về Môi trường Khởi nghiệp.

Quyền lợi:
• Mức lương: Thương lượng, phù hợp với kỹ năng và kinh nghiệm.
• Bảo hiểm xã hội và bảo hiểm y tế theo quy định của công ty.
• Làm việc 5 ngày/tuần.
• Môi trường làm việc chuyên nghiệp, năng động và sáng tạo.
• Cơ hội thăng tiến và phát triển sự nghiệp.
• Cách thức ứng tuyển: Ứng viên quan tâm vui lòng gửi CV và thư xin việc tới email: info@gnf-japan.com hoặc liên hệ số điện thoại: 0363003831 để biết thêm chi tiết.

Chúng tôi mong được hợp tác với các ứng viên tài năng và đam mê. Tham gia GNF-JAPAN để xây dựng các chiến dịch marketing đột phá và đạt được những thành công mới cùng nhau!
                """
                processed_content = replace_non_bmp_chars_with_placeholder(post_content)
                content_box.send_keys(processed_content)

                # Tìm và click nút đăng bài
                try:
                    # Tìm thẻ div có class xác định và aria-label="Đăng"
                    post_button = driver.find_element(By.XPATH, '//div[contains(@class, "x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz x9f619 x3nfvp2 xdt5ytf xl56j7k x1n2onr6 xh8yej3") and @aria-label="Đăng"]')
                    post_button.click()
                    print("Đã nhấn nút Đăng.")
                    time.sleep(20)  # Chờ bài đăng được xử lý
                except Exception as e:
                    print(f"Lỗi khi nhấn nút Đăng: {e}")
            
            except Exception as e:
                print(f"Lỗi khi đăng bài trong nhóm: {e}")
            
            finally:
                driver.close()  # Đóng tab hiện tại
                driver.switch_to.window(driver.window_handles[0])  # Quay lại tab chính
    
    except Exception as e:
        print(f"Lỗi trong quá trình thực thi: {e}")
    
    finally:
        print(f"Nuôi xong tài khoản: {account['name']}")
        driver.quit()
        print("Driver đã đóng.")

# Thực thi
for account in accounts:
    perform_task(account)