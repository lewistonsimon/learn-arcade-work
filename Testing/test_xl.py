# in terminal type: pip install "and library name that you want to install"
import random
# from openpyxl import Workbook
# wb = Workbook()
#
# # grab the active worksheet
# ws = wb.active
#
# # Data can be assigned directly to cells
# ws['A1'] = 42
#
# for i in range(200):
#     ws.append(["Random Number:". random.randrange(1000)])
# # Rows can also be appended
# ws.append([1, 2, 3])
#
# # Python types will automatically be converted
# import datetime
# ws['A2'] = datetime.datetime.now()
#
# # Save the file
# wb.save("sample.xlsx")

import matplotlib.pyplot as plt

x = [1,2,3,4]
y1 = [1,3,8,4]
y2 = [2, 2, 3, 3]

plt.plot(x, y1, label = "series 1")
plt.plot(x, y2, lable = "series 2")

