> **Xem video demo tại đây: [Video demo](https://record-project.s3.ap-southeast-2.amazonaws.com/crawl-demo.mp4)**

 # Giới thiệu project
Dự án được thực hiện dựa trên yêu cầu của team marketing về một Graphical User Interface cho phép người dùng tìm kiếm, cào, tạo mới, đăng tải bài viết thuộc chủ đề dược phẩm. 
> **Xem video demo tại đây: [Video demo](https://record-project.s3.ap-southeast-2.amazonaws.com/crawl-demo.mp4)**

Ban đầu, dự án tiếp nhận ba yêu cầu về tính năng sản phẩm: Cào bài viết, Tạo mới bài viết, Đăng tải bài viết.

- **Tính năng 1 - Cào bài viết:** Thực hiện sử dụng thư viện scrapy trong python.
- **Tính năng 2 - Tạo mới bài viết:** Thực hiện sử dụng api của OpenAI. Sau đó yêu cầu này được hủy bỏ vì chi phí token không nhỏ. 
- **Tính năng 3 - Đăng tải bài viết:** Thực hiện sử dụng api của Wordpress vì website được đăng tải là wordpress-based.

# Giá trị đóng góp cho người dùng
- **Tiết kiệm thời gian thu thập văn bản bài viết:** Công việc tìm kiếm, copy các bài viết với chủ đề dược từ các website uy tín được thực hiện thường xuyên. Công cụ này giúp họ lưu trữ văn bản của một lượng lớn bài viết trong thời gian nhanh chóng. Các văn bản này sau đó có thể được copy paste vào UI của chatgpt để sáng tạo nội dung mới.
- **Cung cấp prompt giúp chatgpt sáng tạo nội dung hiệu quả:** Một trong các yêu cầu ban đầu của tool là sử dụng openai api để sáng tạo nội dung. Trước khi yêu cầu bị hủy, công đoạn prompt engineering đã được thực hiện. Trong source code (executors/generator.py) chứa prompt step-by-step để chatgpt đưa ra văn bản mới một cách hiệu quả. Tool này có thể được tiếp tục sử dụng sau này nếu chi phí token được cung cấp, hoặc sử dụng prompt trực tiếp trên UI của chatgpt.
- **Tiết kiệm thời gian đăng tải hàng loạt bài viết:** Người dùng có thể đăng tải cùng một lúc một số lượng lớn bài viết thông qua api của Wordpress.        
