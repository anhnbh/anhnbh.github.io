Hanwha Life Vietnam – Meeting Notes (Day 1)

I. Thành phần tham gia
* Security HWL
* System HWL
* Admin HWL
* Network HWL
* AWS
* G-AsiaPacific
II. Requirements / Thu thập yêu cầu
1. Assessment – Hiện trạng On-prem
* Networking & VLAN:
    * Core được bảo vệ bởi Firewall, nhiều subnet khác nhau.
    * App network cũng tách subnet riêng, được bảo vệ bởi Firewall riêng.
    * Một số vùng:
        * Vùng DMZ
        * Vùng user external
        * Vùng web internal
    * Web public: WAF + F5
    * Firewall: nội bộ dùng firewall riêng, bên ngoài dùng Checkpoint
    * Có Palo Alto, Salesforce
    * Networking theo chuẩn Cisco
    * Internet thực tế: 5Mb quốc tế, đang dùng ~100Mb
    * ISP có đường TBCO
    * VPN: GlobalProtect NAT ra ngoài (chỉ Client-to-Site, chưa có Site-to-Site)
* Môi trường hiện tại:
    * Tổng 9 môi trường → HWL thống nhất rút còn 3 (Prod, Pre-Prod/UAT, Non-Prod).
    * CIDR hiện tại: 10.84.0.0/16 (không overlap).
    * Prod + Staging + UAT tách theo CIDR chung.
* Về VPN/Connectivity:
    * Chưa có Site-to-Site VPN.
    * Cần đánh giá khả năng:
        * Point-to-Point
        * Tích hợp Salesforce
        * Sử dụng Palo Alto
* Load Balancer:
    * F5 có rule tự viết và tuning.
    * Hỏi: Rule hiện tại có thể migrate lên AWS WAF/ALB không?
    * Không có giải pháp LB đồng nhất trên F5 — một số app dùng Nginx.
2. DNS & Certificate
* DNS nội bộ chạy trên Windows Server:
    * 3 DNS servers → 2 DC active + 1 DR standby
* Domain internal: korealife.com.vn
* Domain app mới: hanwhalife.com.vn
* Certificate: mua wildcard cho public & private.
* Plan: dựng DNS server replica trên AWS, có thể bỏ DR on-prem.
3. Identity Management
* IDP:
    * Microsoft AD SSO
    * EntraID (Azure AD)
* SAML đang dùng → tiếp tục kết nối.
* Một số app dùng Azure App Proxy → cần đánh giá cách kết nối với AWS SSO.
    * AuthN vẫn ở EntraID
    * AuthZ có thể xử lý trên AWS
* Role Based Control hiện tại vẫn giữ nguyên.

III. Infrastructure
1. Bandwidth
* Giai đoạn Go-Live sẽ cần mở thêm băng thông.
* Monitoring sẽ đưa lên AWS, có thể tận dụng hệ thống hiện tại.
* Direct Connect:
    * Cần test thêm latency.
    * Chi phí dự kiến: ~50,000 USD.
    * Giá tham khảo: ~1M VND / Mbps → 100 Mbps = ~1 tỷ VND/tháng.
    * User nội bộ 300–400 người nằm ở Singapore region (VPN/Internet access).
2. Server & CI/CD
* CI/CD:
    * Jenkins, Docker, Ansible.
    * Build cho core eBao (Dockerfile).
    * Prod: deploy manual.
    * Non-prod: full CI/CD bằng Jenkins.
* Batch jobs:
    * Chạy ở DB Layer 7 (convert image, import data, application jobs).
    * Mong muốn chuyển sang: Step Functions, SQS.
* Auth:
    * HWL đang POC Cognito.
    * App dùng OAuth2/OIDC → AuthN đưa lên Cloud, AuthZ giữ nguyên.
* Code repo: SVN + GitLab.

IV. Application
1. Ưu tiên
* eBao và toàn bộ thành phần liên quan (call in/out)
* Database:
    * DB của eBao đang được truy cập từ các app (20+ ứng dụng, 39 schema).
    * HWL sẽ cung cấp lại mapping schema.
    * DBLink nhiều và phức tạp → HWL sẽ tổng hợp lại.
