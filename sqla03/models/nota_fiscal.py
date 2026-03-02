import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase

from typing import List

from models.revendedor import Revendedor
from models.lote import Lote

import sqlalchemy.orm as orm

# Nota fiscal pode ter vários lotes
lotes_nota_fiscal = sa.Table(
    'lotes_nota_fiscal', 
    ModelBase.metadata,
    sa.Column("id_nota_fiscal", sa.BigInteger, sa.ForeignKey("notas_fiscais.id")),
    sa.Column("id_lote", sa.BigInteger, sa.ForeignKey("lotes.id")),
    
)

class NotaFiscal(ModelBase):
    __tablename__ = 'notas_fiscais' 
    __allow_unmapped__ = True
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement= True)
    data: datetime = sa.Column(sa.DateTime, default=datetime.now, index = True)
    valor: float = sa.Column(sa.DECIMAL(8,2), nullable=False)
    numero_serie: str = sa.Column(sa.String(45), nullable=False)
    descricao: str = sa.Column(sa.String(200))
    
    id_revendedor = sa.Column(sa.BigInteger, sa.ForeignKey('revendedores.id'))
    revendedor: Revendedor = orm.relationship("Revendedor", lazy="joined")
    
    # Uma nota fiscal pode ter vários lotes e um lote pode está ligado a um lote
    lotes: List[Lote] = orm.relationship('Lote', secondary=lotes_nota_fiscal, backref="lote", lazy="dynamic")
    
    def __repr__(self) -> str:
        return f'<Nota Fiscal: {self.numero_serie}>'
    
    
        