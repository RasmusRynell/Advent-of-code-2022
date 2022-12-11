import json
import sys
import os

def eval_operation(lhs, operation, rhs, reduce):
    return reduce((lhs + rhs) if "+" in operation else (lhs * rhs))

def eval_test(test, value):
    return value % test == 0

monkeys = {}

if __name__ == "__main__":
    part = 2
    
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        data = f.read().split('\n\n')
        for monkey in data:
            monkey = monkey.split('\n')
            monkey_id = int(monkey[0].split(' ')[1][:-1])
            items = [int(x) for x in monkey[1].split(':')[1].split(',')]
            operation = monkey[2].split(' ')[5:]
            test = monkey[3].split(' ')[3:]
            test_passed_new_monkey_id = int(monkey[4].split()[-1])
            test_failed_new_monkey_id = int(monkey[5].split()[-1])
            monkeys[monkey_id] = {
                  'items': items,
                  'operation': operation,
                  'test': int(test[-1]),
                  'test_passed_new_monkey_id': test_passed_new_monkey_id,
                  'test_failed_new_monkey_id': test_failed_new_monkey_id,
                  'times_inspected': 0,
            }

    for round in range(20 if part == 1 else 10_000):
        for monkey_id, monkey in monkeys.items():
            for item in monkey['items']:

                monkey['times_inspected'] += 1
                lhs = item
                opp = monkey['operation'][1]
                rhs = int(monkey['operation'][2]) if monkey['operation'][2].isdigit() else item

                new_item_level = eval_operation(lhs, opp, rhs, (lambda x: x // 3) if (part == 1) else (lambda x: x % 223092870))
                # 223092870 is the product of 2,3,5,7,11,13,17,19,23 (All test numbers from input file) (23 is from the test file)
                
                test_eval_result = eval_test(monkey['test'], new_item_level)
                if test_eval_result:
                    monkeys[monkey['test_passed_new_monkey_id']]['items'].append(new_item_level)
                else:
                    monkeys[monkey['test_failed_new_monkey_id']]['items'].append(new_item_level)
            monkey['items'] = []


    for monkey_id, monkey in monkeys.items():
        print(f"Monkey {monkey_id} has {monkey['items']} items and inspected {monkey['times_inspected']} items")

    top_monkeys = sorted(monkeys.items(), key=lambda x: x[1]['times_inspected'], reverse=True)[:2]
    print({top_monkeys[0][1]['times_inspected'] * top_monkeys[1][1]['times_inspected']})

    #print(json.dumps(monkeys, indent=2, sort_keys=True))
