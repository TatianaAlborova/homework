import threading
import time
import random

lock = threading.Lock()

class Bank(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            refill = random.randint(50, 500)
            self.lock.acquire()
            try:
                self.balance += refill
                print(f"Пополнение: {refill}. Баланс: {self.balance}")
            finally:
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            rm = random.randint(50, 500)
            print(f'Запрос на {rm}')
            self.lock.acquire()
            try:
                if rm <= self.balance:
                    self.balance -= rm
                    print(f'Снятие: {rm}. Баланс: {self.balance}')
                else:
                    print(f'Запрос отклонен, недостаточно средств')
            finally:
                self.lock.release()
            time.sleep(0.001)



bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')