→ Yêu cầu: thống kê tổng quan eBao call out + eBao receive request.
* eBao đang migration sang PostgreSQL.
2. Ứng dụng Non-core
* Chưa POC → ưu tiên hạ tầng core trước.
3. Deploy eBao lên AWS
* Mong muốn chạy bằng container (hiện legacy Java 8).
* Giữ nguyên version để đảm bảo ổn định.
* HWL sẽ chọn 1 API để thử nghiệm estimate thời gian migrate.
4. Workstreams
* Infra
* Application (Non-Core)
5. POC ứng dụng đầu tiên
* Claim Workflow Web
* Tiêu chí: không phụ thuộc DBLink phức tạp.

V. AWS Landing Zone & Security
1. EKS (Chuẩn bị thêm thông tin)
* Jobs hiện tại:
    * 15–30s
    * Một số jobs 30–45 phút
* Có thể chạy:
    * EKS
    * Step Function / Lambda
2. Account Structure & Governance
* Tách account theo:
    * Core apps
    * Apps chứa dữ liệu khách hàng
    * Phân theo employee/business
* Tagging & naming convention để quản lý chi phí.
3. Security Compliance
* Theo nghị định nhà nước – tài liệu HWL đã gửi.
* Không expose API ra ngoài → không yêu cầu PCI/CIS bắt buộc.
* Hardening:
    * Dùng image chuẩn, scan hàng tháng.
    * Tools: Graciven.
    * Vừa script vừa manual.
    * Không dùng Packer.
* SIEM:
    * 200GB/month log (system + audit).
    * Câu hỏi: Có centralize logs về AWS không?
        * Có thể dùng OpenSearch.
* Logging / Monitoring:
    * Syslog → CloudWatch
    * App logs → Grafana/Prometheus/Loki hoặc EFK
* Patching:
    * Ansible, không có logs patching.
    * Recommend: AWS SSM Patch Manager.
4. Secrets & Encryption
* On-prem dùng Vault → Cloud dùng:
    * AWS KMS
    * Secrets Manager
* Cần đánh giá performance.
5. Retention / Archive
* Logs retain 1 năm → archive theo chính sách.
* Backup logs theo yêu cầu 20 năm.
6. WAF / Shield
* AWS WAF: đầy đủ basic rules.
* HWL có nhiều custom rule → cần extract để mapping.
* Shield Advanced: 3,000 USD/tháng.
7. OU review
* Cần list team IT quản trị.
* PAM đang POC → recommend BeyondTrust Record Session.
8. Application scanning
* Có cần SAST/DAST? (HWL hỏi)
* Hiện chưa support file-scan khi download/upload.
    * Nếu đi qua S3 → dùng PrivateLink hoặc Palo Alto để scan.

VI. DR Strategy
* Hai phương án:
    1. DR trên Cloud (đa AZ hoặc multi-region)
    2. DR xuống On-prem
* Test:
    * Tắt 1 AZ → verify HA
    * Region failover demo
Serverless DR
* CI/CD cần mô tả cách deploy serverless.

VII. Backup Strategy
* Weekly: full backup
* Daily: retention 3 days
* Backup instance + DB bằng AWS Backup.
* Tuân theo NHNN: dump data rồi restore lại on-prem để chứng minh.
* Upload file staging zone:
    * Cần cơ chế "tạm upload" trước khi finalize → trigger automation.
* Kiểm tra DMS cho backup replicate.
Email Notification
* AWS SNS cho ứng dụng, chăm sóc khách hàng.
* Lo ngại domain bị đánh giá spam.
* Mong muốn migrate mail marketing lên cloud.
    * Sử dụng domain riêng cho marketing.
Alerting
* Sử dụng SNS alerts.

VIII. Observability
* Hiện tại:
    * Logs: Grafana / Prometheus
    * Network monitor: CheckMK
    * Chưa có Application Performance Monitoring
    * Kubernetes mới có Non-prod, chưa có Prod
Yêu cầu
* Design solution cho:
    * Observability
    * Monitoring
    * Tracing

✔ Summary
* Tập trung trước vào hạ tầng Core + eBao.
* POC ứng dụng đầu tiên: Claim Workflow Web.
* HWL sẽ cung cấp:
    * DBLink mapping
    * Custom WAF rules
    * SIEM version
    * API mẫu để estimate migrate
* Tiếp tục phân tích LZ, Security, EKS, Account structure.
