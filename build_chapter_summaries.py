"""
Generates comprehensive, bilingual (Vietnamese & English) Chapter-by-Chapter summaries
for 'Docker in Action, 2nd Edition' (Parts 1-3, Chapters 1-13), plus a clean
Table of Contents & Reading Roadmap ('00 - Mục lục & Lộ trình Đọc (Docker in Action).md').
"""

from __future__ import annotations

from pathlib import Path

VAULT_DIR = Path(r"C:\Users\hiepnc1\Documents\Obsidian Vault\Docker-in-Action-2ed")
BACKUP_DIR = Path(r"D:\hiepnc\obsidian_brain\Docker-in-Action-2ed")

ROADMAP_STEM = "00 - Mục lục & Lộ trình Đọc (Docker in Action)"
SUMMARY_STEM = "docker-in-action-2ed-Bilingual-Summary"
CANVAS_FILE = "Docker Learning Path.canvas"

CHAPTERS = [
    {
        "num": 1,
        "part": 1,
        "part_label": "Phần 1: Cô lập Tiến trình & Điện toán Độc lập Môi trường",
        "stem": "Chương 01 - Tổng quan về Docker (Welcome to Docker)",
        "title_vi": "Chương 01: Tổng quan về Docker (Welcome to Docker)",
        "summary_vi": "Giới thiệu nền tảng Docker là gì, sự khác biệt cốt lõi giữa Container và Máy ảo (VM), những bài toán kinh điển mà Docker giải quyết (xung đột thư viện, tính di động, bảo vệ máy chủ), và thời điểm nên áp dụng Docker.",
        "summary_en": "Introduces what Docker is, the fundamental difference between containers and virtual machines, core problems Docker solves (organization, portability, host protection), and when to use Docker in modern ecosystems.",
        "sections_vi": """### 1.1 Docker là gì? (What is Docker?)
* **"Hello, World" & Containers**: Docker là nền tảng đóng gói và vận hành phần mềm bên trong các **container** độc lập. Mỗi container chứa ứng dụng cùng toàn bộ thư viện, tệp cấu hình và phụ thuộc của nó.
* **Containers không phải là ảo hóa phần cứng (Containers are not virtualization)**: Khác với Máy ảo (VM) cần Hypervisor và cả một Guest OS riêng biệt (nặng hàng GB, khởi động mất hàng phút), container **chia sẻ trực tiếp nhân Linux Kernel** của máy chủ và chạy như các tiến trình user-space thông thường.
* **Chạy phần mềm cô lập & Shipping containers**: Ý tưởng của Docker lấy cảm hứng từ container vận tải tiêu chuẩn — đóng gói một lần, vận chuyển và chạy đồng nhất trên laptop cá nhân, server test, hoặc cloud production.

### 1.2 Docker giải quyết những bài toán gì?
* **Getting organized (Sắp xếp gọn gàng)**: Chấm dứt tình trạng cài đặt chồng chéo phần mềm và phụ thuộc trực tiếp lên hệ điều hành máy chủ (gây xung đột phiên bản thư viện — "Dependency Hell").
* **Improving portability (Tăng tính di động)**: Xóa bỏ câu nói kinh điển *"Trên máy tôi vẫn chạy bình thường mà!"*. Nếu chạy được trong container ở máy dev, nó sẽ chạy giống hệt trên production.
* **Protecting your computer (Bảo vệ máy tính)**: Cô lập tiến trình và giới hạn quyền hạn giúp phần mềm lỗi hoặc không đáng tin cậy khó làm hỏng hệ điều hành nền.

### 1.3 – 1.6 Vai trò, Phạm vi sử dụng & Docker CLI
* **Tại sao Docker quan trọng**: Rút ngắn thời gian triển khai từ nhiều ngày xuống vài giây, tối ưu hóa mật độ sử dụng phần cứng server.
* **Khi nào dùng Docker**: Lý tưởng cho microservices, CI/CD pipelines, môi trường phát triển đồng nhất và dịch vụ cloud; ít phù hợp hơn cho ứng dụng desktop GUI nặng hoặc hệ thống yêu cầu kernel hoàn toàn khác (ví dụ chạy nhân Windows trên Linux thuần).
* **Trợ giúp dòng lệnh (`docker help`)**: Mọi câu lệnh CLI đều theo cấu trúc `docker <nhóm_đối_tượng> <hành_động>` (ví dụ `docker container run`, `docker image ls`).""",
        "cli_table": """| Câu lệnh | Chức năng |
| :--- | :--- |
| `docker version` | Kiểm tra phiên bản Docker CLI (Client) và Docker Daemon (Server). |
| `docker info` | Xem thông tin hệ thống: số container, image, storage driver, cgroups driver. |
| `docker run hello-world` | Tải image mẫu và chạy container đầu tiên để kiểm tra cài đặt. |
| `docker help` / `docker <cmd> --help` | Tra cứu cú pháp và cờ tùy chọn trực tiếp từ CLI. |""",
        "sections_en": """### 1.1 What is Docker?
Docker packages applications and their dependencies into isolated runtime units called **containers**. Unlike VMs, containers do not emulate hardware or boot an entire guest OS; they share the host Linux kernel while keeping user-space filesystems, processes, and networks isolated.

### 1.2 Problems Solved
1. **Organization**: Eliminates host dependency clutter and version conflicts between co-located applications.
2. **Portability**: Guarantees identical runtime behavior across laptop, staging, and production servers.
3. **Host Protection**: Constrains process visibility and capabilities, shielding the host OS.

### 1.3 – 1.6 Ecosystem & CLI Help
Docker accelerates CI/CD and resource utilization, organized consistently under object-verb CLI commands (`docker <object> <verb> --help`).""",
        "takeaways_vi": """- Container nhẹ và nhanh hơn VM vì **không cần Hypervisor hay Guest OS**, mà chạy trực tiếp trên nhân hệ điều hành chủ.
- Chuẩn hóa cấu trúc giao tiếp Client-Server qua `docker` CLI gửi lệnh tới `dockerd` daemon.""",
    },
    {
        "num": 2,
        "part": 1,
        "part_label": "Phần 1: Cô lập Tiến trình & Điện toán Độc lập Môi trường",
        "stem": "Chương 02 - Chạy phần mềm trong Container (Running Software in Containers)",
        "title_vi": "Chương 02: Chạy phần mềm trong Container (Running Software in Containers)",
        "summary_vi": "Thực hành kiểm soát vòng đời container qua bài toán Website Monitor & Website Farm, hiểu PID namespace, loại bỏ xung đột định danh, xây dựng hệ thống độc lập môi trường (Read-only FS, ENV) và container bền bỉ (Restart policy, PID 1).",
        "summary_en": "Hands-on container lifecycle control: interactive vs detached execution, PID namespace isolation, eliminating metaconflicts, read-only root filesystems, environment injection, restart policies, PID 1 / init systems, and cleanup.",
        "sections_vi": """### 2.1 Kiểm soát Container: Xây dựng Website Monitor
* **Tạo và khởi chạy (`docker create`, `docker start`, `docker run`)**: Tách biệt bước chuẩn bị và bước chạy, hoặc gộp qua `docker run`. Phân biệt chạy nền (`-d` detached) cho dịch vụ web/agent và chạy tương tác (`-it`) cho công cụ dòng lệnh.
* **Liệt kê, dừng, khởi động lại & xem log**: Theo dõi trạng thái bằng `docker ps -a`, đọc đầu ra chuẩn bằng `docker logs`, điều khiển bằng `docker stop` / `docker restart`.

### 2.2 Bài toán đã giải & PID Namespace
* Docker dùng **PID Namespace** của Linux Kernel để cô lập cây tiến trình. Tiến trình chính bên trong container luôn thấy mình là **PID 1**, không thể nhìn thấy hay gửi tín hiệu (`kill`) tới tiến trình của máy chủ hoặc của container khác.

### 2.3 Xóa bỏ Metaconflicts: Xây dựng Website Farm
* **Định danh linh hoạt (`--name`, Container ID, `--cidfile`)**: Thay vì phụ thuộc ID ngẫu nhiên, đặt tên tường minh để quản lý hoặc xuất CID ra file cho script tự động.
* **Trạng thái & phụ thuộc**: Hiểu sự khác biệt giữa Container đang chạy (`Running`), Tạm dừng (`Paused` - đóng băng tiến trình trên RAM), Đã thoát (`Exited`) và Đã xóa.

### 2.4 Xây dựng hệ thống Độc lập Môi trường (Environment-Agnostic)
* **Read-only filesystems (`--read-only`)**: Khóa hệ thống tệp gốc ở chế độ chỉ đọc để ngăn ứng dụng ghi nhầm dữ liệu trạng thái vào lớp container (và chống mã độc ghi file).
* **Tiêm biến môi trường (`-e` / `--env-file`)**: Truyền cấu hình như URL đích, cổng, chu kỳ kiểm tra lúc khởi chạy thay vì viết cứng vào code.

### 2.5 – 2.6 Container bền bỉ (Durable Containers) & Dọn dẹp
* **Chính sách tự khởi động lại (`--restart`)**: Các chế độ `no`, `on-failure[:max-retries]`, `always`, `unless-stopped`.
* **PID 1 và tiến trình `init` (`--init`)**: Tiến trình PID 1 trong Linux có trách nhiệm thu dọn tiến trình con chết (zombie processes) và chuyển tiếp tín hiệu `SIGTERM`. Dùng `--init` (tích hợp `tini`) nếu ứng dụng không tự xử lý việc này.
* **Dọn dẹp (`docker rm`, `--rm`)**: Tránh tích tụ container `Exited` gây lãng phí dung lượng.""",
        "cli_table": """| Câu lệnh | Chức năng |
| :--- | :--- |
| `docker run -d --name monitor --restart unless-stopped alpine sleep 3600` | Chạy nền có tên riêng và tự khởi động lại khi crash hoặc reboot máy chủ. |
| `docker run --rm --read-only -e TARGET_URL=https://example.com my-app` | Chạy tạm tự xóa (`--rm`), khóa ổ đĩa gốc chỉ đọc, truyền biến môi trường. |
| `docker run -d --init my-app` | Bọc tiến trình chính bằng `tini` init để dọn zombie process và xử lý `SIGTERM`. |
| `docker logs -f --tail 50 monitor` | Theo dõi 50 dòng log gần nhất theo thời gian thực. |
| `docker rm -f $(docker ps -aq)` | Cưỡng chế xóa sạch toàn bộ container đang có (chỉ dùng ở môi trường dev). |""",
        "sections_en": """### 2.1 – 2.3 Controlling Containers & PID Namespace
Containers can be launched interactively (`-it`) or in the background (`-d`), identified by friendly names (`--name`) or CID files (`--cidfile`). The Linux **PID namespace** isolates each container's process tree so internal processes cannot see or signal processes outside their boundary.

### 2.4 – 2.6 Environment-Agnostic & Durable Containers
Use `--read-only` to enforce statelessness and immutability, inject runtime parameters via `-e`/`--env-file`, enable resilience with `--restart`, and pass `--init` so PID 1 properly forwards OS signals and reaps zombie processes.""",
        "takeaways_vi": """- Luôn thiết kế container theo hướng **stateless & read-only** (`--read-only`), truyền toàn bộ cấu hình thay đổi qua biến môi trường (`-e`).
- Dùng cờ `--init` hoặc dùng entrypoint script chuẩn để tiến trình PID 1 nhận đúng `SIGTERM` khi dừng container.""",
    },
    {
        "num": 3,
        "part": 1,
        "part_label": "Phần 1: Cô lập Tiến trình & Điện toán Độc lập Môi trường",
        "stem": "Chương 03 - Đơn giản hóa cài đặt phần mềm (Software Installation Simplified)",
        "title_vi": "Chương 03: Đơn giản hóa cài đặt phần mềm (Software Installation Simplified)",
        "summary_vi": "Cách Docker định danh, tìm kiếm, tải về và cô lập tệp tin cài đặt phần mềm thông qua Registry, Repository, Tag và cơ chế Image Layers của Union Filesystem.",
        "summary_en": "Explains Docker software naming (registries, repositories, tags), pulling/loading images as files or from registries, and how image layers & Union Filesystems abstract and isolate container filesystems.",
        "sections_vi": """### 3.1 Định danh phần mềm (Identifying Software)
* **Named Repository**: Tên chuẩn của một image có dạng `[registry_host[:port]/][namespace/]repository[:tag]` (ví dụ `quay.io/coreos/etcd:v3.5` hoặc mặc định trên Docker Hub là `library/nginx:latest`).
* **Sử dụng Tags**: Tag xác định phiên bản cụ thể (ví dụ `postgres:15-alpine`). Tránh dùng `:latest` trong production vì `:latest` có thể âm thầm thay đổi theo thời gian.

### 3.2 Tìm kiếm và Cài đặt phần mềm
* **Làm việc với Docker Registries qua CLI**: Tìm kiếm (`docker search`), tải xuống (`docker pull`) và dùng Registry thay thế ngoài Docker Hub (như Quay.io, GitHub Container Registry, Amazon ECR).
* **Images dưới dạng tệp (Images as files)**: Đóng gói image thành file `.tar` để mang sang server không có Internet bằng `docker save -o app.tar my-app:1.0` và nạp lại bằng `docker load -i app.tar`.
* **Cài đặt từ Dockerfile & Website Docker Hub**: Khám phá Official Images (được kiểm duyệt bảo mật) và Verified Publishers trên Docker Hub.

### 3.3 Tệp cài đặt và Sự cô lập (Installation Files & Isolation)
* **Image Layers in action**: Mỗi Docker Image được ghép từ nhiều **tầng chỉ đọc (read-only layers)** xếp chồng lên nhau. Nếu 5 image cùng dùng chung tầng `alpine:3.18`, tầng này chỉ được tải và lưu **1 lần duy nhất** trên đĩa.
* **Container Filesystem Abstraction (Union Filesystems)**: Khi chạy container, Docker gắn thêm một tầng ghi-đọc mỏng (`writable container layer`) lên đỉnh của các tầng image qua cơ chế **Copy-on-Write (CoW)**.
* **Ưu và nhược điểm của Union FS**:
  * *Ưu điểm*: Tốc độ khởi tạo container tức thì, tiết kiệm ổ cứng tối đa.
  * *Nhược điểm*: Hiệu năng ghi nặng (như database) trên tầng CoW kém hơn hệ thống file gốc; một số đặc tính POSIX nâng cao (như `rename` thư mục lớn across layers) có thể gặp giới hạn — cần giải quyết bằng **Volumes** ở Chương 4.""",
        "cli_table": """| Câu lệnh | Chức năng |
| :--- | :--- |
| `docker pull postgres:15-alpine` | Tải về các layer của image theo đúng phiên bản tag. |
| `docker images` | Liệt kê tất cả image và các tag đang lưu trên máy. |
| `docker save -o backup.tar nginx:alpine` | Xuất toàn bộ image (gồm mọi layer và lịch sử) thành file `.tar` offline. |
| `docker load -i backup.tar` | Nạp lại image từ file `.tar` mà không cần Internet. |
| `docker history nginx:alpine` | Xem từng layer đã tạo nên image và kích thước mỗi layer. |""",
        "sections_en": """### 3.1 – 3.2 Identifying, Finding & Installing Software
Docker uniquely addresses software packages via `[registry/][namespace/]repo:tag`. Images can be fetched from Docker Hub or alternative registries (`docker pull`), built locally, or transferred offline as tar archives via `docker save` / `docker load`.

### 3.3 Image Layers & Union Filesystems
Union filesystems stack immutable **read-only layers** shared across images, topping each running container with a single ephemeral **writable layer** (Copy-on-Write). This gives instant startup and space efficiency, though I/O-heavy stateful data should bypass the union filesystem via Volumes.""",
        "takeaways_vi": """- Không dùng tag `:latest` trên môi trường thật; hãy ghim phiên bản cụ thể (`1.25.3-alpine`).
- Cơ chế chia sẻ layer giúp tải image cực nhanh và tiết kiệm dung lượng ổ cứng khi chạy nhiều dịch vụ dùng chung base image.""",
    },
    {
        "num": 4,
        "part": 1,
        "part_label": "Phần 1: Cô lập Tiến trình & Điện toán Độc lập Môi trường",
        "stem": "Chương 04 - Lưu trữ và Volumes (Working with Storage and Volumes)",
        "title_vi": "Chương 04: Lưu trữ và Volumes (Working with Storage and Volumes)",
        "summary_vi": "Giải quyết bài toán lưu trữ dữ liệu bền vững (Stateful) và hiệu năng I/O thông qua Bind Mounts, bộ nhớ tạm trên RAM (tmpfs), Named Volumes và kỹ thuật chia sẻ dữ liệu giữa các container.",
        "summary_en": "Covers container file trees and mount points, Bind mounts for host sharing, In-memory storage (tmpfs), Docker Volumes for container-independent persistence (NoSQL DB example), sharing mount points, volume cleanup, and volume plugins.",
        "sections_vi": """### 4.1 – 4.3 Cây thư mục, Bind Mounts và In-Memory Storage (`tmpfs`)
* **File trees & Mount points**: Khi container bị xóa, tầng ghi-đọc của nó mất vĩnh viễn. Để giữ dữ liệu hoặc đọc trực tiếp file trên máy chủ, Docker gắn kết (mount) không gian lưu trữ bên ngoài vào một đường dẫn bên trong cây thư mục container.
* **Bind Mounts (`--mount type=bind,...`)**: Ánh xạ trực tiếp một thư mục/tệp bất kỳ từ máy chủ vào container. Rất tiện khi phát triển code (hot-reload) hoặc chia sẻ file cấu hình từ host, nhưng phụ thuộc vào cấu trúc thư mục máy chủ.
* **In-memory storage (`tmpfs`)**: Lưu dữ liệu hoàn toàn trên **RAM**, không bao giờ ghi xuống ổ đĩa. Lý tưởng cho file tạm tốc độ cao, cache, hoặc bí mật nhạy cảm cần tự biến mất khi container tắt.

### 4.4 Docker Volumes (Quản lý dữ liệu độc lập với Container)
* **Named Volumes**: Vùng lưu trữ chuyên trách do Docker trực tiếp quản lý tại `/var/lib/docker/volumes/`.
* **Ứng dụng với NoSQL Database (Cassandra / MongoDB)**: Đưa thư mục dữ liệu database ra Volume giúp vượt qua giới hạn hiệu năng của Union Filesystem và đảm bảo dữ liệu sống sót ngay cả khi nâng cấp hay xóa bỏ container database.

### 4.5 – 4.7 Chia sẻ Mount Points, Dọn dẹp & Volume Plugins
* **Chia sẻ dữ liệu & Anonymous Volumes**: Các container có thể cùng trỏ vào một Named Volume hoặc kế thừa điểm gắn kết bằng cờ `--volumes-from` (mẫu Sidecar đọc/xoay vòng log).
* **Dọn dẹp Volumes (`docker volume prune`)**: Tránh "mồ côi" Anonymous Volumes làm đầy ổ cứng khi xóa container mà quên dùng cờ `-v`.
* **Volume Plugins**: Mở rộng lưu trữ sang hệ thống mạng/đám mây bên ngoài (AWS EBS, NFS, Ceph, GlusterFS) để phục vụ cụm nhiều máy chủ.""",
        "cli_table": """| Câu lệnh | Chức năng |
| :--- | :--- |
| `docker volume create db_data` | Tạo một Named Volume chuyên dụng do Docker quản lý. |
| `docker run -d --mount type=volume,src=db_data,dst=/var/lib/cassandra cassandra` | Gắn Named Volume vào container database bằng cú pháp `--mount` chuẩn. |
| `docker run --rm --mount type=bind,src=$(pwd)/src,dst=/app,readonly alpine` | Ánh xạ thư mục máy chủ theo chế độ chỉ đọc (`readonly`). |
| `docker run -d --mount type=tmpfs,dst=/tmp,tmpfs-size=64m my-app` | Gắn bộ nhớ tạm 64MB trên RAM cho thư mục `/tmp`. |
| `docker volume ls` / `docker volume prune` | Liệt kê và dọn dẹp các volume không còn gắn vào container nào. |""",
        "sections_en": """### 4.1 – 4.3 Bind Mounts & In-Memory Storage (`tmpfs`)
Mount points override sections of a container's union filesystem. **Bind mounts** link an arbitrary host path directly into the container (great for dev workflows), whereas **tmpfs mounts** store ephemeral or sensitive data solely in host RAM.

### 4.4 – 4.7 Docker Volumes & Shared Storage
**Docker Volumes** decouple data lifecycles from container lifecycles, bypass UnionFS copy-on-write overhead for databases, support multi-container sharing (or `--volumes-from`), and integrate with external storage backends via volume plugins.""",
        "takeaways_vi": """- Luôn dùng **Named Volume** cho dữ liệu Production (Database, file người dùng), ưu tiên cú pháp `--mount` vì rõ ràng hơn `-v`.
- Dùng `tmpfs` cho dữ liệu nhạy cảm tạm thời và dùng `docker rm -v` / `docker volume prune` để tránh đầy ổ đĩa bởi volume mồ côi.""",
    },
    {
        "num": 5,
        "part": 1,
        "part_label": "Phần 1: Cô lập Tiến trình & Điện toán Độc lập Môi trường",
        "stem": "Chương 05 - Mạng đơn máy chủ (Single-host Networking)",
        "title_vi": "Chương 05: Mạng đơn máy chủ (Single-host Networking)",
        "summary_vi": "Kiến thức nền tảng về mạng máy tính cho container, cách thiết lập User-defined Bridge Network với DNS nội bộ, các chế độ mạng đặc biệt (host, none), ánh xạ cổng (Port Publishing) và tùy chỉnh DNS.",
        "summary_en": "Reviews networking fundamentals (NAT, ports, interfaces), user-defined Docker bridge networks with automatic DNS, special network modes (host & none), inbound NodePort publishing, custom DNS customization, and security caveats.",
        "sections_vi": """### 5.1 Nền tảng mạng máy tính (Networking Background)
* Hiểu mối liên hệ giữa giao thức (TCP/UDP), giao diện mạng ảo (`veth`, `docker0`), dải IP nội bộ, **NAT (Network Address Translation)** cho luồng đi ra và **Port Forwarding** cho luồng đi vào từ Internet.

### 5.2 Mạng Container trong Docker (Bridge Network)
* **User-defined Bridge Network (`docker network create`)**: Khác với mạng `bridge` mặc định cũ kỹ, mạng Bridge tự định nghĩa cung cấp **Embedded DNS Server (`127.0.0.11`)**. Các container cùng mạng chỉ cần gọi nhau bằng **tên container** (Service Discovery tự động) và hoàn toàn tách biệt với các mạng khác.
* **Khảo sát mạng Bridge (`docker network inspect`)**: Xem danh sách IP, Subnet, Gateway và các container đang kết nối vào mạng.

### 5.3 Các chế độ mạng đặc biệt: `host` và `none`
* **`--network host`**: Gỡ bỏ cô lập NET Namespace. Container dùng thẳng card mạng và IP máy chủ (hiệu năng mạng tối đa, không qua NAT, nhưng dễ đụng độ port và kém cô lập).
* **`--network none`**: Chỉ giữ card `lo` (loopback), ngắt toàn bộ kết nối mạng ra ngoài — an toàn tuyệt đối cho tác vụ xử lý offline.

### 5.4 – 5.5 Ánh xạ cổng (Inbound Traffic), Tùy chỉnh DNS & Lưu ý Bảo mật
* **Port Publishing (`-p 8080:80`, `-P`)**: Ánh xạ cổng cụ thể trên máy chủ vào cổng container (hoặc gắn chặt vào `127.0.0.1:8080:80` để chỉ cho phép truy cập nội bộ).
* **Không có Firewall tự động giữa các container cùng mạng**: Mọi container trong cùng một Bridge Network đều có thể kết nối tới mọi cổng của nhau -> hãy tách thành nhiều mạng riêng (ví dụ `frontend-net` và `backend-net`).
* **Custom DNS (`--dns`, `--dns-search`, `--add-host`)**: Chỉ định DNS server riêng hoặc bổ sung ánh xạ host nội bộ (`/etc/hosts`) khi cần.""",
        "cli_table": """| Câu lệnh | Chức năng |
| :--- | :--- |
| `docker network create --driver bridge app-net` | Tạo mạng bridge riêng có DNS tự động phân giải tên container. |
| `docker run -d --name api --network app-net my-api` | Khởi chạy API ẩn trong mạng nội bộ (không mở port ra ngoài). |
| `docker run -d --name web --network app-net -p 80:80 nginx` | Mở cổng 80 công khai cho proxy và cho phép proxy gọi `http://api`. |
| `docker network connect db-net api` | Gắn thêm một card mạng thứ hai để container `api` nối được tới tầng DB. |
| `docker network inspect app-net` | Kiểm tra dải IP, gateway và các container thuộc mạng `app-net`. |""",
        "sections_en": """### 5.1 – 5.3 Bridge, Host, and None Networks
Each container lives in its own **NET namespace**. Creating a **user-defined bridge network** gives containers isolation plus automatic service discovery by container name via Docker's embedded DNS. Use `--network host` for raw host networking without NAT, or `--network none` for completely air-gapped containers.

### 5.4 – 5.5 Port Publishing & Caveats
Expose inbound ports selectively using `-p host_port:container_port`. Remember Docker bridge networks do not enforce L3/L4 firewall policies between co-located containers—segment multi-tier apps into isolated networks (`frontend` vs `backend`) and customize resolution with `--dns` / `--add-host` when necessary.""",
        "takeaways_vi": """- Luôn tạo **User-defined Bridge Network** thay vì dùng mạng `bridge` mặc định hay cờ `--link` lỗi thời.
- Áp dụng mô hình mạng phân tầng (Network Segmentation): chỉ mở cổng public cho Reverse Proxy, giấu Database và Backend API trong mạng nội bộ không publish port.""",
    },
    {
        "num": 6,
        "part": 1,
        "part_label": "Phần 1: Cô lập Tiến trình & Điện toán Độc lập Môi trường",
        "stem": "Chương 06 - Giới hạn rủi ro với Kiểm soát Tài nguyên (Limiting Risk with Resource Controls)",
        "title_vi": "Chương 06: Giới hạn rủi ro với Kiểm soát Tài nguyên (Limiting Risk with Resource Controls)",
        "summary_vi": "Kiểm soát tài nguyên phần cứng qua Linux Cgroups (RAM, CPU, Devices), chia sẻ bộ nhớ IPC, quản lý User/UID/User Namespace remapping, điều chỉnh Linux Capabilities và bảo vệ nâng cao bằng AppArmor/SELinux/Seccomp.",
        "summary_en": "Details Cgroups-based resource limits (memory, CPU, devices), shared IPC memory, running as non-root users and User Namespace UID remapping, dropping/adding Linux Capabilities, privileged mode risks, and LSM hardening (AppArmor, SELinux, seccomp).",
        "sections_vi": """### 6.1 Thiết lập hạn mức tài nguyên (Memory, CPU, Devices)
* **Giới hạn Bộ nhớ (`-m` / `--memory`)**: Ngăn một container bị rò rỉ RAM làm sập cả máy chủ. Khi vượt ngưỡng, nhân Linux sẽ kích hoạt **OOM Killer** để kết thúc tiến trình vi phạm.
* **Giới hạn CPU (`--cpus`, `--cpu-shares`, `--cpuset-cpus`)**: Ấn định số nhân tối đa (ví dụ `--cpus 1.5`) hoặc trọng số chia sẻ CPU khi hệ thống quá tải.
* **Truy cập thiết bị (`--device`)**: Cấp quyền truy cập thiết bị phần cứng cụ thể (GPU, USB, card âm thanh) thay vì mở toàn quyền.

### 6.2 Chia sẻ bộ nhớ (Sharing IPC)
* Hai container xử lý hiệu năng cao cần trao đổi dữ liệu qua bộ nhớ chia sẻ có thể ghép chung **IPC Namespace** bằng cờ `--ipc=container:<tên_container>` (hoặc `--ipc=shareable`).

### 6.3 Hiểu về User trong Container & User Namespace Remapping
* Mặc định tiến trình trong container chạy dưới UID 0 (`root`), cùng UID 0 trên máy chủ! Nếu container thoát ra ngoài qua lỗi kernel hoặc volume gắn sai, nó có quyền root thật.
* **Chạy với Non-root user (`-u 1000:1000` / `--user`)**: Luôn chỉ định UID cụ thể khớp với quyền trên Volume.
* **Linux User Namespace (`--userns-remap`)**: Ánh xạ UID 0 bên trong container thành một UID không có đặc quyền (ví dụ UID 100000) ở máy chủ thật.

### 6.4 – 6.7 Linux Capabilities, Privileged & Công cụ tăng cường bảo mật
* **Linux Capabilities (`--cap-drop=ALL`, `--cap-add=...`)**: Chia nhỏ quyền lực tối thượng của `root` thành hàng chục quyền nhỏ (như `NET_BIND_SERVICE` để mở port < 1024). Áp dụng **Least Privilege**: bỏ sạch tất cả rồi chỉ cấp lại quyền thực sự cần.
* **Tránh `--privileged`**: Cờ này tắt gần như mọi rào cản bảo mật, cho container quyền kiểm soát phần cứng như máy chủ.
* **AppArmor, SELinux & Seccomp (`--security-opt`)**: Lọc system calls (`seccomp`) và gắn nhãn kiểm soát truy cập bắt buộc (`MAC`) để khóa chặt bề mặt tấn công theo từng nhóm: Applications, High-level services, Low-level system services.""",
        "cli_table": """| Câu lệnh | Chức năng |
| :--- | :--- |
| `docker run -d -m 512m --cpus 1.5 my-app` | Giới hạn cứng 512MB RAM và 1.5 nhân CPU cho container. |
| `docker run --rm --user 10001:10001 --cap-drop=ALL my-app` | Chạy dưới quyền non-root và tước bỏ toàn bộ Linux Capabilities thừa. |
| `docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE nginx` | Chỉ cấp duy nhất quyền mở port dưới 1024 mà không cần full root. |
| `docker run --security-opt=no-new-privileges my-app` | Cấm tiến trình bên trong tự nâng đặc quyền (`setuid`). |""",
        "sections_en": """### 6.1 – 6.2 Resource Allowances & IPC
Linux **Cgroups** constrain hardware usage (`--memory`, `--cpus`, `--device`) so a runaway container cannot starve the host. High-throughput co-located apps can deliberately share POSIX shared memory using `--ipc=container:<name>`.

### 6.3 – 6.7 Least Privilege & Hardening
Avoid running as root inside containers: set `--user` explicitly, configure User Namespace UID remapping (`--userns-remap`), strip root capabilities (`--cap-drop=ALL`) and re-add only essential ones, reject `--privileged`, and harden syscalls via `seccomp`, `AppArmor`, or `SELinux` (`--security-opt`).""",
        "takeaways_vi": """- Nguyên tắc Production: **Luôn đặt giới hạn RAM/CPU**, chạy **non-root (`--user`)**, và dùng **`--cap-drop=ALL`** kèm **`no-new-privileges`**.
- Cấm dùng `--privileged` trên các dịch vụ ứng dụng thông thường.""",
    },
    {
        "num": 7,
        "part": 2,
        "part_label": "Phần 2: Đóng gói Phần mềm để Phân phối",
        "stem": "Chương 07 - Đóng gói phần mềm vào Image (Packaging Software in Images)",
        "title_vi": "Chương 07: Đóng gói phần mềm vào Image (Packaging Software in Images)",
        "summary_vi": "Cơ chế đóng gói thủ công từ container đang chạy (`docker diff` / `docker commit`), giải phẫu sâu Docker Image Layers & Union FS, sự khác biệt giữa `export/import` (flat filesystem) và `save/load`, cùng chuẩn đặt phiên bản.",
        "summary_en": "Explains building images interactively from containers (diff & commit), deep internals of union filesystems/layers/repositories/image sizes, flat filesystem export/import vs image save/load, and versioning best practices.",
        "sections_vi": """### 7.1 Đóng gói Image từ một Container
* **Quy trình thủ công (Commit workflow)**: Khởi chạy một container gốc -> cài đặt công cụ (ví dụ `git` hoặc app mẫu) -> kiểm tra những tệp nào đã bị thay đổi trên tầng container bằng **`docker diff`** -> đóng băng tầng thay đổi thành một image mới bằng **`docker commit`**.
* **Cấu hình thuộc tính Image**: Khi commit có thể đính kèm thông tin tác giả (`-a`), thông điệp (`-m`), hoặc thay đổi lệnh khởi động (`-c "ENTRYPOINT ..."`) để biến container cấu hình xong thành image có thể chạy ngay.

### 7.2 Đi sâu vào Docker Images và Layers
* **Giải phẫu Union Filesystems**: Mỗi lần `commit` (hoặc mỗi bước build) sẽ tạo một **tầng mới (layer)** bất biến chỉ chứa phần chênh lệch (`delta`) so với tầng bên dưới.
* **Image, Layer, Repository và Tag**: Thực chất, Image ID là mã băm SHA256 của tệp cấu hình JSON (chỉ danh sách các layer digests); còn **Repository:Tag** chỉ là "con trỏ tên thân thiện" trỏ tới Image ID đó. Một Image có thể có nhiều tag trỏ vào cùng lúc.
* **Quản lý kích thước & Giới hạn Layer**: Xóa một tệp lớn ở tầng trên *không làm giảm kích thước tổng của Image*, vì tệp đó vẫn nằm nguyên trong tầng lịch sử bên dưới (chỉ bị đánh dấu ẩn bằng *whiteout file*). Do đó cần dọn cache trong chính bước tạo tệp.

### 7.3 Export & Import Flat Filesystems
* **`docker export` / `docker import`**: Xuất toàn bộ hệ thống tệp hợp nhất của container ra thành **1 tầng phẳng duy nhất (flat filesystem)**, xóa sạch toàn bộ lịch sử layers và metadata (giúp thu gọn kích thước nhưng mất `ENV`, `ENTRYPOINT`). Khác hoàn toàn với `docker save` / `docker load` (giữ nguyên toàn bộ lịch sử nhiều layers và metadata).

### 7.4 Thực hành tốt về Đánh phiên bản (Versioning Best Practices)
* Dù `docker commit` hữu ích khi sửa nhanh hoặc học tập, trong thực tế chuyên nghiệp bạn nên đóng gói tự động và tái tạo được hoàn toàn bằng **Dockerfile** (Chương 8), đồng thời gắn tag theo phiên bản ngữ nghĩa (SemVer) hoặc mã commit Git.""",
        "cli_table": """| Câu lệnh | Chức năng |
| :--- | :--- |
| `docker diff <container>` | Xem các tệp đã thêm (`A`), thay đổi (`C`), hoặc xóa (`D`) trong container. |
| `docker commit -a "Team" -m "Add git" <cid> ubuntu-git:1.0` | Tạo image mới từ trạng thái hiện tại của container. |
| `docker export <cid> > flat-app.tar` | Xuất hệ thống tệp hiện tại thành tar phẳng (mất lịch sử layer). |
| `docker import flat-app.tar my-flat-app:1.0` | Tạo image 1 tầng duy nhất từ file export. |
| `docker tag my-app:1.0 myrepo/my-app:v1.0.2` | Gắn thêm bí danh/tag mới trỏ tới cùng một Image ID. |""",
        "sections_en": """### 7.1 – 7.2 Committing Containers & Layer Internals
You can interactively configure a container, inspect filesystem deltas via `docker diff`, and freeze changes into a new read-only layer with `docker commit`. A Docker image is fundamentally a manifest of immutable content-addressable layers; deleting a file in a later layer only writes a unionfs *whiteout* marker and does not reclaim space from lower layers.

### 7.3 – 7.4 Flat Export vs Save & Versioning
`docker export` / `docker import` flattens a container filesystem into a single-layer image (stripping metadata/history), whereas `docker save` / `docker load` preserves multi-layer structure. For maintainability, prefer declarative Dockerfiles and deterministic version tags.""",
        "takeaways_vi": """- Xóa file tạm (như cache `apt` hay file tải về) **ở tầng khác** không làm nhẹ image; phải xóa trong **cùng một bước tạo**.
- Phân biệt rõ: `save/load` giữ nguyên toàn bộ layers và metadata của Image; `export/import` làm phẳng container thành 1 layer duy nhất.""",
    },
    {
        "num": 8,
        "part": 2,
        "part_label": "Phần 2: Đóng gói Phần mềm để Phân phối",
        "stem": "Chương 08 - Tự động hóa xây dựng Image với Dockerfile (Building Images with Dockerfiles)",
        "title_vi": "Chương 08: Tự động hóa xây dựng Image với Dockerfile (Building Images with Dockerfiles)",
        "summary_vi": "Hướng dẫn toàn diện viết Dockerfile chuyên nghiệp: các chỉ thị Metadata & Filesystem, tiêm hành vi lúc build (`ARG`, `ONBUILD`), tối ưu Build Cache, thiết kế Startup Scripts + `HEALTHCHECK` và làm cứng bảo mật Image (Hardened Images).",
        "summary_en": "Complete guide to writing maintainable, hardened Dockerfiles: metadata vs filesystem instructions, build-time injection (`ARG`, `ONBUILD`), build cache efficiency, startup validation & `HEALTHCHECK`, content digests, and user/SUID hardening.",
        "sections_vi": """### 8.1 – 8.2 Đóng gói bằng Dockerfile & Các chỉ thị nền tảng
* **Dockerfile** là kịch bản văn bản mô tả từng bước tự động tạo ra Docker Image thông qua lệnh `docker build`.
* **Metadata Instructions**: `FROM` (image nền), `LABEL` (tác giả, phiên bản), `ENV` (biến môi trường lưu vào image), `EXPOSE` (khai báo cổng tài liệu), `WORKDIR` (đặt thư mục làm việc hiện hành), `USER`, `VOLUME`, `CMD` & `ENTRYPOINT`.
* **Filesystem Instructions**: `RUN` (thực thi lệnh khi build và tạo layer mới), `COPY` (sao chép tệp từ build context — luôn ưu tiên dùng `COPY`), `ADD` (tự giải nén tar hoặc tải URL — hạn chế dùng).

### 8.3 – 8.4 Tiêm tham số lúc Build (`ARG`, `ONBUILD`) & Bảo trì Dockerfile
* **`ARG`**: Biến chỉ tồn tại trong lúc `docker build` (truyền qua `--build-arg`), không rò rỉ vào container runtime như `ENV`.
* **`ONBUILD`**: Định nghĩa bước trì hoãn chỉ kích hoạt khi một Dockerfile khác dùng image này làm `FROM`.
* **Tối ưu Build Cache & `.dockerignore`**: Docker tái sử dụng cache từ trên xuống dưới cho đến dòng đầu tiên thay đổi. Do đó hãy đưa bước ít đổi (`COPY package.json`, `RUN npm ci`) lên trước `COPY . .`, đồng thời tạo `.dockerignore` loại bỏ `.git`, `node_modules` để giảm kích thước Build Context.

### 8.5 Startup Scripts, Init Process & `HEALTHCHECK`
* **Kiểm tra điều kiện tiên quyết (Preconditions Validation)**: Dùng script `entrypoint.sh` kiểm tra biến môi trường bắt buộc hoặc độ sẵn sàng của dependency trước khi `exec "$@"` (chạy ứng dụng chính dưới PID 1).
* **`HEALTHCHECK`**: Định nghĩa câu lệnh kiểm tra sức khỏe định kỳ (ví dụ `curl -f http://localhost:8080/health || exit 1`) giúp Docker phân biệt container đang chạy nhưng bị treo (`unhealthy`) với container khỏe mạnh (`healthy`).

### 8.6 Xây dựng Image cứng cáp & bảo mật (Hardened Images)
* **Content-addressable Image Identifiers (Digests)**: Ghim base image bằng mã băm `@sha256:...` thay vì chỉ dùng tag để chống tấn công thay đổi image âm thầm.
* **User Permissions & SUID/SGID**: Tạo user riêng với `USER appuser` thay vì chạy `root`, và loại bỏ các bit quyền nguy hiểm (`SUID`/`SGID`) khỏi file nhị phân để chặn leo thang đặc quyền.""",
        "cli_table": """| Câu lệnh / Chỉ thị | Chức năng |
| :--- | :--- |
| `docker build -t my-app:1.0 --build-arg VER=2.1 .` | Build image từ Dockerfile và truyền tham số `ARG` lúc build. |
| `docker build --no-cache -t my-app:1.0 .` | Ép build lại từ đầu, bỏ qua toàn bộ cache cũ (hữu ích khi tải gói mới). |
| `COPY --chown=app:app dist/ /app/` | Copy file và gán thẳng quyền sở hữu cho non-root user trong 1 layer. |
| `HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost/ \\|\\| exit 1` | Kiểm tra sức khỏe ứng dụng mỗi 30 giây. |""",
        "sections_en": """### 8.1 – 8.4 Dockerfile Primer & Maintainability
A **Dockerfile** automates image creation declaratively. Use metadata directives (`FROM`, `LABEL`, `WORKDIR`, `ENV`, `ENTRYPOINT`, `CMD`, `USER`) alongside filesystem directives (`RUN`, `COPY`). Order rarely changing steps (dependency installs) before frequently changing source files to maximize build cache hits, and pair with `.dockerignore`. Use `ARG` for build-time parameterization.

### 8.5 – 8.6 Startup Scripts, Health Checks & Hardening
Validate startup preconditions in an entrypoint script using `exec "$@"` to preserve PID 1 signal handling, embed `HEALTHCHECK` probes, pin immutable base image SHA256 digests, run under an unprivileged `USER`, and strip dangerous SUID/SGID binaries.""",
        "takeaways_vi": """- Sắp xếp chỉ thị theo thứ tự **ít thay đổi ở trên -> hay thay đổi ở dưới** và luôn dùng **`.dockerignore`**.
- Dùng **`exec "$@"`** ở cuối entrypoint script để tiến trình chính thay thế shell thành PID 1 và nhận được tín hiệu dừng `SIGTERM`.""",
    },
    {
        "num": 9,
        "part": 2,
        "part_label": "Phần 2: Đóng gói Phần mềm để Phân phối",
        "stem": "Chương 09 - Phân phối phần mềm Công khai và Riêng tư (Public and Private Software Distribution)",
        "title_vi": "Chương 09: Phân phối phần mềm Công khai và Riêng tư (Public and Private Software Distribution)",
        "summary_vi": "Phân tích các mô hình phân phối Docker Image từ công khai đến riêng tư: dùng Hosted Registries (Docker Hub), tự dựng Private Registry nội bộ, truyền file thủ công qua FTP/SSH và phân phối dưới dạng mã nguồn Dockerfile qua GitHub.",
        "summary_en": "Compares Docker image distribution methods along the public-to-private spectrum: hosted public/private registries (Docker Hub), self-hosting an internal Registry (`registry:2`), manual air-gapped archive distribution, and Dockerfile source distribution on GitHub.",
        "sections_vi": """### 9.1 Chọn phương pháp phân phối phù hợp
* **Phổ phương pháp phân phối**: Từ hoàn toàn công khai (Public Hosted Registry) -> Riêng tư trả phí (Private Hosted Registry) -> Tự vận hành nội bộ (Self-hosted Private Registry) -> Thủ công (`save`/`load` qua ổ cứng/FTP) -> Phân phối mã nguồn Dockerfile.
* **Tiêu chí lựa chọn**: Chi phí, kiểm soát bảo mật/tuân thủ nội bộ (compliance), băng thông mạng, kiểm soát truy cập (RBAC) và độ dễ tự động hóa.

### 9.2 Xuất bản qua Hosted Registries (Docker Hub)
* **Public Repositories**: Đăng nhập qua `docker login`, gắn tag theo chuẩn `<username>/<repo>:<tag>` rồi đẩy lên bằng `docker push` để cộng đồng tải về miễn phí.
* **Private Hosted Repositories**: Dành cho doanh nghiệp muốn lưu trữ kín trên cloud mà không cần tự vận hành hạ tầng server Registry.

### 9.3 Tự dựng Private Registry nội bộ
* Docker cung cấp sẵn image chính thức `registry` để chạy một máy chủ lưu trữ Image ngay trong mạng LAN doanh nghiệp hoặc VPC riêng.
* **Cấu hình & Bảo mật**: Bắt buộc kết hợp với TLS/SSL (chứng chỉ HTTPS) và xác thực tài khoản trên môi trường thật để các Docker client kết nối an toàn, tránh lỗi insecure-registry.

### 9.4 – 9.5 Phân phối thủ công & Source Distribution (GitHub)
* **Phân phối thủ công (`save`/`load` qua FTP/USB)**: Hữu ích trong môi trường mạng cô lập tuyệt đối (air-gapped) hoặc hệ thống quân sự/ngân hàng không kết nối Internet.
* **Phân phối mã nguồn (Dockerfile trên GitHub)**: Thay vì gửi file image nặng hàng trăm MB, chỉ đẩy `Dockerfile` + mã nguồn lên GitHub. Người dùng tự pull code và chạy `docker build`, hoặc tích hợp Automated Builds.""",
        "cli_table": """| Câu lệnh | Chức năng |
| :--- | :--- |
| `docker login` | Xác thực tài khoản vào Docker Hub hoặc Private Registry. |
| `docker tag my-app:1.0 myuser/my-app:1.0` | Gắn tên repository chuẩn để chuẩn bị đẩy lên Docker Hub. |
| `docker push myuser/my-app:1.0` | Đẩy các layer mới lên Registry (bỏ qua layer đã tồn tại). |
| `docker run -d -p 5000:5000 --name my-registry registry:2` | Tự khởi chạy một Private Docker Registry nội bộ tại cổng 5000. |
| `docker tag app:1.0 localhost:5000/app:1.0 && docker push localhost:5000/app:1.0` | Đẩy image vào Private Registry vừa dựng. |""",
        "sections_en": """### 9.1 – 9.2 Selecting Distribution & Hosted Registries
Choose distribution based on privacy, cost, bandwidth, and automation needs. Hosted registries like **Docker Hub** provide public sharing and private repositories via `docker login`, `docker tag <user>/<repo>:<tag>`, and `docker push`.

### 9.3 – 9.5 Self-Hosted Registries, Manual Archives & Source Workflows
Organizations requiring on-premise control can deploy the official `registry` container behind TLS and auth. In air-gapped networks, export compressed archives with `docker save` / `docker load`; for transparent builds, distribute source repositories containing a `Dockerfile` via Git/GitHub.""",
        "takeaways_vi": """- Quá trình `docker push` rất thông minh: chỉ tải lên những **layer chưa tồn tại** trên Registry đích, giúp tiết kiệm đáng kể băng thông khi cập nhật code.
- Phân phối qua **Private Registry** giúp doanh nghiệp kiểm soát chặt chẽ dữ liệu nội bộ nhưng cần chú trọng cấu hình TLS và sao lưu dữ liệu lưu trữ của Registry.""",
    },
    {
        "num": 10,
        "part": 2,
        "part_label": "Phần 2: Đóng gói Phần mềm để Phân phối",
        "stem": "Chương 10 - Quy trình xây dựng Image (Image Pipelines)",
        "title_vi": "Chương 10: Quy trình xây dựng Image (Image Pipelines)",
        "summary_vi": "Thiết kế quy trình CI/CD chuyên nghiệp cho Docker Image: chuyển đổi từ All-in-one sang Multi-stage builds siêu nhẹ, tự động ghi metadata (`Make` / git hash), chạy test ngay trong pipeline và chiến lược gắn Tag theo môi trường & Semantic Versioning.",
        "summary_en": "Designing production image build pipelines: comparing all-in-one vs separate builder/runtime vs multi-stage builds, stamping build metadata with Make, running automated image tests, and Continuous Delivery tagging strategies (unique tags, stage configs, SemVer).",
        "sections_vi": """### 10.1 – 10.2 Mục tiêu của Build Pipeline & Các mẫu thiết kế Image
* **Mục tiêu**: Nhanh, tái tạo được hoàn toàn (reproducible), an toàn (bề mặt tấn công nhỏ nhất) và có khả năng truy xuất nguồn gốc (traceability).
* **Mẫu 1 – All-in-one Images**: Đưa cả trình biên dịch, SDK, thư viện dev và mã nguồn vào 1 image. *Nhược điểm*: Phình to hàng GB và đầy lỗ hổng bảo mật.
* **Mẫu 2 – Tách Build & Runtime Images**: Dùng container builder để biên dịch ra binary, copy sang máy chủ rồi build image runtime thứ hai (cần script trung gian phức tạp).
* **Mẫu 3 – Multi-Stage Builds (Chuẩn khuyến nghị)**: Khai báo nhiều khối `FROM ... AS <stage>` trong **cùng 1 Dockerfile**. Giai đoạn cuối dùng base tối giản (`alpine` hoặc `scratch`) và chỉ dùng `COPY --from=builder` lấy đúng file nhị phân thành phẩm, giảm kích thước từ ~800MB xuống còn ~15MB.

### 10.3 – 10.4 Ghi Metadata bằng `Make` & Kiểm thử Image trong Pipeline
* **Orchestrating with `Makefile`**: Dùng `make` tự động truyền Git Commit SHA, ngày build, số phiên bản vào `--build-arg` để gắn thành `LABEL` vĩnh viễn trên Image.
* **Testing Images in Pipeline**: Sau khi build xong nhưng trước khi `push`, chạy các container test tự động (như `docker run --rm my-app test`, công cụ kiểm tra cấu hình/bảo mật như Chef InSpec hoặc quét lỗ hổng). Chỉ đẩy lên Registry khi mọi kiểm thử đều đạt.

### 10.5 Chiến lược gắn Tag cho Image (Tagging Patterns)
* **Unique Tags cho Continuous Delivery (CD)**: Gắn kèm mã Git SHA hoặc số Build CI (ví dụ `my-app:git-a1b2c3d`) để mọi bản triển khai đều duy nhất, không bao giờ ghi đè nhầm và dễ dàng rollback.
* **Configuration Image per Deployment Stage**: Có thể đóng gói biến cấu hình đặc thù (dev/staging/prod) hoặc giữ 1 image bất biến (immutable artifact) và tiêm config lúc chạy.
* **Semantic Versioning (SemVer)**: Gắn song song nhiều tag (`1.4.2`, `1.4`, `1`) để người dùng chọn mức ổn định mong muốn.""",
        "cli_table": """| Mẫu / Câu lệnh | Chức năng |
| :--- | :--- |
| `FROM golang:1.21 AS builder` ... `FROM alpine:3.18` + `COPY --from=builder` | Cú pháp **Multi-stage Build** tách công cụ build nặng khỏi runtime nhẹ. |
| `docker build --target test-stage -t my-app:test .` | Chỉ build và dừng ở stage kiểm thử cụ thể trong Multi-stage Dockerfile. |
| `docker build --build-arg GIT_SHA=$(git rev-parse --short HEAD) .` | Gắn vết mã nguồn Git vào metadata của Image trong CI/CD. |
| `docker run --rm my-app:git-a1b2c3d ./run-smoke-test.sh` | Chạy smoke test tự động trên chính image vừa build trước khi push. |""",
        "sections_en": """### 10.1 – 10.2 Pipeline Goals & Build Patterns
Production pipelines aim for speed, reproducibility, security, and traceability. **Multi-stage builds** solve the bloat of all-in-one images and complexity of multi-Dockerfile scripts by running heavy compilers in a `builder` stage and copying only compiled artifacts (`COPY --from=builder`) into a minimal `alpine` or `scratch` runtime stage.

### 10.3 – 10.5 Metadata, Automated Testing & Tagging
Automate build invocations with tools like `Make` to inject `GIT_SHA` and build dates as immutable labels, verify artifacts before publishing via automated container tests (e.g., smoke tests or InSpec), and publish using deterministic unique tags (Git SHA / CI build ID) alongside Semantic Versioning aliases (`1`, `1.4`, `1.4.2`).""",
        "takeaways_vi": """- **Multi-stage builds** là kỹ thuật bắt buộc trong CI/CD hiện đại để thu nhỏ image tới 90% và loại bỏ công cụ tấn công khỏi môi trường Production.
- Luôn gắn **Unique Tag (như Git Commit Hash)** cho mọi lần build CI/CD; không dựa vào tag `:latest`.""",
    },
    {
        "num": 11,
        "part": 3,
        "part_label": "Phần 3: Trừu tượng hóa Cấp cao và Điều phối",
        "stem": "Chương 11 - Quản lý Dịch vụ với Docker và Compose (Services with Docker and Compose)",
        "title_vi": "Chương 11: Quản lý Dịch vụ với Docker và Compose (Services with Docker and Compose)",
        "summary_vi": "Bước chuyển từ quản lý từng Container đơn lẻ sang khái niệm Dịch vụ (Service) có khả năng tự phục hồi/nhân bản/rolling update, và cách khai báo toàn bộ hệ thống đa dịch vụ bằng Docker Compose V3 YAML.",
        "summary_en": "Shifts from imperative single containers to declarative Services (resurrection, replication, rolling updates, health rollbacks) and defines complete multi-service stateful architectures using Docker Compose V3 YAML with automated load balancing and service discovery.",
        "sections_vi": """### 11.1 "Hello World!" với Docker Service
* **Container vs Service**: Chạy `docker run` là thao tác **mệnh lệnh (imperative)** trên 1 container đơn lẻ — nếu máy sập hoặc container chết, không ai thay thế nếu thiếu điều phối. **Docker Service** là mô hình **khai báo (declarative)**: bạn khai báo *trạng thái mong muốn* (ví dụ luôn chạy 3 bản sao), và hệ thống sẽ tự duy trì trạng thái đó.
* **Tự phục hồi, Nhân bản, Rolling Update & Rollback**: Nếu 1 bản sao bị crash, trình điều phối tự tạo bản thay thế (*resurrection*). Khi nâng cấp image (`v1` -> `v2`), hệ thống cập nhật cuốn chiếu từng phần (*rolling rollout*) và tự hoàn tác (*rollback*) nếu `HEALTHCHECK` báo lỗi.

### 11.2 Khai báo môi trường đa dịch vụ với Compose V3
* **A YAML Primer**: Nắm cấu trúc thụt lề, key-value, danh sách (`-`) trong YAML.
* **Tập hợp các dịch vụ (`docker-compose.yml`)**: Định nghĩa đồng thời Web frontend, Backend API, Cache, Database, Networks và Volumes chỉ trong 1 file văn bản, khởi chạy toàn bộ stack bằng một lệnh `docker compose up -d`.

### 11.3 – 11.4 Dịch vụ Có trạng thái (Stateful) & Khám phá dịch vụ
* **Stateful Services**: Kết hợp khai báo khóa `volumes:` cấp cao trong Compose để gắn kết lưu trữ bền vững cho Database (Postgres, WordPress, Redis) qua các lần khởi động lại hoặc tái tạo service.
* **Load Balancing & Service Discovery**: Compose tự tạo một mạng Bridge riêng cho dự án. Mỗi dịch vụ có thể gọi nhau trực tiếp qua **tên service** viết trong YAML (ví dụ backend kết nối `postgres://db:5432`), đồng thời hỗ trợ cân bằng tải DNS nội bộ khi scale nhiều replica.""",
        "cli_table": """| Câu lệnh | Chức năng |
| :--- | :--- |
| `docker compose up -d` | Đọc `docker-compose.yml`, tạo mạng/volume và chạy toàn bộ stack ở chế độ nền. |
| `docker compose ps` | Kiểm tra trạng thái và cổng ánh xạ của tất cả service thuộc stack. |
| `docker compose logs -f api` | Theo dõi log riêng của service `api` theo thời gian thực. |
| `docker compose up -d --scale api=3` | Nhân bản service `api` lên 3 container chạy song song. |
| `docker compose down` | Dừng và gỡ bỏ các container + mạng của stack (thêm `-v` nếu muốn xóa cả volume). |""",
        "sections_en": """### 11.1 – 11.2 From Containers to Declarative Services & Compose V3
A **Service** guarantees a desired target state (replica count, automatic container resurrection, zero-downtime rolling updates, and health-driven rollbacks). **Docker Compose V3 YAML** declares entire multi-service topologies, dependencies, networks, and volumes reproducibly in source-controlled configuration.

### 11.3 – 11.4 Stateful Services, Discovery & Load Balancing
Compose provisions isolated project networks automatically and wires **Service Discovery** by YAML service name, allowing stateless tiers to resolve and communicate with stateful volume-backed database containers seamlessly.""",
        "takeaways_vi": """- **Docker Compose** biến cấu hình hạ tầng phức tạp thành mã nguồn (`docker-compose.yml`) dễ đọc, dễ tái tạo và chia sẻ qua Git.
- Lưu ý: `docker compose down` mặc định **giữ lại Named Volumes** để bảo vệ dữ liệu; chỉ dùng `down -v` khi thực sự muốn xóa sạch database thử nghiệm.""",
    },
    {
        "num": 12,
        "part": 3,
        "part_label": "Phần 3: Trừu tượng hóa Cấp cao và Điều phối",
        "stem": "Chương 12 - Quản lý Cấu hình và Bí mật (First-class Configuration Abstractions)",
        "title_vi": "Chương 12: Quản lý Cấu hình và Bí mật (First-class Configuration Abstractions)",
        "summary_vi": "Tách biệt hoàn toàn mã nguồn khỏi cấu hình và thông tin nhạy cảm theo chuẩn ứng dụng hiện đại bằng các tài nguyên chuyên biệt của Docker là `docker config` và `docker secret`.",
        "summary_en": "Separates application images from environment settings and credentials using Docker's first-class `config` and `secret` resources: managing immutable config lifecycles and encrypting sensitive secrets delivered strictly in memory.",
        "sections_vi": """### 12.1 – 12.2 Phân phối cấu hình & Tách biệt Ứng dụng khỏi Cấu hình
* **Tại sao không nhúng file cấu hình vào Image?**: Nếu file `nginx.conf` hay `config.yaml` nằm bên trong image, mỗi khi đổi một tham số giữa môi trường Test và Production, bạn lại phải build image mới — vi phạm tính bất biến (immutability).
* **Tài nguyên `docker config`**: Là đối tượng hạng nhất (first-class resource) trong Docker Swarm/Compose giúp lưu trữ tập tin cấu hình độc lập, không phụ thuộc ổ cứng từng máy chủ.
* **Vòng đời bất biến**: Bạn tạo bằng `docker config create`, gắn vào service để đọc như một tệp thông thường trên container (ví dụ `/etc/nginx/nginx.conf`), và khi muốn cập nhật cấu hình thì tạo phiên bản mới (`app_config_v2`) rồi cập nhật service không gián đoạn.

### 12.3 Secrets — Dạng cấu hình đặc biệt cho Thông tin Nhạy cảm
* **Vấn đề của Biến môi trường (`ENV`)**: Biến môi trường dễ bị lộ qua `docker inspect`, log lỗi crash dump hoặc câu lệnh `ps`.
* **Cơ chế của `docker secret`**:
  * Được **mã hóa khi lưu trữ (encrypted at rest)** trong cơ sở dữ liệu đồng thuận Raft của Manager nodes và **mã hóa trên đường truyền (TLS)** khi gửi xuống Worker node.
  * Chỉ được giải mã và gắn vào container chạy thực tế thông qua hệ thống tệp trên **RAM (`tmpfs`)** tại đường dẫn `/run/secrets/<tên_secret>`. Không bao giờ ghi xuống đĩa cứng!
  * Ngay khi container dừng lại, đường dẫn `/run/secrets/` được tháo bỏ hoàn toàn.""",
        "cli_table": """| Câu lệnh | Chức năng |
| :--- | :--- |
| `docker config create my_conf_v1 ./app.conf` | Lưu file cấu hình thành tài nguyên `config` dùng chung trên cụm. |
| `docker config ls` / `docker config inspect my_conf_v1` | Liệt kê và kiểm tra cấu hình đã lưu (config không bảo mật nên đọc lại được). |
| `echo "S3cr3tP@ss" \\| docker secret create db_pass -` | Tạo một **Secret** được mã hóa từ đầu vào chuẩn (không lưu lại file văn bản thô). |
| `docker service create --name db --secret db_pass postgres:15` | Gắn secret vào service `db` dưới dạng file trong `/run/secrets/db_pass`. |
| `docker service update --secret-rm db_pass --secret-add db_pass_v2 db` | Xoay vòng (rotate) mật khẩu cho dịch vụ đang chạy. |""",
        "sections_en": """### 12.1 – 12.2 Separating App & Config (`docker config`)
Hardcoding configuration files inside images breaks artifact immutability across environments. Docker **Configs** decouple non-sensitive configuration files as immutable cluster resources mounted cleanly into target container paths without bind-mount host dependencies.

### 12.3 Docker Secrets (`docker secret`)
Never pass passwords or private keys in image layers or plain environment variables (`ENV`). **Docker Secrets** are encrypted at rest in the Raft store, transmitted solely over mutual TLS to active tasks, and decrypted only inside an in-memory `tmpfs` mount (`/run/secrets/<name>`), leaving zero plaintext footprint on disk.""",
        "takeaways_vi": """- Tuyệt đối **không lưu mật khẩu/API key trong `Dockerfile` hay `ENV`** khi triển khai Production; hãy dùng **`Secrets`** (hoặc mount file từ RAM).
- Cả `docker config` và `docker secret` đều có tính **bất biến (immutable)** — khi cần thay đổi, hãy tạo bản `_v2` rồi cập nhật service trỏ sang bản mới để dễ dàng rollback.""",
    },
    {
        "num": 13,
        "part": 3,
        "part_label": "Phần 3: Trừu tượng hóa Cấp cao và Điều phối",
        "stem": "Chương 13 - Điều phối Dịch vụ trên Cụm Swarm (Orchestrating Services with Swarm)",
        "title_vi": "Chương 13: Điều phối Dịch vụ trên Cụm Swarm (Orchestrating Services with Swarm)",
        "summary_vi": "Mở rộng ứng dụng vượt khỏi một máy chủ đơn lẻ lên cụm nhiều Docker Host với Docker Swarm: kiến trúc Manager/Worker, triển khai Stack hoàn chỉnh, định tuyến Swarm Routing Mesh, mạng Overlay đa máy chủ và chiến lược phân bổ Tasks.",
        "summary_en": "Master multi-host orchestration with Docker Swarm: Manager/Worker architecture, deploying full application stacks (`docker stack deploy`), Swarm Routing Mesh & multi-host Overlay networks, load balancing, Replicated vs Global services, and placement constraints.",
        "sections_vi": """### 13.1 – 13.2 Tạo cụm Swarm & Triển khai Ứng dụng lên Cụm
* **Docker Swarm Mode**: Tích hợp sẵn trong Docker Engine để gom nhiều máy chủ thành một cụm ảo duy nhất (`docker swarm init`, `docker swarm join`).
* **Manager Nodes vs Worker Nodes**: Manager duy trì trạng thái cụm qua đồng thuận **Raft** (khuyến nghị số lẻ như 3 hoặc 5 Manager để chịu lỗi) và lập lịch **Tasks** (tức các container); Worker nhận lệnh và thực thi Tasks.
* **Triển khai Stack (`docker stack deploy -c compose.yml my-stack`)**: Tái sử dụng định nghĩa YAML của Docker Compose V3 kèm khối `deploy:` để tạo đồng bộ Services, Networks, Configs và Secrets trên cả cụm nhiều máy chủ.

### 13.3 Giao tiếp trên Cụm: Routing Mesh & Overlay Networks
* **Swarm Routing Mesh (Ingress)**: Khi bạn publish cổng (ví dụ `80`), Swarm tự động mở cổng `80` trên **mọi máy chủ** trong cụm. Bất kể request đi vào IP của máy chủ nào (dù máy đó không chạy container web), Routing Mesh sẽ tự định tuyến nội bộ tới đúng container đang sống!
* **Overlay Networks (`--driver overlay`)**: Mạng ảo trải rộng xuyên qua nhiều máy chủ vật lý khác nhau (hỗ trợ tùy chọn mã hóa IPSec `--opt encrypted`). Mọi service trong mạng Overlay tự tìm kiếm nhau theo tên và tự động cân bằng tải (VIP Load Balancing).

### 13.4 Chiến lược Phân bổ Task trên Cụm (Placing Service Tasks)
* **Replicated vs Global Services**:
  * `replicated` (mặc định): Chạy đúng số lượng bản sao chỉ định (ví dụ `replicas: 5`) phân tán đều trên cụm.
  * `global`: Chạy **đúng 1 task trên mỗi node** trong cụm (cực kỳ phù hợp cho agent thu thập log, metric monitoring như Prometheus Node Exporter).
* **Placement Constraints & Preferences**: Ràng buộc dịch vụ chỉ chạy trên các node thỏa mãn nhãn (ví dụ `node.labels.disk == ssd` cho database) hoặc đặt giới hạn tài nguyên (`resources.limits` / `reservations`) để lập lịch thông minh.""",
        "cli_table": """| Câu lệnh | Chức năng |
| :--- | :--- |
| `docker swarm init` | Khởi tạo cụm Swarm và biến máy hiện tại thành Manager đầu tiên. |
| `docker node ls` | Xem danh sách tất cả Manager và Worker nodes cùng trạng thái hoạt động. |
| `docker network create -d overlay --opt encrypted secure-net` | Tạo mạng Overlay đa máy chủ có mã hóa lưu lượng. |
| `docker stack deploy -c docker-compose.yml prod_app` | Triển khai toàn bộ hệ thống đa dịch vụ lên cụm Swarm. |
| `docker stack services prod_app` / `docker service ps <svc>` | Theo dõi số replica và vị trí node đang chạy từng Task. |""",
        "sections_en": """### 13.1 – 13.2 Swarm Clustering & Stacks
**Docker Swarm** transforms a pool of Docker hosts into a unified cluster of Raft-backed **Manager nodes** and task-executing **Worker nodes**. Using `docker stack deploy`, standard Compose V3 definitions scale across multiple physical/cloud hosts seamlessly.

### 13.3 – 13.4 Routing Mesh, Overlay Networks & Scheduling
The **Swarm Routing Mesh** accepts inbound service ports on any node in the cluster and routes traffic to healthy tasks over encrypted **Overlay networks** using built-in VIP load balancing. Schedulers distinguish between **Replicated services** (exact N replicas) and **Global services** (one task per node, ideal for monitoring agents), steered by node placement constraints and resource reservations.""",
        "takeaways_vi": """- **Swarm Routing Mesh** + **Overlay Network** giúp ẩn giấu hoàn toàn sự phức tạp về địa chỉ IP vật lý của cụm nhiều máy chủ.
- Hiểu rõ bộ ba: **Compose** (phát triển local / 1 host) ➔ **Swarm Stack** (triển khai cụm gọn nhẹ) ➔ **Placement Constraints + Global/Replicated** (tối ưu phần cứng cụm).""",
    },
]


