# import time
# from threading import Thread
#
#
# def read_file():
#     print("O'qish boshlandi!!!")
#     time.sleep(1)
#     print("O'qish tugadi✅✅")
#
#
# start = time.time()
#
# th1 = Thread(target= read_file)
# th2 = Thread(target= read_file)
# th3 = Thread(target= read_file)
#
# th1.start()
# th2.start()
# th3.start()
#
# th1.join()
# th2.join()
# th3.join()
#
# end = time.time()
#
# print(f"Faylni o'qish uchun {round(end - start, 2)}")

# --------------------------------------------------
# import time
# from threading import Thread
#
#
# def read_file():
#     print("O'qish boshlandi!!!")
#     time.sleep(0.000000000000000000001)
#     print("O'qish tugadi✅✅")
#
#
# start = time.time()
# threades = []
# for i in range(10000):
#     th = Thread(target=read_file)
#     th.start()
#     threades.append(th)
#
# for th in threades:
#     th.join()
# end = time.time()
#
# print(f"Faylni o'qish uchun {round(end - start, 2)}")
