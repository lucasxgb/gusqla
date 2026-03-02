from conf.db_session import create_session # Seção de conexão ao BD
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem  import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor

from models.lote import Lote



from models.picole import Picole
from models.nota_fiscal import NotaFiscal

def insert_aditivo_nutritivo() -> AditivoNutritivo:
    print("cadastrando aditivo nutritivo")
    nome: str = input("Informe o nome do aditivo nutritivo: ")
    formula_quimica: str = input("Informe a fórmula química do aditivo nutritivo: ")
    
    an = AditivoNutritivo(nome = nome, formula_quimica = formula_quimica)
    
    with create_session() as session:
        session.add(an)
        session.commit()
        
        print(f"Cadastro realizado -> Aditivo Nutritivo")
        print(f"Nome - {an.nome}")
        print(f"Id - {an.id}")    
        print(f"Data de Criação - {an.data_criacao}")
        print(f"Formula Química- {an.formula_quimica}")
    return an


def insert_sabor():
    print("Inserindo Sabor")
    sabor: str = input("Informe o sabor a ser adicionado: ")

    
    s = Sabor(nome = sabor,)
    
    with create_session() as session:
        session.add(s)
        session.commit()
        
    print(f"Cadastro realizado -> Sabor")
    print(f"Nome - {s.nome}")
    print(f"Id - {s.id}")

def insert_tipo_embalagem():
    print("Inserindo Tipo de Embalagem")
    tipo: str = input("Informe o tipo de embalagem: ")

    
    te = TipoEmbalagem(nome = tipo,)
    
    with create_session() as session:
        session.add(te)
        session.commit()
        
    print(f"Cadastro realizado -> Tipo Embalagem")
    print(f"Nome - {te.nome}")
    print(f"Id - {te.id}")

def insert_tipo_picole():
    print("Inserindo Tipo de Picole")
    tipo: str = input("Informe o tipo de picole: ")

    
    tp = TipoPicole(nome = tipo,)
    
    with create_session() as session:
        session.add(tp)
        session.commit()
        
    print(f"Cadastro realizado -> Tipo Picole")
    print(f"Nome - {tp.nome}")
    print(f"Id - {tp.id}")
    
def insert_ingrediente() -> Ingrediente:
    print("Inserindo Ingrediente")
    ingrediente: str = input("Informe o Ingrediente: ")

    
    i = Ingrediente(nome = ingrediente,)
    
    with create_session() as session:
        session.add(i)
        session.commit()
        
    print(f"Cadastro realizado -> Ingrediente")
    print(f"Nome - {i.nome}")
    print(f"Id - {i.id}")
    
    return i
  
def insert_conservante() -> Conservante:
    print("Inserindo Conservante")
    conservante: str = input("Informe o Conservante: ")
    descricao: str = input("Informe a descrição do conservante: ")
    

    
    ct = Conservante(nome = conservante, descricao =descricao)
    
    with create_session() as session:
        session.add(ct)
        session.commit()
        
    print(f"Cadastro realizado -> Conservante")
    print(f"Nome - {ct.nome}")
    print(f"Id - {ct.id}") 
    print(f"Descricao - {ct.descricao}") 
    return ct
    
def insert_revendedor() -> Revendedor:
    print("Inserindo Revendedor")
    cnpj: str = input("Informe o CPNJ do revendedor: ")
    razao_social: str = input("Informe razão social do revendedor: ")
    contato: str = input("Informe o contato do revendedor: ")
    
    

    
    revendedor = Revendedor(cnpj = cnpj, razao_social = razao_social, contato = contato)
    
    with create_session() as session:
        session.add(revendedor)
        session.commit()
        
    return revendedor
    
def insert_lote() -> Lote:
    print("Inserindo novo Lote")
    quantidade: int = input("Informe a quantidade de Lote: ")
    id_tipo_picole: int = input("Informe o ID do tipo de picole: ")
    
    lote = Lote(quantidade = quantidade, id_tipo_picole = id_tipo_picole)
    
    with create_session() as session:
        session.add(lote)
        session.commit()
        
    return lote    
    
def insert_nota_fiscal() -> NotaFiscal:
    print("Inserindo Nota Fiscal")
    valor: float = input("Informe o valor da nota fiscal: ")

    numero_serie: str = input("Informe o numero de serie: ")
    descricao: str = input("Informe a descricao: ")
    
    id_revendedor: int = input("Informe o ID do revendedor: ")
    
    notaFiscal = NotaFiscal(valor = valor, numero_serie = numero_serie, descricao = descricao, id_revendedor = id_revendedor)
    
    lote1 = insert_lote()
    notaFiscal.lotes.append(lote1)
    
    with create_session() as session:
        session.add(notaFiscal)
        session.commit()
        
    return notaFiscal    

def insert_picole():
    print("Inserindo Picole")
    preco: float = input("Informe o valor do picole: ")
    id_sabor: int = input("Informe o ID do sabor: ")
    id_tipo_picole: int = input("Informe o ID do tipo de picole: ")
    id_tipo_embalagem: int = input("Informe o ID do tipo de embalagem: ")
        
    picole = Picole(preco = preco, id_sabor = id_sabor, id_tipo_picole = id_tipo_picole, id_tipo_embalagem = id_tipo_embalagem)
    
    ingrediente1 = insert_ingrediente()
    picole.ingredientes.append(ingrediente1)
    
    ingrediente2 = insert_ingrediente()
    picole.ingredientes.append(ingrediente2)
    
    conservante = insert_conservante()
    picole.conservante.append(conservante)
    
    
    aditivo_nutritivo = insert_aditivo_nutritivo()
    picole.aditivos_nutrititivos.append(aditivo_nutritivo)
    
    
    
    with create_session() as session:
        session.add(picole)
        session.commit()
        
        print(f'Picole cadastrado com sucesso')
        print(f'iD {picole.id}')
        print(f'Preco {picole.preco}')
        print(f'Sabor {picole.sabor.nome}')
        print(f'Tipo Picole {picole.tipo_picole.nome}')
        print(f'Tipo Embalagem {picole.tipo_embalagem.nome}')
        

        
if __name__ == "__main__":
    
    #Inserindo Aditivo Nutritivo
    #insert_aditivo_nutritivo()
    
    # Inserindo sabor
    # insert_sabor()   
    
    
    # Inserindo tipo de embalagem
    # insert_tipo_embalagem()
    
    # Inserindo tipo de picole
    # insert_tipo_picole()
    
    # Ingrediente
    # insert_ingrediente()
    
    # Conservante
    # insert_conservante()
    
    # Revendedor
    # revendedor: Revendedor = insert_revendedor()
    # print(f"Revendedor -> Cadastrado {revendedor.cnpj}")
    # print(f"Razao Social: {revendedor.razao_social}")
    # print(f"Contato: {revendedor.contato}")
    
    # Lote
    # lote: Lote = insert_lote()
    # print(f"Lote -> Cadastrado {lote.id}")
    # print(f"Quantidade {lote.quantidade}")
    # print(f"Id tipo {lote.id_tipo_picole}")
    
    # Nota Fiscal
    # nota_fiscal: NotaFiscal = insert_nota_fiscal()
    # print(f'Id da nota {nota_fiscal.id}')
    # print(f'Valor da nota {nota_fiscal.valor}')
    # print(f'N° de Série {nota_fiscal.numero_serie}')
    # print(f'Nota fiscaç desc {nota_fiscal.descricao}')
    # print(f'Id do revendedor {nota_fiscal.id_revendedor}')
    
    # Picole
    insert_picole()
    
    
    
