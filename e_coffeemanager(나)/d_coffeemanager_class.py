import copy

class Coffee:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock #self.stock이라고 하고 stock을 할당

def main():
    """
    음료판매관리프로그램
    """
    # 음료관련 데이터
    americano = Coffee(name='아메리카노', price=3000, stock=10)
    moca = Coffee(name='모카', price=4000, stock=10)
    latte = Coffee(name='라떼', price=5000, stock=10)
    drinks = [americano, moca, latte]
    
    sales_price = 0 # 매출

    while(True):
        print('\n=======Index=======')
        print('음료판매(1)')
        print('현황(2)')
        print('종료(3)')
        menu = int(input('입력: ')) 

        if(menu ==1):
            print('\n=====Menu=====')
            for drink in drinks:#는 name에 drinks로 넣는거자나 그러니까 name>drink로 바꿔줘. 첫번째 바퀴에는 아메리카노에 대한 정보
                    print(f'{drink.name}({drinks.index(drink)})')

            drink = int(input('\n * 음료코드: '))
            order_cnt = int(input(' * 주문수량: '))
        
            # 사용자가 입력한 음료코드가 유효한 음료코드인지 검증하고
            # 유효하지 않다면 Index로 돌려보내는 검증 로직을 작성하세요.    
            # '유효하지 않은 음료코드입니다.'
            if(drink < 0 or drink >= len(drinks)):
                print('유효하지 않은 음료코드입니다.')
                continue 

            selected = drinks[drink]
            if(selected.stock < order_cnt):
                print('재고가 없습니다.')
                continue
                
            selected.stock -= order_cnt
            sales_price += selected.price * order_cnt

            print(f'\n제품명: {selected.name}')
            print(f'판매가: {selected.price}')
            print(f'판매수량: {order_cnt}')
            print(f'결제금액: {selected.price * order_cnt}')
            print(f'남은 재고: {selected.stock}')

        elif(menu == 2):
            print('\n=======Status=======')
            for drink in drinks:
                print(f'{drink.name} | 재고: {drink.stock}')
                    
        elif(menu == 3):
            print('종료합니다.')
            break

main()