import string

# 
# class STROPS:
# 
#     def generate_seq_id(self):
#         for a1 in string.ascii_uppercase:
#             for a2 in string.ascii_uppercase:
#                 for a3 in string.ascii_uppercase:
#                     for num in range(1, 10000):
#                         number = str(num)
#                         if len(number) < 4:
#                             pads = 4 - len(number)
#                             number = "0"*pads + number
#                         yield a1 + a2 + a3 + number
#     
#     def __repr__(self):
#         return 'UUID('+ self.generate_seq_id() + ')' 
# if __name__ == "__main__":
#     so = STROperations()
#     for i in so.generate_seq_id():
#         print(i)