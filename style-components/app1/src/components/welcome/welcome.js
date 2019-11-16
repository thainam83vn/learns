import React from "react";
import styled from "styled-components";

const Title = styled.h1`
  color: red;
  font-style: italic;
`;
const Input = styled.input.attrs(props => ({
  // we can define static props
  type: "password"
}))`
  color: palevioletred;
  font-size: 1em;
  border: 2px solid palevioletred;
  border-radius: 3px;

  /* here we use the dynamically computed prop */
  margin: ${props => props.size};
  padding: ${props => props.size};
`;

const data = `
Trong thời gian làm việc hơn 1 năm rưỡi ở Phillips 66, Hongjin Tan đã đánh cắp các bí mật về công nghệ chế tạo pin tương lai của tập đoàn này và đang lên kế hoạch trở về Trung Quốc thì bị FBI bắt giữ.

Theo Hãng tin Reuters, dù đã có "thẻ xanh" ở Mỹ, Tan vẫn muốn trở về Trung Quốc sau khi đọc được một mẩu tuyển dụng phát triển dây chuyền sản xuất pin lithium ion của một công ty Trung Quốc.

Trong thông cáo ngày 12-11, Bộ Tư pháp Mỹ xác nhận ông Tan đã nhận tội tại một tòa án liên bang ở Oklahoma cho 3 tội danh: trộm cắp bí mật thương mại, chuyển giao trái phép bí mật thương mại và sở hữu trái phép bí mật thương mại.

Giá trị thị trường của công nghệ pin mà ông này ăn cắp là hơn 1 tỉ USD. Trong đơn tố cáo gửi đến Cục Điều tra liên bang Mỹ (FBI), Phillips 66 cho biết công nghệ mà Tan ăn cắp đã giúp họ kiếm được từ 1,4 đến 1,8 tỉ USD.

Trong một tuyên bố sau phiên tòa ngày 12-11 (giờ Mỹ), trợ lý bộ trưởng tư pháp Mỹ, ông John Demers, nhận xét vụ việc của ông Tan đã ghép thêm một mảnh nữa vào bức tranh ăn cắp sở hữu trí tuệ Mỹ từ Trung Quốc.

Ông Trent Shores, một luật sư tham gia phiên tòa, gọi Tan là một trong số "các gián điệp công nghiệp Trung Quốc" và nhiệm vụ của những người này là nhằm đánh cắp bí mật thương mại và sở hữu trí tuệ của Mỹ.

"Sự xâm lược kinh tế của Trung Quốc đặt ra một mối đe dọa đối với các ngành công nghiệp công nghệ cao mới nổi của Mỹ", ông Shores cảnh báo.

Theo Hãng thông tấn AFP, ông Tan làm việc như một nhà khoa học cộng tác với Phillips 66 từ tháng 6-2017 cho đến khi bị bắt giữ vào tháng 12-2018 trong bộ phận chuyên về nghiên cứu và phát triển công nghệ pin mới.

Tan trước đó học tập, nghiên cứu và lấy bằng tiến sĩ tại Viện Công nghệ California của Mỹ.

Tòa đã ấn định thời gian tuyên án công dân Trung Quốc vào ngày 12-2 năm sau, với mức án dự kiến sẽ giảm xuống còn 2 năm tù sau khi Tan nhận tội. Tập đoàn Phillips 66 được bồi thường 150.000 USD.
`;

export default () => {
  return (
    <div>
      <Title>Welcome</Title>
      <Input size="5px" />
    </div>
  );
};
