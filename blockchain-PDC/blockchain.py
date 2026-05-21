import hashlib
import json

class Block:
    def __init__(self,index,timestamp,data,prior_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prior_hash = prior_hash
        self.hash = self.create_hash()

    def create_hash(self):
        blockstring = f"{self.index}{self.prior_hash}{self.timestamp}{self.data}".encode()

        return hashlib.sha256(blockstring).hexdigest()

    
class StudentBlock:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, '29/11/1979', 'MyFirstBlockChainUVV.br','0')
    
    def get_last_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        new_block.prior_hash = self.get_last_block().hash
        new_block.hash = new_block.create_hash()
        self.chain.append(new_block)
    
    def valiadating_blockchain(self):
        for i in range(1,len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.create_hash():
                return False
            if current_block.prior_hash != previous_block.hash:
                return False
            
        return True

if __name__ == "__main__":
    student_coin = StudentBlock()
    firstblock = student_coin.create_genesis_block()
    student_coin.add_block(Block(1,'12/12/1999','amount = 27'))
    student_coin.add_block(Block(2,'01/01/2000','amount = 13'))
    student_coin.add_block(Block(3,'02/01/2000','amount = 75'))

    print(json.dumps(student_coin.chain, default=lambda o: o.__dict__,indent=4))


    print('Blockchain validá ?' + str(student_coin.valiadating_blockchain()))

    student_coin.chain[1].data = 'amount = 28'
    print('Blockchain apos alteracao de dados valida?' + str(student_coin.valiadating_blockchain()))

    student_coin.chain[1].hash = student_coin.chain[1].create_hash()
    print('Blockchain apos atualizar o hash valida?' + str(student_coin.valiadating_blockchain()))