def _make_roadmap_content() -> str:
    p1_items = [c for c in CHAPTERS if c["part"] == 1]
    p2_items = [c for c in CHAPTERS if c["part"] == 2]
    p3_items = [c for c in CHAPTERS if c["part"] == 3]

    def _checklist(items: list[dict]) -> str:
        return "\n".join(
            f"- [ ] **[[{c['stem']}]]**\n  *{c['summary_vi']}*"
            for c in items
        )

    return f"""---
title: "{ROADMAP_STEM}"
type: roadmap
tags:
  - docker
  - roadmap
  - moc
  - obsidian-brain
aliases: ["Start Here", "Mục lục Docker in Action", "Reading Roadmap"]
---

# 📚 00 - Mục lục & Lộ trình Đọc: Docker in Action (2nd Edition)

> [!tip] **Tóm tắt chuẩn theo đúng 13 Chương sách**
> Toàn bộ kiến thức của cuốn sách **Docker in Action, 2nd Edition** *(Jeff Nickoloff & Stephen Kuenzli)* đã được cô đọng thành **13 Chương** thuộc **3 Phần lớn** dưới đây — sạch sẽ, có trình tự từ nhập môn đến làm chủ cụm Swarm, hoàn toàn không còn node vụn rác.

---

## 🗺️ Sơ đồ Lộ trình 3 Phần – 13 Chương

```mermaid
flowchart TD
    Start(["📖 Khởi đầu"]) --> C01["[[{CHAPTERS[0]['stem']}]]"]
    C01 --> C02["[[{CHAPTERS[1]['stem']}]]"]
    C02 --> C03["[[{CHAPTERS[2]['stem']}]]"]
    C03 --> C04["[[{CHAPTERS[3]['stem']}]]"]
    C04 --> C05["[[{CHAPTERS[4]['stem']}]]"]
    C05 --> C06["[[{CHAPTERS[5]['stem']}]]"]
    C06 --> C07["[[{CHAPTERS[6]['stem']}]]"]
    C07 --> C08["[[{CHAPTERS[7]['stem']}]]"]
    C08 --> C09["[[{CHAPTERS[8]['stem']}]]"]
    C09 --> C10["[[{CHAPTERS[9]['stem']}]]"]
    C10 --> C11["[[{CHAPTERS[10]['stem']}]]"]
    C11 --> C12["[[{CHAPTERS[11]['stem']}]]"]
    C12 --> C13["[[{CHAPTERS[12]['stem']}]]"]
    C13 --> Sum["📌 [[{SUMMARY_STEM}]]"]

    style Start fill:#0284c7,stroke:#0369a1,color:#fff
    style Sum fill:#db2777,stroke:#be185d,color:#fff
```

---

## 🟢 Phần 1: Cô lập Tiến trình & Điện toán Độc lập Môi trường *(Chương 01 – 06)*
{_checklist(p1_items)}

---

## 🟠 Phần 2: Đóng gói Phần mềm để Phân phối *(Chương 07 – 10)*
{_checklist(p2_items)}

---

## 🟣 Phần 3: Trừu tượng hóa Cấp cao và Điều phối *(Chương 11 – 13)*
{_checklist(p3_items)}

---

## 🎨 Bảng Trực Quan & Tổng Kết Toàn Sách
* 🗺️ Mở bảng trắng trực quan 3 Phần: **[[{CANVAS_FILE}]]**
* 📖 Đọc bản tóm tắt tổng thể cuốn sách: **[[{SUMMARY_STEM}]]**
"""


