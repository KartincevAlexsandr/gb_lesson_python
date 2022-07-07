import re


tempText = ''

## логирование
def logger(func):
    def wrapper(text):

        res = func(text)
        with open("logCalc.txt", 'a', encoding='utf-8') as file:
            file.write(f' выражение {text} результат {res} \n')
        return res

    return wrapper






@logger
def resolution(textExpression):
    def compute_mul_div(arg):
        # print(f"{arg=}")
        val = arg[0]
        mch = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',val)
        # print(f"{mch=}")
        if not mch:
            return
        content = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',val).group()

        if len(content.split('*')) > 1:
            n1, n2 = content.split('*')
            value = float(n1) * float(n2)
        else:
            n1, n2 = content.split('/')
            value = float(n1) / float(n2)

        before, after = re.split('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', val, 1)
        new_str = f"{before} {value} {after}"


        arg[0] = new_str
        compute_mul_div(arg)


    def compute_add_sub(arg):
        while True:
            if arg[0].__contains__('+-') or arg[0].__contains__("++") or arg[0].__contains__('-+') or arg[0].__contains__("-"):
                arg[0] = arg[0].replace('+-', '-')
                arg[0] = arg[0].replace('++', '+')
                arg[0] = arg[0].replace('-+', '-')
                arg[0] = arg[0].replace('--', '+')
            else:
                break

            if arg[0].startswith('-'):  #
                arg[1] += 1
                arg[0] = arg[0].replace('-', '&')
                arg[0] = arg[0].replace('+', '-')
                arg[0] = arg[0].replace('&', '+')
                arg[0] = arg[0][1:]


        val = arg[0]
        mch = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', val)
        if not mch:
            return
        content = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', val).group()
        if len(content.split('+')) > 1:
            n1, n2 = content.split('+')
            value = float(n1) + float(n2)
        else:
            n1, n2 = content.split('-')
            value = float(n1) - float(n2)

        before, after = re.split('\d+\.*\d*[\+\-]{1}\d+\.*\d*', val, 1)
        new_str = f"{before} {value} {after}"
        arg[0] = new_str
        compute_add_sub(arg)


    def compute(expression):
        inp = [expression, 0]
        # print(f"{inp=}")
        compute_mul_div(inp)
        inp[0] = inp[0].lstrip()
        print(f"{inp=}")
        if divmod(inp[1], 2)[1] == 1:
            result = float(inp[0])
            result = result * -1
        else:
            if not re.split('[\+\-]{1}', inp[0], 1):
                result = float(inp[0])
            else:
                if '-' in inp[0]:
                    tem = inp[0].split('-')
                    result = float(tem[0])-float(tem[1])
                elif '+' in inp[0] :
                    tem = inp[0].split('+')
                    result = float(tem[0])+float(tem[1])
                elif '**' in inp[0] :
                    tem = inp[0].split('**')
                    result = float(tem[0])**float(tem[1])
                elif '*' in inp[0] :
                    tem = inp[0].split('*')
                    result = float(tem[0])*float(tem[1])
                elif '/' in inp[0] :
                    tem = inp[0].split('/')
                    result = float(tem[0])/float(tem[1])
                elif ' ' in inp[0] :
                    tem = inp[0].split(' ')
                    result = float(tem[0])*float(tem[1])

                else:
                    result = float(inp[0])


        return result


    def exec_bracket(expression):
        # print(f"{expression=}")
        if not re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', expression):
            final = compute(expression)
            return final


        content = re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', expression).group()
        # print(f"{content=}")

        before, nothing, after = re.split('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', expression, 1)
        #
        # print('before：', expression)

        content = content[1: len(content) - 1]

        ret = compute(content)
        #
        # print('% s =% s' % (content, ret))

        expression = f"{before} {ret} {after}"
        # print('after:', ret)
        # print("=" * 10, 'Конец последнего вычисления', "=" * 10)
        return exec_bracket (expression)

    textExpression = re.sub('\s*', '', textExpression)
    result = exec_bracket(textExpression)
    return result


def funcCalc(param):
    global tempText

    if param == "C":
        tempText = ""
    elif param == "Del":
        try:
            tempText = tempText[0:-1]
        except:
            tempText = ""

    elif param == '=':
        tempText = resolution(tempText)
        print(f'{tempText=}')
        return str(tempText)


    else:
        tempText += param

    return tempText
