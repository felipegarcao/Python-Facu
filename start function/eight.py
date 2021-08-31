def funcao():
    h_i = int(input("informe a hora de inicio: "))
    m_i = int(input("informe os minutos de inicio:"))
    h_f = int(input("informe a hora final: "))
    m_f = int(input("informe o minuto final: "))
    
    if m_f < m_i:
        m_f = m_f + 60
        h_f = h_f - 1
    if h_f < h_i:
        h_f = h_f + 24

    tot_m = m_f - m_i
    tot_h = h_f - h_i
    total = tot_h * 60 + tot_m
    print(f"o total é {total} minutos")

def main():
    funcao()

main() 
