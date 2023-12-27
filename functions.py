def check_num(num):
    """
        Проверяет, является ли переданное значение числом или нет.

        Args:
            num (str): Строковое представление числа для проверки.

        Returns:
            int: 1, если переданная строка не является числом, 0 в противном случае.
        """
    for i in range(len(str(num))):
        if not ((str(num))[i] in '-0123456789'):
            return 1
            break
    else:
        return 0


balance = 0


def input_balance(blc):
    """
        Обновляет баланс, добавляя указанное значение.

        Args:
            blc (str): Строковое представление числа для обновления баланса.

        Returns:
            str: "wrong input", если переданная строка не является числом, в противном случае None.
        """
    global balance

    if check_num(blc) == 1:
        return "wrong input"

    balance += int(blc)


categories = [0, 0, 0, 0, 0]


def add_categories_budget(categ_inf, ind):
    """
        Обновляет бюджет категории и баланс в соответствии с введенной информацией.

        Args:
            categ_inf (str): Строка с информацией о бюджете категории (например, "1 500").
            ind (int): Индекс категории для обновления.

        Returns:
            str: "wrong input", если введенная строка имеет неверный формат.
                 "no money", если на балансе недостаточно средств для выделения указанного бюджета.
                 В противном случае None.
        """
    global categories
    global balance

    if categ_inf.count(" ") == 1:
        budg_of_categ = categ_inf.split(" ")

        if check_num(budg_of_categ[1]) == 0:
            balance -= int(budg_of_categ[1])
            if balance >= 0:
                categories[ind] += int(budg_of_categ[1])
            else:
                balance += int(budg_of_categ[1])
                return "no money"
        else:
            return "wrong input"
    else:
        return "wrong input"

    print(f"1 - {categories[0]} , 2 - {categories[1]} , 3 - {categories[2]} , 4 - {categories[3]} ,5 - {categories[4]}")
