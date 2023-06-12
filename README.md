### Info 
This project was developed as part of a test assignment. It allows for determining the independent movement of the ETHUSDT futures, excluding movements caused by the influence of BTCUSDT price.

### Installation instructions

1. You must have docker installed

2. Clone rep
```bash
git clone https://github.com/Shved15/SP-Shcherbin-test-task.git
```

3. Inside the project directory enter:

```bash
docker-compose up --build
```

4. If everything is fine, then in a minute you should get logs in the console


### Task:

1. Вам нужно определить собственные движения цены фьючерса ETHUSDT, исключив из них движения вызванные влиянием цены BTCUSDT. Опишите, какую методику вы выбрали, какие параметры подобрали, и почему.

2. Напишите программу на Python, которая в реальном времени (с минимальной задержкой) следит за ценой фьючерса ETHUSDT и используя выбранный вами метод, определяет собственные движение цены ETH. При изменении цены на 1% за последние 60 минут, программа выводит сообщение в консоль. При этом программа должна продолжать работать дальше, постоянно считывая актуальную цену.




