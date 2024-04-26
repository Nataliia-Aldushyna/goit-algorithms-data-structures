"""
Завдання 1
Потрібно розробити програму, яка імітує приймання й обробку заявок: 
програма має автоматично генерувати нові заявки (ідентифіковані унікальним номером або іншими даними),
додавати їх до черги, а потім послідовно видаляти з черги для "обробки", 
імітуючи таким чином роботу сервісного центру.

"""

import queue
import time
import threading

# Створити чергу заявок
request_queue = queue.Queue()


# Функція generate_request():
# Генерує нову заявку та додає її до черги
def generate_request():
    while not exit_flag:
        time.sleep(2)
        request = "Request #" + str(time.time())
        request_queue.put(request)
        print("New request:", request)


# Функція process_request():
# Видаляє заявку з черги та імітує її обробку
def process_request():
    while not exit_flag:
        if not request_queue.empty():
            request = request_queue.get()
            print("Processing request:", request)
            time.sleep(1)
        else:
            print("No requests to process")
            time.sleep(2)


exit_flag = False
generator_thread = threading.Thread(target=generate_request)
processor_thread = threading.Thread(target=process_request)

generator_thread.start()
processor_thread.start()


input("Press Enter to stop the program...\n")
exit_flag = True

generator_thread.join()
processor_thread.join()
