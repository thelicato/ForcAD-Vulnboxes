from pwn import *

def status(host, port):
    conn = remote(host, port)
    conn.recvuntil(b'>')
    conn.close()

def put_flag(host, port, token, flag_id, flag, vuln):
    conn = remote(host, port)
    conn.recvuntil(b'>')
    conn.sendline(b'2')
    conn.recvuntil(b'>')
    conn.sendline(b'2')
    conn.recvuntil(b'Token:')
    conn.sendline(token.encode('utf-8'))
    conn.recvuntil(b'ID:')
    conn.sendline(flag_id.encode('utf-8'))
    conn.recvuntil(b'Vuln:')
    conn.sendline(vuln.encode('utf-8'))
    conn.recvuntil(b'Value:')
    conn.sendline(flag.encode('utf-8'))
    received_text = conn.recvline().decode('utf-8').strip()
    conn.close()
    if not "Flag correctly set" in received_text:  
        raise Exception('Unable to set flag')
    return {"flag_id": flag_id}

def get_flag(host, port, token, flag_id, vuln):
    conn = remote(host, port)
    conn.recvuntil(b'>')
    conn.sendline(b'2')
    conn.recvuntil(b'>')
    conn.sendline(b'1')
    conn.recvuntil(b'Token:')
    conn.sendline(token.encode('utf-8'))
    conn.recvuntil(b'ID:')
    conn.sendline(flag_id.encode('utf-8'))
    conn.recvuntil(b'Vuln:')
    conn.sendline(vuln.encode('utf-8'))
    received_text = conn.recvline().decode('utf-8').strip()
    conn.close()
    return {"flag": received_text}