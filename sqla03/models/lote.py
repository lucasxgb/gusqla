import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime
from models.model_base import ModelBase


from models.tipo_picole import TipoPicole



class Lote(ModelBase):
    __tablename__ = 'lotes' 
    __allow_unmapped__ = True
    
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement= True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index = True)
    
    quantidade: str = sa.Column(sa.Integer, nullable=False)
    
    id_tipo_picole: int = sa.Column(sa.BigInteger, sa.ForeignKey('tipos_picole.id')) #tabela.campo
    tipo_picole : TipoPicole = orm.relationship("TipoPicole", lazy="joined")

    
    def __repr__(self) -> str:
        return f'<Lote: {self.id}>'
    
    
        