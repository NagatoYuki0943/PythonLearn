import hashlib

msg = "hello world"

res = hashlib.md5(msg.encode('utf-8')).hexdigest()  # hexdigest 转为16进制
print(res)
# 5eb63bbbe01eeed093cb22bb8f5acdc3  32个长度

res = hashlib.sha1(msg.encode('utf-8')).hexdigest()
print(res)
# 2aae6c35c94fcfb415dbe95f408b9ce91ee846ed 40个长度

res = hashlib.sha224(msg.encode('utf-8')).hexdigest()
print(res)
# 2f05477fc24bb4faefd86517156dafdecec45b8ad3cf2522a563582b  # 56个长度

res = hashlib.sha256(msg.encode('utf-8')).hexdigest()
print(res)
# b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9  # 64个长度

res = hashlib.sha384(msg.encode('utf-8')).hexdigest()
print(res)
# fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd  # 96个长度

res = hashlib.sha512(msg.encode('utf-8')).hexdigest()
print(res)
# 309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f  # 128个长度

