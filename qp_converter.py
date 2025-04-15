import quopri

def str_to_bytes(text: str, encoding: str = 'utf-8') -> bytes:
    return text.encode(encoding)

def bytes_to_quoted_printable(b: bytes) -> bytes:
    return quopri.encodestring(b)

def quoted_printable_to_ascii_hex(qp: bytes) -> str:
    return ''.join(f'{byte:02X}' for byte in qp)

def run_converter():
    print("🔠 中文字符 → Quoted-printable 编码工具")
    text = input("请输入文字（例如：杭）：")
    encoding = input("选择编码方式（utf-8 或 gbk，默认 utf-8）：").strip().lower()
    if encoding not in ['utf-8', 'gbk']:
        encoding = 'utf-8'

    # 编码过程
    print(f"\n✅ 使用编码：{encoding}")
    byte_data = str_to_bytes(text, encoding)
    print(f"➡ 原始字节（{encoding}）：", ' '.join(f'{b:02X}' for b in byte_data))

    qp_data = bytes_to_quoted_printable(byte_data)
    print("➡ Quoted-printable 编码结果：", qp_data.decode('ascii'))

    hex_output = quoted_printable_to_ascii_hex(qp_data)
    print("➡ 编码字符串的 ASCII 十六进制：", hex_output)

if __name__ == "__main__":
    run_converter()
