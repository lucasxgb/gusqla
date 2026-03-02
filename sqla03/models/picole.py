import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase


from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.sabor import Sabor
from models.aditivo_nutritivo import AditivoNutritivo
from models.conservante import Conservante
from models.ingrediente import Ingrediente


from typing import List, Optional



import sqlalchemy.orm as orm

# Picole pode ter varios aditivos nutritivos
aditivos_nutritivos_picole = sa.Table(
    'aditivos_nutritivos_picole', 
    ModelBase.metadata,
    sa.Column("id_picole", sa.BigInteger, sa.ForeignKey("picoles.id")),
    sa.Column("id_aditivo_nutritivo", sa.BigInteger, sa.ForeignKey("aditivos_nutritivos.id")),
    
)


# Picole pode ter varios ingredientes
ingredientes_picole = sa.Table(
    'ingredientes_picole', 
    ModelBase.metadata,
    sa.Column("id_picole", sa.BigInteger, sa.ForeignKey("picoles.id")),
    sa.Column("id_ingrediente", sa.BigInteger, sa.ForeignKey("ingredientes.id")),
    
)

# Picole pode ter varios conservantes
conservantes_picole = sa.Table(
    'conservantes_picole', 
    ModelBase.metadata,
    sa.Column("id_picole", sa.BigInteger, sa.ForeignKey("picoles.id")),
    sa.Column("id_conservante", sa.BigInteger, sa.ForeignKey("conservantes.id")),
    
)



class Picole(ModelBase):
    __tablename__ = 'picoles' 
    __allow_unmapped__ = True
    
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement= True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index = True)
    preco: float = sa.Column(sa.DECIMAL(8,2), nullable=False)
   
    
    id_sabor = sa.Column(sa.BigInteger, sa.ForeignKey('sabores.id'))
    sabor: Sabor = orm.relationship("Sabor", lazy="joined")
    
    id_tipo_embalagem = sa.Column(sa.BigInteger, sa.ForeignKey('tipos_embalagem.id'))
    tipo_embalagem: TipoEmbalagem = orm.relationship("TipoEmbalagem", lazy="joined")
    
    id_tipo_picole = sa.Column(sa.BigInteger, sa.ForeignKey('tipos_picole.id'))
    tipo_picole: TipoPicole = orm.relationship("TipoPicole", lazy="joined")
    
    # Um picole pode ter varios ingredientes 
    ingredientes: List[Ingrediente] = orm.relationship("Ingrediente", secondary=ingredientes_picole, backref='ingrediente', lazy='joined') 
    
      # Um picole pode ter varios conservantes ou nenhum
    conservante: Optional[List[Conservante]] = orm.relationship("Conservante", secondary=conservantes_picole, backref='conservante', lazy='joined')
    
     # Um picole pode ter varios aditivos  ou nenhum
    aditivos_nutrititivos: Optional[List[AditivoNutritivo]]  = orm.relationship("AditivoNutritivo", secondary=aditivos_nutritivos_picole, backref='aditivo_nutritivo', lazy='joined')
    
    def __repr__(self) -> str:
        return f'<Picole: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preco {self.preco}>'
    
    
        