import Rule
import copy

def get_rule_set():
    '''
获得论文中的所有规则
    '''

    res = []
    
    add = copy.deepcopy(Rule.Rule())
    add.add_precondition('水处理不合格'       , 0.6)
    add.add_precondition('受热管局部汽化'     , 0.2)
    add.add_precondition('排污不及时'         , 0.2)
    add.set_alpha(0.75)
    add.set_CF(0.95)
    add.set_resule('受热管结垢')
    res.append(add)  # 添加Rule 1

    add = copy.deepcopy(Rule.Rule())
    add.add_precondition('受热管结垢'       , 0.5)
    add.add_precondition('清垢处理不及时'    , 0.5)
    add.set_alpha(0.8)
    add.set_CF(0.95)
    add.set_resule('传热热阻增大')

    res.append(add)  # 添加Rule 4

    add = copy.deepcopy(Rule.Rule())
    add.add_precondition('对流管束积灰'       , 0.5)
    add.add_precondition('清灰处理不及时'    , 0.5)
    add.set_alpha(0.85)
    add.set_CF(0.92)
    add.set_resule('传热热阻增大')

    res.append(add)  # 添加Rule 5

    add = copy.deepcopy(Rule.Rule())
    add.add_precondition('水冷壁管结焦'       , 0.5)
    add.add_precondition('除焦处理不及时'    , 0.5)
    add.set_alpha(0.8)
    add.set_CF(0.90)
    add.set_resule('传热热阻增大')
    res.append(add)  # 添加Rule 6

    return res
