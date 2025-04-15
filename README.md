# 中文字符 → Quoted-printable 编码工具

这是一个简单的 Python 工具，可以将中文字符（例如“杭”）转换为 Quoted-printable 编码，支持 UTF-8 和 GBK 编码方式，并输出中间过程：

- 原始编码字节
- Quoted-printable 编码结果
- 编码字符串的 ASCII 十六进制表示

## 🛠 使用方式

1. 安装 Python（推荐 3.6+）
2. 运行脚本：

```bash
python qp_converter.py
```
3. 输入你要转换的中文字符，选择编码方式（utf-8 或 gbk）

4. 程序会输出每一步转换结果

示例
输入字符：杭
选择编码：GBK
输出：

复制
编辑
➡ 原始字节（gbk）：BA BC  
➡ Quoted-printable 编码结果：=BA=BC  
➡ 编码字符串的 ASCII 十六进制：3D42413D4243
🚀 项目用途
了解邮件编码（MIME / Quoted-printable）

中文编码调试 / 学习

网络安全 / 编码还原工具开发

欢迎 star 🌟 这个项目！