def _make_chapter_content(idx: int) -> str:
    ch = CHAPTERS[idx]
    prev_link = f"⬅ **[[{CHAPTERS[idx - 1]['stem']}]]**" if idx > 0 else "⬅ *(Chương đầu tiên)*"
    next_link = f"**[[{CHAPTERS[idx + 1]['stem']}]]** ➔" if idx < len(CHAPTERS) - 1 else "*(Chương cuối cùng)* ➔"

    return f"""---
title: "{ch['title_vi']}"
chapter: {ch['num']}
part: {ch['part']}
type: chapter-summary
tags:
  - docker
  - chapter
  - part-{ch['part']}
  - obsidian-brain
source: "[[{SUMMARY_STEM}]]"
---

# 📖 {ch['title_vi']}

> [!info] **{ch['part_label']}**
> 🇻🇳 **Trọng tâm chương**: {ch['summary_vi']}
>
> 🇬🇧 **Executive Summary**: {ch['summary_en']}

---

## 🇻🇳 PHÂN TÍCH CHI TIẾT TỪNG MỤC (TIẾNG VIỆT)

{ch['sections_vi']}

---

## 🛠️ Bảng Câu lệnh CLI & Thực hành Trọng tâm

{ch['cli_table']}

---

## 🇬🇧 COMPREHENSIVE ENGLISH CHAPTER SUMMARY

{ch['sections_en']}

---

## 💡 Đúc kết & Thực hành Tốt nhất (Key Takeaways)

{ch['takeaways_vi']}

---

## 🧭 Điều hướng Chương
{prev_link} &nbsp;|&nbsp; 🧭 **[[{ROADMAP_STEM}]]** &nbsp;|&nbsp; {next_link}

* 📖 Quay về bản tóm tắt tổng thể: **[[{SUMMARY_STEM}]]**
"""


def main() -> None:
    VAULT_DIR.mkdir(parents=True, exist_ok=True)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    roadmap_text = _make_roadmap_content()
    for out_dir in (VAULT_DIR, BACKUP_DIR):
        (out_dir / f"{ROADMAP_STEM}.md").write_text(roadmap_text, encoding="utf-8")
    print(f"✓ Created Roadmap: {ROADMAP_STEM}.md")

    for idx, ch in enumerate(CHAPTERS):
        text = _make_chapter_content(idx)
        fname = f"{ch['stem']}.md"
        for out_dir in (VAULT_DIR, BACKUP_DIR):
            (out_dir / fname).write_text(text, encoding="utf-8")
        print(f"✓ Created Chapter {ch['num']:02d}: {fname}")


if __name__ == "__main__":
    main()
