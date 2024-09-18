import hashlib
import time

def sha256(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def is_valid_hash(block_hash, target_difficulty):
    return int(block_hash, 16) < target_difficulty

def mine_block(block_header, target_difficulty):
    nonce = 0
    start_time = time.time()
    
    while True:
        header_with_nonce = block_header + str(nonce)
        
        block_hash = sha256(header_with_nonce)
        
        if is_valid_hash(block_hash, target_difficulty):
            end_time = time.time() 
            print(f"Hash válido encontrado: {block_hash}")
            print(f"Nonce utilizado: {nonce}")
            print(f"Tiempo: {end_time - start_time:.4f} segundos\n")
            break
        
        nonce += 1

def simulate_mining(block_header, difficulty_levels):
    for difficulty in difficulty_levels:
        print(f"Minando con dificultad: {difficulty}")
        mine_block(block_header, difficulty)

if __name__ == "__main__":
    block_header = "poW"
    
    difficulty_levels = [
        0x0000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
        0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
        0x000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
        0x0000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
        0x00000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  
        0x000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
        0x0000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
        0x00000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
        0x000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
        0x0000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
        0x00000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  
        0x000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF   
    ]
    
    simulate_mining(block_header, difficulty_levels)


