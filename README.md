"# MLOps" 

Design_Pattern
1. Factory Design Pattern (Mẫu thiết kế nhà máy)
Mục đích: Factory Pattern được sử dụng để tạo ra các đối tượng mà không cần chỉ định lớp cụ thể nào. Nó cho phép bạn trừu tượng hóa việc tạo đối tượng và tách biệt quá trình khởi tạo đối tượng khỏi code sử dụng đối tượng đó.
Cách hoạt động: Một lớp hoặc phương thức gọi đến Factory sẽ không cần biết về việc cụ thể hóa đối tượng mà nó sẽ nhận. Factory Pattern thường được sử dụng khi hệ thống cần tạo nhiều loại đối tượng có cùng giao diện hoặc lớp cha nhưng khác biệt ở chi tiết cài đặt.
Khi nào sử dụng: Khi bạn cần khởi tạo nhiều đối tượng khác nhau thuộc cùng một họ (family) lớp, nhưng không muốn để lớp gọi biết về chi tiết của các lớp con cụ thể.

Factory Pattern tập trung vào việc tạo ra các đối tượng, giúp tách rời quá trình khởi tạo khỏi mã chính.

2. Strategy Design Pattern (Mẫu thiết kế chiến lược)
Mục đích: Strategy Pattern được sử dụng để định nghĩa một họ các thuật toán khác nhau, và cho phép các thuật toán này có thể thay thế cho nhau trong runtime. Mẫu thiết kế này giúp thay đổi hành vi của đối tượng mà không cần thay đổi code của đối tượng đó.
Cách hoạt động: Bạn có thể xác định nhiều chiến lược (strategy), và tại runtime, một đối tượng sẽ được truyền chiến lược phù hợp để thực hiện hành vi tương ứng. Mẫu này thường được sử dụng khi có nhiều thuật toán để thực hiện một tác vụ và bạn muốn chọn thuật toán phù hợp tại thời điểm runtime.
Khi nào sử dụng: Khi bạn có nhiều cách khác nhau để thực hiện một hành động hoặc thuật toán, và muốn thay đổi hành vi này một cách linh hoạt.

Strategy Pattern tập trung vào hành vi của đối tượng, cho phép thay đổi thuật toán linh hoạt mà không làm thay đổi cấu trúc của đối tượng.

Analysze data: Julius
